<script setup>
defineProps({
  titulo: String,
  descripcion: String,
  imagen: String,
  accion: String 
})
</script>

<template>
  <div class="card">
    <img :src="imagen" alt="Imagen de la tarjeta" class="card-img" />
    <div class="card-content">
      <h3 class="card-title">{{ titulo }}</h3>
      <p class="card-description">{{ descripcion }}</p>
      <a 
        v-if="accion && accion.startsWith('http')" 
        :href="accion" 
        target="_blank" 
        rel="noopener noreferrer" 
        class="card-button">
        Ver más
      </a>
    </div>
  </div>
</template>


<style scoped>
.card {
  max-width: 320px;
  border: 1px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.25);
  transition: transform 0.3s ease;
  background-color: #ffffff;
  margin: 3rem;
}

.card:hover {
  transform: translateY(-5px);
}

.card-img {
  width: 100%;
  height: 200px;
}

.card-content {
  padding: 1rem;
  text-align: center;
}

.card-title {
  font-size: 1.3rem;
  font-weight: bold;
  color: #4f74f9;
  margin-bottom: 0.5rem;
}

.card-description {
  font-size: 0.95rem;
  color: #555;
  margin-bottom: 1rem;
  text-align: center;
}

.card-button {

  background-color: #4f74f9;
  color: #fff;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  transition: background-color 0.3s ease;
  text-decoration: none;
}

.card-button:hover {
  background-color: #06b5f8;
}
</style>
