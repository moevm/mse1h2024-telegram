import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', name: 'Login', component: Login},
    {path: '/admin', name: "admin", component: () => import('@/views/AdminPanel.vue'), children: [
        {path: 'tables', name: "tables", component: () => import('@/views/TablesPage.vue')},
        {path: 'teachers', name: "teachers", component: () => import('@/views/TeachersPage.vue')},
        {path: 'logs', name: "logs", component: () => import('@/views/LogsPage.vue')}
      ]},
  ]
})

export default router
