<<<<<<< HEAD
import { createRouter, createWebHistory } from "vue-router"
import LoginPage from "@/views/LoginPage.vue"
import AdminPanel from "@/views/AdminPanel.vue"
import TablesPage from "@/views/TablesPage.vue"
import TeachersPage from "@/views/TeachersPage.vue"
import LogsPage from "@/views/LogsPage.vue"
=======
import { createRouter, createWebHistory } from 'vue-router'
import LoginPage from '@/views/LoginPage.vue'
import AdminPanel from '@/views/AdminPanel.vue'
import TablesPage from '@/views/TablesPage.vue'
import TeachersPage from '@/views/TeachersPage.vue'
import LogsPage from '@/views/LogsPage.vue'
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
<<<<<<< HEAD
      path: "/",
      name: "Login",
=======
      path: '/',
      name: 'Login',
>>>>>>> 0b583128bfe77ebe54a88a7a44e614543cc2985a
      component: LoginPage
    },
    {
      path: "/admin",
      name: "admin",
      component: AdminPanel,
      children: [
        {
          path: "tables",
          name: "tables",
          component: TablesPage
        },
        {
          path: "teachers",
          name: "teachers",
          component: TeachersPage
        },
        {
          path: "logs",
          name: "logs",
          component: LogsPage
        }
      ]
    },
  ]
})

export default router
