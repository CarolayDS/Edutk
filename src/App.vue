<script setup>
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'
import BarraMenu from './components/BarraMenu.vue'
import Ultimo from './components/Ultimo.vue'
import Auth from './components/Auth.vue'

import { store } from './store'
import { supabase } from '../supabase'

// Al montar el componente, verificamos si ya hay usuario
onMounted(async () => {
  const { data, error } = await supabase.auth.getUser()
  if (!error) {
    store.state.user = data.user
  }

  // Escuchamos cambios de sesión (login/logout)
  supabase.auth.onAuthStateChange((_event, session) => {
    store.state.user = session?.user || null
  })
})
</script>

<template>
  <!-- Si no hay usuario logueado -->
  <Auth v-if="!store.state.user" />

  <!-- Si hay usuario logueado -->
  <div v-else class="layout">
    <header>
      <BarraMenu />
    </header>

    <main class="main">
      <RouterView />
    </main>

    <footer>
      <Ultimo />
    </footer>
  </div>
</template>

<style scoped>
.layout {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
  overflow-x: hidden;
}

.main {
  padding-top: 100px;
  flex: 1;
}
</style>
