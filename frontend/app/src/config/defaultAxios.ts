import axios from "axios";

const apiUrl = import.meta.env.VITE_BACKEND_URL;
const axiosInstance = axios.create({
  baseURL: `${apiUrl}api`,
});

export default axiosInstance;