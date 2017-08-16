<template>
    <div>
        <select class="custom-select">
            <option selected="">Choose an organization</option>
            <option v-for="orga in orgas.results" v-bind:value="orga.name">
               {{ orga.name }} 
            </option>
        </select>
        <h1>Dashboard</h1>
        <h2>{{ keys.count }} / {{ quotas.max_keys.value }}</h2>
        <h2>{{ orgas.count }} / {{ quotas.max_orgas.value }}</h2>
        Wesh gro
    </div>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  // middleware: 'auth',
  layout: 'dashboard',
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    let keys = await axios.get('/keys/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    let orgas = await axios.get('/organizations/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_keys: quotas.data['results'][0], max_orgas: quotas.data['results'][1]}
    return { quotas: quotas, keys: keys.data, orgas: orgas.data }
  }
}
</script>
