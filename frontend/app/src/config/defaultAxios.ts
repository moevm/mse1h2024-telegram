import axios, { type AxiosInstance } from 'axios'
import router from '@/router/index'

const apiUrl: any = import.meta.env.VITE_BACKEND_URL
const axiosInstance: AxiosInstance = axios.create({
  baseURL: `${apiUrl}api`
})

axiosInstance.interceptors.request.use((config) => {
  const token: string | null = localStorage.getItem('token')
  config.headers['Authorization'] = `Bearer ${token}`
  return config
})

axiosInstance.interceptors.response.use(
  (response) => {
    return response
  },
  (error) => {
    if (error.response && error.response.status === 403) {
      router.push('/')
    }
    return Promise.reject(error)
  }
)

export default axiosInstance
