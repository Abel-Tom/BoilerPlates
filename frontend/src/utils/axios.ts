import axios from 'axios';
import { BASE_URL } from '../common/constants';
import eventBus from '../common/EventBus';

const axiosInstance = axios.create({
  baseURL: BASE_URL,
  headers: {
    Authorization: `Bearer ${localStorage.getItem('access')}`
  }
});

axiosInstance.interceptors.response.use(
  response => {
    if (response.config.url === 'auth/logout/'){
      console.log('axe resp obj ', response.config.url);
      axiosInstance.interceptors.request.use(
        config => {
          if(config.headers){
            config.headers['Authorization'] = ``;
          }
              return config;
          },
          error => {
              return Promise.reject(error);
          }
      );
      localStorage.removeItem("refresh");
      localStorage.removeItem("access");
    }
    return response
  },
  error => {
    
    if (error.response.status === 401 && error.response.data.messages && 
        error.response.data.messages[0].message === 'Token is invalid or expired'
    ){
        console.log('token invalid');
        const refresh = localStorage.getItem("refresh");

        axiosInstance
        .post(BASE_URL + "auth/login/refresh/", {
            refresh
        })
        .then(response => {
            if (response.data.refresh) {
            localStorage.setItem("refresh", response.data.refresh);
            }
            if (response.data.access) {
            localStorage.setItem("access", response.data.access);
            axiosInstance.interceptors.request.use(
              config => {
                if(config.headers){
                  config.headers['Authorization'] = `Bearer ${localStorage.getItem('access')}`;
                }
                    return config;
                },
                error => {
                    return Promise.reject(error);
                }
            );
            return axiosInstance.request(error.config);
            }
            return response.data.access;
        })
        .catch(error => {
            eventBus.dispatch("logout");
            console.log('error resp2', error)
            return error
        });
    }
    else{
        return Promise.reject(error);
    }
    
});

export default axiosInstance;