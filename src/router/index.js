import { createRouter, createWebHistory } from 'vue-router'
import Inicio from '../pages/inicio.vue'
import examenes from '../pages/examenes.vue'
import Materiales from '../pages/Materiales.vue'
import Correccion from '../pages/Correccion.vue'


const routes = [
  { path: '/', name: 'inicio', component: Inicio },
  { path: '/materiales', name: 'Materiales', component: Materiales },
  { path: '/correccion', name: 'Correcion', component: Correccion},
  { path: '/examenes', name:'examenes', component: examenes},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
