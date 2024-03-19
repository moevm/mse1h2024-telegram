import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', name: 'Login', component: Login},
    {path: '/tables', name: "tables", component: () => import('@/components/TablesPage.vue')},
    {path: '/teachers', name: "teachers", component: () => import('@/components/TeachersPage.vue')},
    {path: '/logs', name: "logs", component: () => import('@/components/LogsPage.vue')}
})

export default router