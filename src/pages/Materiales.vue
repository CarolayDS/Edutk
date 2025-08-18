<script setup>
import Banner from '../components/Banner.vue'
import Tarjetita from '../components/Tarjetita.vue'
import auditorio from '../assets/auditorio.png'
import primaria from '../assets/primaria.png'
import secundaria from '../assets/secundaria.png'
import banner2 from '../assets/banner2.png'
import gamma from '../assets/gamma.jpg'
import scribe from '../assets/scribe.jpg'
import writesonic from '../assets/writesonic.png'
</script>

<template>
    <div>
        <Banner
            title="MATERIALES"
            description="Estas tecnologías avanzadas están revolucionando sectores clave como la educación, la salud, el comercio y la industria, brindando soluciones innovadoras para mejorar la eficiencia y calidad en el trabajo."
            :image="banner2"
        />
        <div class="tarjetas-container">
            <Tarjetita
            titulo="Gamma"
            descripcion="Gamma es una plataforma de IA que permite crear presentaciones y contenido visual interactivo. La IA ayuda a generar diapositivas y gráficos automáticamente, optimizando el tiempo de los docentes para crear materiales educativos atractivos y efectivos."
            :imagen="gamma"
            :accion="'https://gamma.app/es'"
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

        </div>
    </div>
</template>

<style scoped>
.tarjetas-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem; /* espacio entre tarjetas */
  padding: 1rem 1rem;
}
</style>
