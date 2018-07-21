import axios from 'axios'

console.log(process.env.endpoint)
console.log(process.env.ENDPOINT)
export default axios.create({
  baseURL: process.env.endpoint,
  timeout: 20000
})
