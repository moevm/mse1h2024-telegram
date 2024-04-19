import axios, { type AxiosInstance } from 'axios'

const apiUrl: any = import.meta.env.VITE_BACKEND_URL
const axiosInstance: AxiosInstance = axios.create({
  baseURL: `${apiUrl}api`
})

export default axiosInstance
