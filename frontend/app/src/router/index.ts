import { createRouter, createWebHistory, type NavigationGuardNext, type RouteLocationNormalized } from 'vue-router'
import axios from '@/config/defaultAxios'
import LoginPage from '@/views/LoginPage.vue'
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
      component: LoginPage
    },
    {
      path: '/admin',
      name: 'admin',
      component: AdminPanel,
      children: [
        {
          path: 'tables',
          name: 'tables',
          component: TablesPage
        },
        {
          path: 'teachers',
          name: 'teachers',
          component: TeachersPage
        },
        {
          path: 'logs',
          name: 'logs',
          component: LogsPage
        }
      ]
    }
  ]
})

router.beforeEach(
  (to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) => {
    if (to.name !== 'Login') {
      axios
        .get('/auth/test-token')
        .then(() => next())
        .catch(() => next({ name: 'Login' }))
    } else {
      next()
    }
  }
)

export default router
