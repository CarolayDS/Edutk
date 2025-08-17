<script setup>
import Banner from '../components/Banner.vue'
import nosotros1 from '../assets/nosotros1.png'
import edutk from  '../assets/edutk.png'
</script>

<template>
  <div class="contenido">
        <!-- IMAGEN NOSOTROS -->
        <Banner
            title="NOSOTROS"
            description="Somos EduTK, una startup peruana innovadora dedicada a transformar la educación mediante el uso de tecnologías educativas."
            :image="nosotros1"
        />

        <!-- Contenido HISTORIA JPB -->
        <div class="historia-contenedor">
            <!-- Columna de Historia  -->
            <div class="columna texto-col">
                <h1>¿Quienes somos?</h1>
                <p class="descripcion">
                    En EduTK, somos una startup peruana comprometida con la innovación educativa. Utilizamos tecnologías avanzadas para ofrecer soluciones prácticas y efectivas que mejoran la labor docente. Nos especializamos en automatizar el proceso de creación y corrección de exámenes, con el objetivo de reducir la carga laboral de los educadores y promover su bienestar. Nuestro enfoque está en proporcionar herramientas que optimicen el tiempo y esfuerzo de los docentes, permitiéndoles dedicar más energía al proceso de enseñanza y al desarrollo de los estudiantes. A través de nuestra plataforma, buscamos transformar la educación de manera accesible, eficiente y saludable para todos los involucrados en el proceso educativo.
                </p>
            </div>
            <!-- Columna de imagen -->
            <div class="columna imagen-col">
                <img :src="edutk" alt="Ing" class="insignia_pardo-img" />
            </div>
        </div>
  </div>
</template>

<style scoped>
.contenido {
  text-align: center;
  margin: 0;
  padding: 0;
}
/* HISTORIA E IMAGEN */

.historia-contenedor {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;              /* separación entre columnas */
  max-width: 1000px;
  margin: 2rem auto;      /* centra horizontal y separa vertical */
  padding: 0 1rem;        /* espacio en móviles */
}

/* Columnas individuales */
.columna {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

/* Imagen en la segunda columna */
.insignia_pardo-img {
  display: block;        /* convierte el img en bloque */
  width: 70%;
  height: auto;
  object-fit: cover;
  border-radius: 6px;
  margin: 0 auto 1rem;  /* 0 arriba, auto izquierda/derecha, 1rem abajo */
}

/* Textos */
.texto-col h1{
  color: #0731c6;
  margin-bottom: 0.5rem;
}

.descripcion {
  font-size: 0.95rem;
  color: #555;
  line-height: 1.4;
  text-align: justify;
}

/* AJUSTE EN DISPOSITIVOS MÓVILES */
@media (max-width: 768px) {
  .historia-contenedor {
    grid-template-columns: 1fr;
  }
  .vision-img {
    margin-bottom: 0.8rem;
  }
}
</style>
