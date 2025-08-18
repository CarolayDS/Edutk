<script setup>
import Banner from '../components/Banner.vue'
import mision from '../assets/mision.png'
import vision from '../assets/vision.png'
import nosotros1 from '../assets/nosotros1.png'
import edutk_inicio from  '../assets/edutk_inicio.png'
</script>

<template>
  <div class="contenido">
    <!-- Banner principal -->
    <img :src="edutk_inicio" alt="Principal  Foto" class="principal-img" />
    <h2>Startup peruana innovadora dedicada a transformar la educación en el Perú</h2>

    <!-- Galería de Misión y Visión -->
    <div class="galeria">
      <div class="item item-mision">
        <img :src="mision" alt="Misión" />
        <h3>MISIÓN</h3>
        <p class="descripcion">
          EduTK tiene como misión brindar a los docentes una herramienta eficiente para la creación y corrección de exámenes, automatizando procesos para reducir su carga laboral y promover su bienestar. A través de la tecnología, buscamos optimizar el tiempo de los docentes, permitiéndoles enfocarse en la enseñanza y el desarrollo académico de sus estudiantes, mientras mejoramos su calidad de vida y salud mental.
        </p>
      </div>
      <div class="item item-vision">
        <img :src="vision" alt="Visión" />
        <h3>VISIÓN</h3>
        <p class="descripcion">
          Ser la plataforma líder en la automatización de procesos educativos, proporcionando soluciones innovadoras para la creación y corrección de exámenes, que no solo optimicen el tiempo del docente, sino que también contribuyan a su bienestar. EduTK aspira a ser un aliado clave para los educadores, apoyando la educación de calidad sin comprometer su salud y calidad de vida.
        </p>
      </div>
    </div>

    <!-- BANNER NOSOTROS-->
    <Banner
        title="NOSOTROS"
        description="EduTK es una startup peruana innovadora dedicada a transformar la educación mediante el uso de tecnologías educativas. Con el objetivo de optimizar el tiempo de los docentes y mejorar su bienestar, ofrecemos soluciones que automatizan la creación y corrección de exámenes."
        :image="nosotros1"
        :buttons="[
        { label: 'Ver más', to: '/nosotros' },
        ]"
    />
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
  color: #0731c6;
  margin-top: 1rem;
}
.contenido h2 {
  color: #0731c6;
  margin-top: 5rem;
  margin-bottom: 1rem;
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
  width: 70%;
  margin: 0 auto 1rem;
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

</style>
