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
      <router-link :to="accion" class="card-button">
        Ver más
      </router-link>
    </div>
  </div>
</template>


<style scoped>
.card {
  max-width: 320px;
  border: 1px solid #ddd;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  transition: transform 0.3s ease;
  background-color: #fff;
  margin: 3rem;
}

.card:hover {
  transform: translateY(-5px);
}

.card-img {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.card-content {
  padding: 1rem;
  text-align: center;
}

.card-title {
  font-size: 1.2rem;
  font-weight: bold;
  color: #0731c6;
  margin-bottom: 0.5rem;
}

.card-description {
  font-size: 0.95rem;
  color: #555;
  margin-bottom: 1rem;
  text-align: center;
}

.card-button {
  background-color: #0731c6;
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
