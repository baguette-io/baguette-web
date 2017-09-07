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
                            <nuxt-link class="dropdown-item" v-for="orga in orgas.results" :key="orga.name" v-bind:to="'/dashboard/organizations/' + orga.name">
                                {{ orga.name }} 
                            </nuxt-link>
                        </div>
                    </div>
                </div>
                <div class="col-md-3"></div>
                <create-organization @success="organization_created" :show="showCreateOrganization" @close="showCreateOrganization = false" />
                <create-key @success="key_created" :show="showCreateKey" @close="showCreateKey = false" />
                <div class="col-sm-3">
                    <a class="btn btn-default" href="#" aria-label="Create Organization">
                        <i class="fa fa-plus-circle text-danger" aria-hidden="true" v-on:click="showCreateOrganization = true" ></i>
                    </a>
                    <small class="text-muted text-uppercase text-weight-light">organizations</small>
                    <div class="row">
                        <div class="col-sm-2"></div>
                        <div class="col">
                            <p class="h6">{{ orgas.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_orgas.value | int }}</span></p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-3">
                    <a class="btn btn-default" href="#" aria-label="Create Key">
                        <i class="fa fa-plus-circle text-danger" aria-hidden="true" v-on:click="showCreateKey = true" ></i>
                    </a>
                    <small class="text-muted text-uppercase text-weight-light">keys</small>
                    <div class="row">
                        <div class="col-sm-2"></div>
                        <div class="col">
                            <p class="h6">{{ keys.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_keys.value | int }}</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br />
        <div class="container">
            <div class="row">
               <div class="col-md-6">
                    <list-events />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import CreateKey from '~/components/dashboard/create/key'
import CreateOrganization from '~/components/dashboard/create/organization'
import ListEvents from '~/components/dashboard/list/events'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    CreateKey,
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
    const orgas = await axios.get('/organizations/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_keys: quotas.data['results'][0], max_orgas: quotas.data['results'][1]}
    return { quotas: quotas, keys: keys.data, orgas: orgas.data }
  },
  data: function () {
    return {
      showCreateKey: false,
      showCreateOrganization: false
    }
  },
  methods: {
    key_created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Key ', ' imported.')
      this.keys.count += 1
    },
    organization_created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Organization ', ' created.')
      this.orgas.count += 1
    }
  }
}
</script>
