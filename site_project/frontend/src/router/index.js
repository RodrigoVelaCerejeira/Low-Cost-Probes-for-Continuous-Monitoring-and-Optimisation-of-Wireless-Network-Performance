import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import DashbordView from '../views/DashbordView.vue'
import InfoView from '../views/InfoView.vue'
import RaspberriesView from '../views/RaspberriesView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: LoginView
  },

  {
    path: '/info',
    name: 'info',
    component: InfoView
  },

  {
    path: '/dashboard',
    name: 'dashbord',
    component: DashbordView
  },

  {
    path: '/raspberries',
    name: 'raspberries',
    component: RaspberriesView
  }

  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
