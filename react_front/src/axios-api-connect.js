import axios from 'axios';

const instance = axios.create({
    //baseURL: 'localhost:8000'
    baseURL:'http://localhost:8000'
})

export default instance;