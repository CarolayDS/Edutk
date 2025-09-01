<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const menuAbierto = ref(false)
const router = useRouter()

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

</script>

<template>
  <nav class="navbar">
    <div class="navbar-container">
      <!-- Logo -->
      <div class="logo">
        <img src="../assets/edutk.png" alt="Logo EDUTK" />
      </div>

      <!-- Botón hamburguesa -->
      <button
        class="hamburguesa"
        @click="menuAbierto = !menuAbierto"
        :class="{ activo: menuAbierto }"
        aria-label="Abrir menú"
      >
        <span></span>
        <span></span>
        <span></span>
      </button>

      <!-- Menú -->
      <ul class="menu" :class="{ abierto: menuAbierto }">
        <li>
          <router-link to="/" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Inicio</router-link>
        </li>
        <li>
          <router-link to="/materiales" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Herramientas IA</router-link>
        </li>
        <li>
          <router-link to="/examenes" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Generar examen</router-link>
        </li>
        <li>
          <router-link to="/correccion" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Corrección</router-link>
        </li>
         <li>
          <button @click="logout" class="btn-menu">Salir</button>
        </li>
      </ul>

    </div>
  </nav>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from "../../supabase"

const menuAbierto = ref(false)
const router = useRouter()

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

async function logout() {
  try {
    const { error } = await supabase.auth.signOut()
    if (error) throw error
    router.push('/login') // usa router de setup
  } catch (error) {
    console.error('Error al cerrar sesión:', error.message)
  }
}
</script>


<style scoped>
/* NAVBAR */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 80px;
  background: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  padding: 1rem 0;
}

.navbar-container {
  max-width: 1200px;
  margin: auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo img {
  height: 75px;
}

/* MENÚ */
.menu {
  display: flex;
  gap: 2rem;
  list-style: none;
  margin: 0;
  padding: 0;
}

.btn-menu {
  background-color: #007bff;
  color: #ffffff;
  padding: 0.5em 1.1em;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  font-size: 0.8rem;
  cursor: pointer;
  transition: background-color 0.3s ease, transform 0.2s ease;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.15);
  text-align: center;
  text-decoration: none;
  display: inline-block;
  margin-top: -5px;

}

/* HAMBURGUESA */
.hamburguesa {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 30px;
  height: 22px;
  background: none;
  border: none;
  cursor: pointer;
  z-index: 1001; /* para estar encima del menú */
}

.hamburguesa span {
  display: block;
  height: 3px;
  width: 100%;
  background: #239ac2;
  border-radius: 5px;
  transition: all 0.4s ease;
}

/* Animación al activar */
.hamburguesa.activo span:nth-child(1) {
  transform: translateY(9px) rotate(45deg);
}
.hamburguesa.activo span:nth-child(2) {
  opacity: 0;
  transform: translateX(-20px);
}
.hamburguesa.activo span:nth-child(3) {
  transform: translateY(-9px) rotate(-45deg);
}

@media (max-width: 768px) {
  .hamburguesa {
    display: flex;
  }

  .menu {
    position: fixed;
    top: 0;
    left: -100%;
    flex-direction: column;
    background: #e4eff5;
    width: 40%; /* más ancho para que los botones se vean bien */
    height: 100%;
    padding: 2rem 1.5rem;
    box-shadow: 4px 0 12px rgba(0, 0, 0, 0.1);
    transition: left 0.4s ease;
    z-index: 1000;
  }

  .menu.abierto {
    left: 0;
  }

  .menu li {
    margin: 0.5rem 0;
    list-style: none;
    width: 65%;
  }

  .menu a {
    display: flex;               /* icono + texto */
    align-items: center;          /* centra icono con texto */
    justify-content: flex-start;  /* texto alineado a la izquierda */
    gap: 10px;                    /* espacio entre icono y texto */
    background: #239ac2;          /* color de fondo botón */
    color: #fff;
    font-size: 1.1rem;
    font-weight: bold;
    padding: 0.8rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    transition: background 0.3s ease;
    width: 100%;                  /* todos igual de grandes */
    box-sizing: border-box;
  }

  .menu a:hover {
    background: #2d74dd;
  }

}


</style>

