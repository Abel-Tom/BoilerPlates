import axios from "axios";
import axiosInstance from "../utils/axios";
const API_URL = "http://localhost:8000/auth/";

class AuthService {
  login(username: string, password: string) {
    return axios
      .post(API_URL + "login/", {
        username,
        password
      })
      .then(response => {
        if (response.data.refresh) {
          localStorage.setItem("refresh", response.data.refresh);
        }
        if (response.data.access) {
          localStorage.setItem("access", response.data.access);
        }

        return response.data;
      });
  }

  loginRefresh() {
    const refresh = localStorage.getItem("refresh");
    if (refresh) {
      axios
        .post(API_URL + "login/refresh/", {
          refresh
        })
        .then(response => {
          if (response.data.refresh) {
            localStorage.setItem("refresh", response.data.refresh);
          }
          if (response.data.access) {
            localStorage.setItem("access", response.data.access);
          }
        })
        .catch(error => {
          if (error.response && error.response.status === 401) {
            if (error.response.data.detail === 'Token is blacklisted') {
              console.log('please login');
            }
          } else {
            // Handle other errors
            console.error(error);
          }
        });
    }

  }

  logOut = async () => {
    const refresh: string | null = localStorage.getItem("refresh");
    const response = await axiosInstance.post('auth/logout/', {
      "refresh_token": refresh
    });
    localStorage.removeItem("refresh");
    localStorage.removeItem("access");
    console.log(response);
  }

  register(username: string, email: string, password: string) {
    return axios.post(API_URL + "register/", {
      username,
      password,
      email,
      "password2": password,
      "first_name": username,
      "last_name": username
    });
  }

  getCurrentUser() {
    const userStr = localStorage.getItem("user");
    if (userStr) return JSON.parse(userStr);

    return null;
  }

  getAccessToken() {
    const access = localStorage.getItem("access");
    if (access) return access;

    return null;
  }
  getRefreshToken() {
    const refresh = localStorage.getItem("refresh");
    if (refresh) return refresh;

    return null;
  }
}

export default new AuthService();
