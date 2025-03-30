import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from './pages/LoginPage.vue';
import DashboardPage from './pages/Dashboard.vue';
import RaspberryPage from './pages/Raspberry.vue';
import InfoPage from './pages/InfoPage.vue';

const routes = [
  { path: '/', component: LoginPage }, // Login Page
  { path: '/main', component: DashboardPage }, // Main Page
  { path: '/info', component: InfoPage }, 
  { path: '/raspberry', component: RaspberryPage }, 
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;