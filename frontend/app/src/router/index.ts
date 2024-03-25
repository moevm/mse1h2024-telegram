import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/views/Login.vue'
import AdminPanel from '@/views/AdminPanel.vue'
import TablesPage from '@/views/TablesPage.vue'
import TeachersPage from '@/views/TeachersPage.vue'
import LogsPage from '@/views/LogsPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/admin',
      name: "admin",
      component: AdminPanel,
      children: [
        {
          path: 'tables',
          name: "tables",
          component: TablesPage
        },
        {
          path: 'teachers',
          name: "teachers",
          component: TeachersPage
        },
        {
          path: 'logs',
          name: "logs",
          component: LogsPage
        }
      ]
    },
  ]
})

export default router
