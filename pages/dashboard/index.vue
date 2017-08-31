<template>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <select class="custom-select">
                        <option selected="">Choose an organization</option>
                        <option v-for="orga in orgas.results" v-bind:value="orga.name">
                           {{ orga.name }} 
                        </option>
                    </select>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
                <div class="col-md-3"><h1>Dashboard</h1></div>
                <div class="col-md-3"></div>
                <div class="col-sm-3">
                    <small class="text-muted text-uppercase text-weight-light">organizations</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ orgas.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_orgas.value | int }}</span></p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-3">
                    <small class="text-muted text-uppercase text-weight-light">keys</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ keys.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_keys.value | int }}</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
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
