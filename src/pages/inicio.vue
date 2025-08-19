<script setup>
import Banner from '../components/Banner.vue'
import mision from '../assets/mision.png'
import vision from '../assets/vision.png' 
import nosotros1 from '../assets/nosotros_banner.png'
import edutk_inicio from  '../assets/edutk_principal.png'
import info_edutk from  '../assets/info_edutk.png'
import somos from  '../assets/somos.svg'
import Tarjetita from '../components/Tarjetita.vue'
</script>

<template>
  <div class="contenido">
    <!-- Banner principal -->
    <img :src="edutk_inicio" alt="Principal  Foto" class="principal-img" />

    <h2>Startup peruana innovadora dedicada a transformar la educación en el Perú</h2>

    <!-- Galería de Misión y Visión -->
    <div class="galeria">
          <Tarjetita
            titulo="Misión"
            descripcion="Brindar a los docentes una herramienta tecnológica que automatice la creación y corrección de exámenes, reduciendo su carga laboral y permitiéndoles dedicar más tiempo a la enseñanza, al mismo tiempo que se cuida su bienestar y salud mental."
            :imagen="mision"
          />
          <Tarjetita
            titulo="Visión"
            descripcion="Convertirse en la plataforma líder en automatización de procesos educativos, ofreciendo soluciones innovadoras que optimicen el trabajo docente, mejoren su calidad de vida y fortalezcan una educación de calidad."
            :imagen="vision"
          />
    </div>

    <img :src="nosotros1" alt="Principal  Foto" class="principal-img" />

     <!-- Contenido HISTORIA JPB -->
        <div class="historia-contenedor">
            <!-- Columna de Historia  -->
            <div class="columna texto-col">
                <h1>¿Quiénes somos?</h1>
                <p class="descripcion">
                    Somos EDUTK, un equipo de jóvenes innovadores comprometidos con transformar la educación en el Perú a través de la tecnología. Creemos que los docentes son el motor de la enseñanza y que, liberándolos de tareas repetitivas, pueden enfocarse en lo más importante: conectar con sus estudiantes y brindar una educación de calidad. Nuestro propósito es ofrecer herramientas que automaticen procesos, reduzcan la carga laboral y abran nuevas oportunidades educativas, generando un impacto positivo en docentes y estudiantes.
                </p>
            </div>
            <!-- Columna de imagen -->
            <div class="columna imagen-col">
                <img :src="somos" alt="Ing" class="img_columna" />
            </div>
        </div>


        <img :src="info_edutk" alt="Principal  Foto" class="info-img" />
</div>
</template>

<style scoped>
.contenido {
  text-align: center;
  margin: 0;
  padding: 0;
}

.principal-img,
.nosotros-img {
  width: 100%;
  object-fit: cover;
  display: block;
  margin: 0;
  padding: 0;
}

/* Títulos */
.contenido h1 {
  color: #4f74f9;
  margin-top: 1rem;
}
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

.contenido h2 {
  font-family: 'Great Vibes', cursive;
  color: #4f74f9;
  margin-top: 5rem;
  margin-bottom: 1rem;
  font-size: 1.9rem;
}


/* Galería Misión/Visión */
.galeria {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 2rem;
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 1rem;
}

.item {
  text-align: center;
}

.item img {
  width: 100%;
  margin: 3 auto 1rem;
  display: block;
  object-fit: cover;
}

.item h3 {
  color: #06b5f8;
  margin-bottom: 0.5rem;
}

.descripcion {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.4;
  text-align: justify;
}



/* Responsive */
@media (max-width: 768px) {
  .galeria {
    grid-template-columns: 1fr;
  }
  .item img {
    width: 60%;
  }
  
}


/* HISTORIA E IMAGEN */
.historia-contenedor {
  font-family: 'Great Vibes', cursive;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  max-width: 1000px;
  margin: 2rem auto;
  padding: 0 1rem;
}

/* Columnas individuales */
.columna {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Imagen en la segunda columna */
.img_columna {
  display: block;
  width: 70%;
  height: auto;
  object-fit: cover;
  margin: 0 auto 1rem;
}

.info-img {
  max-width: 100%;   /* La imagen nunca será más grande que su contenedor */
  height: auto;      /* Mantiene la proporción */
  display: block;
  margin: 0 auto;    /* Centra la imagen horizontalmente */
  padding: 0;
}


/* 📱 Responsive para celular */
@media (max-width: 768px) {
  .historia-contenedor {
    grid-template-columns: 1fr; /* pasa a 1 sola columna */
    text-align: center;
  }

  .img_columna {
    width: 90%;   /* que se vea más grande en móvil */
    margin: 1rem auto;
  }
}

</style>
