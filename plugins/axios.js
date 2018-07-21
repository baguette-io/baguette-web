import axios from 'axios'

export default axios.create({
  baseURL: process.env.endpoint,
  timeout: 20000
})
