import {
  createRouter,
  createWebHistory,
  type NavigationGuardNext,
  type RouteLocationNormalized
} from 'vue-router'
import LoginPage from '@/views/LoginPage.vue'
import AdminPanel from '@/views/AdminPanel.vue'
import TablesPage from '@/views/TablesPage.vue'
import TeachersPage from '@/views/TeachersPage.vue'
import LogsPage from '@/views/LogsPage.vue'
import StatisticsPage from '@/views/StatisticsPage.vue'
import axios from '@/config/defaultAxios'

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
      name: 'Admin',
      component: AdminPanel,
      children: [
        {
          path: 'tables',
          name: 'Tables',
          component: TablesPage
        },
        {
          path: 'teachers',
          name: 'Teachers',
          component: TeachersPage
        },
        {
          path: 'logs',
          name: 'Logs',
          component: LogsPage
        },
        {
          path: 'statistics',
          name: 'Statistics',
          component: StatisticsPage
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
