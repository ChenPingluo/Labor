import axios from "axios";
const instance = axios.create({
  baseURL: "http://localhost:5000/api/v1",
  timeout: 10000, 
});

instance.interceptors.response.use(
  (response) => response.data,
  (error) => Promise.reject(error)
);

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
});


export default instance;