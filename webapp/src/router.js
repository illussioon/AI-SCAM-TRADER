import { createRouter, createWebHistory } from 'vue-router'
import MainApp from './components/app/main-app.vue'
import MainTutorial from './components/main/main.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: MainApp
  },
  {
    path: '/tutorial',
    name: 'Tutorial', 
    component: MainTutorial
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

