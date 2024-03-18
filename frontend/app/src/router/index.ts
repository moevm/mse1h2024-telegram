import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: () => import('@/components/TablesPage.vue')},
    {path: '/teachers', component: () => import('@/components/TeachersPage.vue')},
    {path: '/logs', component: () => import('@/components/LogsPage.vue')}
  ]
})

export default router
