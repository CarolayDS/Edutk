<script setup>
import { ref } from 'vue'

const mensaje = ref('Aquí podrás cargar exámenes para corrección automática.')
</script>

<template>
  <section class="correccion">
    <h1>Corrección de Exámenes</h1>
    <p>{{ mensaje }}</p>

    <router-link to="/subir-examen" class="btn-ir">Ir a Subir Examen</router-link>
  </section>
</template>

<style scoped>
.correccion {
  max-width: 800px;
  margin: 100px auto 50px;
  text-align: center;
  padding: 40px;
  background-color: #f0f8ff;
  border-radius: 10px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  font-family: 'Segoe UI', sans-serif;
}

h1 {
  color: #01417a;
  margin-bottom: 1rem;
}

p {
  font-size: 1.1rem;
  color: #333;
  margin-bottom: 2rem;
}

.btn-ir {
  background-color: #0c2bd9;
  color: white;
  padding: 0.75em 1.5em;
  border: none;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  font-size: 1rem;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  transition: background-color 0.3s ease;
}

.btn-ir:hover {
  background-color: #544aeb;
}
</style>