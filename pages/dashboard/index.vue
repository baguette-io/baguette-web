<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <div class="dropdown shown">
                        <button class="btn dropdown-toggle btn-outline-danger" href="#" role="button" id="dropdownOrganization" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Choose an organization
                        </button>
                        <div class="dropdown-menu" aria-labelledby="dropdownOrganization">
                            <nuxt-link class="dropdown-item" v-for="orga in orgas.results" :key="orga.name" v-bind:to="'/dashboard/organizations/' + orga.organization.name">
                                {{ orga.organization.name }} 
                            </nuxt-link>
                            <div class="dropdown-divider"></div>
                            <button class="btn btn-block btn-danger" role="button" v-on:click="showCreateOrganization = true">
                                Create an organization
                            </button>
                        </div>
                    </div>
                </div>
                <div class="col-md-3"></div>
                <create-organization @success="organization_created" :show="showCreateOrganization" @close="showCreateOrganization = false" />
                <div class="col-sm-3">
                    <nuxt-link to="/dashboard/organizations/" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">organizations</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ orgas.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_orgas.value | int }}</span></p>
                            </div>
                        </div>
                    </nuxt-link>
                </div>
                <div class="col-sm-3">
                    <nuxt-link to="/dashboard/keys/" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">keys</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ keys.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_keys.value | int }}</span></p>
                            </div>
                        </div>
                    </nuxt-link>
                </div>
            </div>
        </div>
        <div class="container">
            <div class="row">
               <div class="col-md-6">
                    <list-events />
                </div>
               <div class="col-md-3">
                </div>
               <div class="col-md-3">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import CreateOrganization from '~/components/dashboard/create/organization'
import ListEvents from '~/components/dashboard/list/events'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    CreateOrganization,
    ListEvents
  },
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const keys = await axios.get('/keys/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const orgas = await axios.get('/members/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_keys: quotas.data['results'][0], max_orgas: quotas.data['results'][1]}
    return { quotas: quotas, keys: keys.data, orgas: orgas.data }
  },
  data: function () {
    return {
      showCreateOrganization: false
    }
  },
  methods: {
    organization_created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Organization ', ' created.')
      this.orgas.count += 1
    }
  }
}
</script>
