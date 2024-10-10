import { AxiosResponse } from 'axios';
import axiosInstance from '../utils/axios';
import { ThingPayload } from '../types/user.type';

const end_point: string = 'auth/user/';

class UserService {
  getCurrentUser =  (): Promise<AxiosResponse<any, any>> => {
    return axiosInstance.get(end_point)
  }
  getThings =  (): Promise<AxiosResponse<any, any>> => {
    return axiosInstance.get('things/')
  }

  createThing =  (payload: ThingPayload): Promise<AxiosResponse<any, any>> => {
    return axiosInstance.post('things/',payload)
  }
}

export default new UserService();
