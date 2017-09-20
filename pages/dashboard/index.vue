<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <select-organizations :current="''" :path="''" />
                </div>
                <div class="col-md-3"></div>
                <div class="col-sm-2">
                    <nuxt-link to="/dashboard/invitations/" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">invitations</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ invits.count | int }}</p>
                            </div>
                        </div>
                    </nuxt-link>
                </div>
                <div class="col-sm-2">
                    <nuxt-link to="/dashboard/organizations/" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">organizations</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ orgas.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_orgas.value | int }}</span></p>
                            </div>
                        </div>
                    </nuxt-link>
                </div>
                <div class="col-sm-2">
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
                    <list-events :orga="'baguette.io'" />
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
import SelectOrganizations from '~/components/dashboard/select/organizations'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    CreateOrganization,
    ListEvents,
    SelectOrganizations
  },
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const keys = await axios.get('/keys/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const invits = await axios.get('/invitations/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const orgas = await axios.get('/members/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_keys: quotas.data['results'][0], max_orgas: quotas.data['results'][1]}
    return { quotas: quotas, keys: keys.data, orgas: orgas.data, invits: invits.data }
  }
}
</script>
