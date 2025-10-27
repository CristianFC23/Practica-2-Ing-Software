import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/components/HomeView.vue'
import PacientesView from '@/components/PacientesView.vue'
import LaboratoristasView from '@/components/LaboratoristasView.vue'
import ResultadosView from '@/components/ResultadosView.vue'
import NuevaUbicacion from '@/components/NuevaUbicacion.vue'
import NuevoPersonal from '@/components/NuevoPersonal.vue'
import NuevoEquipo from '@/components/NuevoEquipo.vue'
const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/pacientes',
    name: 'pacientes',
    component: PacientesView
  },
  {
    path: '/laboratoristas',
    name: 'laboratoristas',
    component: LaboratoristasView
  },
  {
    path: '/resultados',
    name: 'resultados',
    component: ResultadosView
  },
  { 
    path: '/ubicacion/nueva',
    name: 'nuevaUbicacion',
    component: NuevaUbicacion 
  },
  {
    path: '/personal/nuevo',
    name: 'nuevoPersonal',
    component: NuevoPersonal
  },
  {
  path: '/equipo/nuevo',
  name: 'nuevoEquipo',
  component: NuevoEquipo
}
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router