<template>
    <div style="min-height:500px;">
        <hr />
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <div class="dropdown shown">
                        <button class="btn dropdown-toggle btn-outline-danger" href="#" role="button" id="dropdownOrganization" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            {{ slug }}
                        </button>
                        <div class="dropdown-menu" aria-labelledby="dropdownOrganization">
                            <nuxt-link class="dropdown-item" v-for="orga in orgas.results" :key="orga.name" v-bind:to="'/dashboard/organizations/' + orga.name">
                                {{ orga.name }} 
                            </nuxt-link>
                        </div>
                    </div>
                </div>
                <div class="col-md-1"></div>
                <div class="col-sm-2">
                    <small class="text-muted text-uppercase text-weight-light">members</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ current.stats.members | int }}</p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-2">
                    <small class="text-muted text-uppercase text-weight-light">invitations</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ current.stats.invitations | int }}</p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-2">
                    <small class="text-muted text-uppercase text-weight-light">projects</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ projects.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_projects.value | int }}</span></p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-2">
                    <small class="text-muted text-uppercase text-weight-light">vpcs</small>
                    <div class="row">
                        <div class="col">
                            <p class="h6">{{ vpcs.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_vpcs.value | int }}</span></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br />
        <div class="container">
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  async asyncData ({ params, store, error }) {
    const slug = params.slug
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      params: {'organization': slug},
      headers: {'Authorization': 'JWT ' + token}
    })
    const projects = await axios.get('/projects/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const vpcs = await axios.get('/vpcs/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const orgas = await axios.get('/organizations/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const current = await axios.get('/organizations/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_projects: quotas.data['results'][0], max_vpcs: quotas.data['results'][1]}
    return {slug: slug, quotas: quotas, projects: projects.data, vpcs: vpcs.data, orgas: orgas.data, current: current.data}
  }
}
</script>
