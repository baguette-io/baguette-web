<template>
    <div style="min-height:500px;">
        <hr />
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
        <br />
        <div class="container">
            <div class="row">
               <div class="col">
                 <small class="text-danger text-uppercase font-weight-normal">5 minutes ago</small>
                 <div class="row">
                    <div class="col">
                        <img src="/images/avatar.svg" class="rounded-circle avatar" alt="avatar" />
                        <span class="font-weight-bold">baguette.io</span>&nbsp;fail to deploy on&nbsp;<small class="text-muted text-uppercase text-weight-light">staging</small>

                    </div>
                 </div>
               </div>
            </div>

            <div class="row">
               <div class="col">
                 <small class="text-muted text-uppercase font-weight-normal">25 minutes ago</small>
                 <div class="row">
                    <div class="col">
                        <img src="/images/avatar.svg" class="rounded-circle avatar" alt="avatar" />
                        <span class="font-weight-bold">David</span>&nbsp;deploy&nbsp;<span class="font-weight-bold">baguette.io</span>&nbsp;on&nbsp;<small class="text-muted text-uppercase text-weight-light">staging</small>
                    </div>
                 </div>
               </div>
            </div>

            <div class="row">
               <div class="col">
                 <small class="text-muted text-uppercase font-weight-normal">1 hour ago</small>
                 <div class="row">
                    <div class="col">
                        <img src="/images/avatar.svg" class="rounded-circle avatar" alt="avatar" />
                        <span class="font-weight-bold">Charles</span>&nbsp;added David to&nbsp;<span class="font-weight-bold">baguette.io</span>&nbsp;<small class="text-muted text-uppercase text-weight-light">organization</small>
                    </div>
                 </div>
               </div>
            </div>

            <div class="row">
               <div class="col">
                 <small class="text-success text-uppercase font-weight-normal">2 hour ago</small>
                 <div class="row">
                    <div class="col">
                        <img src="/images/avatar.svg" class="rounded-circle avatar" alt="avatar" />
                        <span class="font-weight-bold">baguette.io</span>&nbsp;success to deploy on&nbsp;<small class="text-muted text-uppercase text-weight-light">master</small>

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
  middleware: 'auth',
  layout: 'dashboard',
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
  }
}
</script>
