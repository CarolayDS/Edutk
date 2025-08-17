# backend/main.py
from dotenv import load_dotenv
load_dotenv()

import os, json, tempfile, logging
from typing import Optional
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ---- Document AI ----
from google.cloud import documentai
from google.api_core.client_options import ClientOptions

# ---- Gemini (lib oficial) ----
import google.generativeai as genai

log = logging.getLogger("uvicorn.error")

# =========================
# Credenciales / Config
# =========================
# 1) Gemini
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_GENAI_API_KEY")
if not GEMINI_API_KEY:
    log.warning("Falta GEMINI_API_KEY/GOOGLE_GENAI_API_KEY")
else:
    genai.configure(api_key=GEMINI_API_KEY)

# 2) Document AI
# En producción: usa GOOGLE_APPLICATION_CREDENTIALS_JSON (contenido del json)
# En local: puedes usar GOOGLE_APPLICATION_CREDENTIALS=backend/google_ocr.json
GOOGLE_JSON = os.getenv("GOOGLE_APPLICATION_CREDENTIALS_JSON")
if GOOGLE_JSON:
    t = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
    t.write(GOOGLE_JSON.encode()); t.flush()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = t.name
elif not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    log.warning("No hay credenciales de Google configuradas.")

PROJECT_ID   = os.getenv("DOC_PROJECT_ID", "appnw-13290")
LOCATION     = os.getenv("DOC_LOCATION", "us")
PROCESSOR_ID = os.getenv("DOC_PROCESSOR_ID", "da39f9cbf3f49f2e")

docai_client = documentai.DocumentProcessorServiceClient(
    client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
)
processor_name = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

# =========================
# FastAPI + CORS
# =========================
app = FastAPI(title="OCR + Grade API")

ALLOWED_ORIGINS = [
    "http://localhost:5173", "http://127.0.0.1:5173",
    "http://localhost:5174", "http://127.0.0.1:5174",
    "http://localhost:8000"
]
FRONTEND_ORIGIN = os.getenv("FRONTEND_ORIGIN")  # en prod: https://tu-app.vercel.app
if FRONTEND_ORIGIN:
    ALLOWED_ORIGINS = [FRONTEND_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# Helpers
# =========================
def run_ocr_bytes(file_bytes: bytes, mime_type: str) -> str:
    raw_document = documentai.RawDocument(content=file_bytes, mime_type=mime_type)
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    response = docai_client.process_document(request=request)
    return response.document.text or ""

def grade_text_with_gemini(text: str, rubric: Optional[str] = None, model: str = "gemini-1.5-flash") -> dict:
    if not GEMINI_API_KEY:
        raise RuntimeError("Gemini no está configurado (GEMINI_API_KEY).")

    rubric_prompt = rubric or (
        "Evalúa el examen del estudiante. El archivo contiene las respuestas a un examen con un rango de preguntas numeradas. "
        "El examen está dividido en las siguientes secciones: "
        "1. Nombre del estudiante (Ejemplo: Juan Pérez). "
        "2. Grado y sección (Ejemplo: 3ro, Sección A). "
        "3. Las preguntas del examen. "
        "4. Respuestas a las preguntas del examen. "
        "Para cada respuesta, indica lo siguiente: "
        " - numero_pregunta, "
        " - pregunta (texto literal de la pregunta), "
        " - respuesta_estudiante (texto literal del alumno), "
        " - correccion (explicación correcta), "
        " - correcta (true o false). "
        "NO calcules la nota final, solo indica si es correcta o incorrecta. "
        "Devuelve SOLO un JSON válido con la siguiente estructura: "
        "{"
        "  'nombre_estudiante': nombre, "
        "  'grado': grado, "
        "  'seccion': seccion, "
        "  'resumen_feedback': resumen, "
        "  'respuestas': ["
        "     {"
        "       'numero_pregunta': numero, "
        "       'pregunta_texto': texto, "
        "       'respuesta_estudiante': texto, "
        "       'correccion': texto, "
        "       'correcta': true/false "
        "     }"
        "  ]"
        "}"
    )

    prompt = f"""Eres un corrector experto.
Usa esta rúbrica:
{rubric_prompt}

Califica el siguiente examen y responde SOLO en JSON:
\"\"\"{text}\"\"\""""

    mdl = genai.GenerativeModel(model)
    resp = mdl.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(response_mime_type="application/json")
    )

    response_text = resp.text
    grade_json = json.loads(response_text)

    respuestas = grade_json.get("respuestas", [])
    total = len(respuestas)
    correctas = sum(1 for r in respuestas if r.get("correcta") is True)
    grade_json["nota_final"] = round((correctas / total) * 20, 2) if total else 0
    grade_json["total_preguntas"] = total
    grade_json["correctas"] = correctas
    return grade_json

# =========================
# Schemas
# =========================
class GradeBody(BaseModel):
    text: str
    rubric: Optional[str] = None
    model: Optional[str] = "gemini-2.0-flash"

# =========================
# Endpoints
# =========================
@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ocr")
async def ocr(file: UploadFile = File(...)):
    if file.content_type not in {"application/pdf", "application/octet-stream", "image/jpeg", "image/png"}:
        raise HTTPException(status_code=400, detail="Sube PDF o imagen válida (JPEG/PNG).")
    try:
        contents = await file.read()
        mime = file.content_type if file.content_type != "application/octet-stream" else "application/pdf"
        text = run_ocr_bytes(contents, mime)
        return {"text": text}
    except Exception as e:
        log.exception("OCR error")
        raise HTTPException(status_code=500, detail=f"OCR error: {e}")

@app.post("/ocr-grade")
async def ocr_and_grade(file: UploadFile = File(...), rubric: Optional[str] = None, model: Optional[str] = "gemini-1.5-flash"):
    if file.content_type not in {"application/pdf", "application/octet-stream", "image/jpeg", "image/png"}:
        raise HTTPException(status_code=400, detail="Sube PDF o imagen válida.")
    try:
        contents = await file.read()
        mime = file.content_type if file.content_type != "application/octet-stream" else "application/pdf"
        text = run_ocr_bytes(contents, mime)
        grade_result = grade_text_with_gemini(text, rubric, model or "gemini-1.5-flash")
        return {"text": text, "grade": grade_result}
    except Exception as e:
        log.exception("OCR+Grade error")
        raise HTTPException(status_code=500, detail=f"OCR+Grade error: {e}")
