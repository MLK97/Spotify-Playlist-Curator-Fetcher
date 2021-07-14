import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/Home.vue'
import SearchView from '../views/Search.vue'
import AuthView from '../views/Auth.vue'

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path: '/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/auth',
    name: 'AuthView',
    component: AuthView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
