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
        <img src="../assets/edutk.png" alt="Logo JPB" />
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
          <router-link to="/nosotros" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Nosotros</router-link>
        </li>
        <li>
          <router-link to="/niveles" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Materiales</router-link>
        </li>
        <li>
          <router-link to="/examenes" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Exámenes</router-link>
        </li>
        <li>
          <router-link to="/normasconvivencia" class="btn-menu" @click="menuAbierto = false; scrollToTop()">Corrección</router-link>
        </li>
         <li>
          <button @click="logout" class="btn-menu">Salir</button>
        </li>
      </ul>

    </div>
  </nav>
</template>

<script>
import { supabase } from "../../supabase"; // Asegúrate de importar supabase si lo necesitas

export default {
  methods: {
    async logout() {
      try {
        const { error } = await supabase.auth.signOut();
        if (error) throw error;
        // Redirige al login o a la página de inicio
        this.$router.push('/login');
      } catch (error) {
        console.error('Error al cerrar sesión:', error.message);
      }
    },
    scrollToTop() {
      window.scrollTo(0, 0);
    }
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
  background-color: #06b5f8 ;
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

.btn-menu:hover {
  background-color: #0731c6;
  transform: scale(1.05);
}


/* HAMBURGUESA */
.hamburguesa {
  display: none;
  flex-direction: column;
  justify-content: space-between;
  width: 26px;
  height: 20px;
  background: none;
  border: none;
  cursor: pointer;
}

.hamburguesa span {
  display: block;
  height: 3px;
  background: #239ac2;
  border-radius: 3px;
  transition: all 0.3s ease;
}

.hamburguesa.activo span:nth-child(1) {
  transform: translateY(8px) rotate(45deg);
}
.hamburguesa.activo span:nth-child(2) {
  opacity: 0;
}
.hamburguesa.activo span:nth-child(3) {
  transform: translateY(-8px) rotate(-45deg);
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .hamburguesa {
    display: flex;
  }

  .menu {
    position: absolute;
    top: 80px;
    left: 0;
    flex-direction: column;
    background: #fff;
    width: 100%;
    padding: 1rem 2rem;
    display: none;
    z-index: 999;
  }

  .menu.abierto {
    display: flex;
  }

  .menu li {
    margin-bottom: 1rem;
  }
}
</style>

