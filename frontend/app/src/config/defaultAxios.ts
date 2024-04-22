import axios, { type AxiosInstance } from 'axios'

const apiUrl: any = import.meta.env.VITE_BACKEND_URL
const axiosInstance: AxiosInstance = axios.create({
  baseURL: `${apiUrl}api`
})

axiosInstance.interceptors.request.use((config) => {
  const token: string | null = localStorage.getItem('token')
  config.headers['Authorization'] = `Bearer ${token}`
  return config
})

export default axiosInstance
