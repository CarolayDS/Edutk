<script setup>
import Banner from '../components/Banner.vue'
import Tarjetita from '../components/Tarjetita.vue'
import banner2 from '../assets/banner2.png'
import gamma from '../assets/gamma.jpg'
import materiales_banner from '../assets/materiales_banner.png'
import scribe from '../assets/scribe.jpg'
import quizziz from '../assets/quizziz.jpg'
import leonardo from '../assets/leonardo.png'
import wolfram from '../assets/wolfram.png'
import writesonic from '../assets/writesonic.png'
</script>

<template>
    <div>
        <img :src="materiales_banner" alt="Principal  Foto" class="principal-img" />
        <div class="tarjetas-container">
            <Tarjetita
            titulo="Gamma"
            descripcion="Gamma es una plataforma de IA que permite crear presentaciones y contenido visual interactivo. La IA ayuda a generar diapositivas y gráficos automáticamente, optimizando el tiempo de los docentes para crear materiales educativos atractivos y efectivos."
            :imagen="gamma"
            :accion="'https://gamma.app'"
            />

            <Tarjetita
            titulo="Scribe"
            descripcion="Scribe es una herramienta de IA diseñada para crear tutoriales y guías paso a paso. Los docentes pueden grabar sus procesos y la IA generará automáticamente un tutorial interactivo, ideal para explicar conceptos complejos a los estudiantes de manera fácil."
            :imagen="scribe"
            :accion="'https://creati.ai/es/ai-tools/scribe-ai-documentation-sops-screenshots/'"
            />

            <Tarjetita
            titulo="WriteSonic"
            descripcion="WriteSonic es una herramienta de generación de contenido con IA que permite a los profesores crear artículos, resúmenes, y material educativo en cuestión de segundos. Su inteligencia artificial ayuda a redactar textos coherentes y bien estructurados para el aula."
            :imagen="writesonic"
            :accion="'https://writesonic.com/'"
            />

            <Tarjetita
            titulo="Quizizz"
            descripcion="Plataforma para realizar quizzes gamificados. Ahora incluye IA para generar preguntas automáticamente."
            :imagen="quizziz"
            :accion="'https://Quizizz.com'"
            />
            
            <Tarjetita
            titulo="Leonardo AI"
            descripcion="Plataforma de generación de imágenes con IA, ideal para crear ilustraciones, recursos visuales y materiales didácticos de alta calidad."
            :imagen="leonardo"
            :accion="'https://leonardo.ai/'"
            />

            <Tarjetita
            titulo="Wolfram Alpha"
            descripcion="Un motor de conocimiento computacional que responde preguntas y realiza cálculos complejos con explicaciones paso a paso."
            :imagen="wolfram"
            :accion="'https://www.wolframalpha.com/'"
            />

        </div>
    </div>
</template>

<style scoped>
.principal-img {
  width: 100%;
  object-fit: cover;
  display: block;
  margin: 0;
  padding: 0;
}
.tarjetas-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem; /* espacio entre tarjetas */
  padding: 1rem 1rem;
}
</style>
