<template>
    <div>
        <div style="min-height:500px;">
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <breadcrumb :items="breadcrumbs" />
                    </div>
                    <div class="col-sm-2">
                      <nuxt-link :to="'/dashboard/organizations/' + slug + '/members/'" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">members</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ current.stats.members | int }}</p>
                            </div>
                        </div>
                      </nuxt-link>
                    </div>
                    <div class="col-sm-2">
                      <nuxt-link :to="'/dashboard/organizations/' + slug + '/invitations/'" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">invitations</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ current.stats.invitations | int }}</p>
                            </div>
                        </div>
                      </nuxt-link>
                    </div>
                    <div class="col-sm-2">
                      <nuxt-link :to="'/dashboard/organizations/' + slug + '/projects/'" class="text-no-decoration">
                        <small class="text-muted text-uppercase text-weight-light">projects</small>
                        <div class="row">
                            <div class="col">
                                <p class="h6">{{ projects.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_projects.value | int }}</span></p>
                            </div>
                        </div>
                      </nuxt-link>
                    </div>
                    <div class="col-sm-2">
                        <nuxt-link :to="'/dashboard/organizations/' + slug + '/vpcs/'" class="text-no-decoration">
                            <small class="text-muted text-uppercase text-weight-light">vpcs</small>
                            <div class="row">
                                <div class="col">
                                    <p class="h6">{{ vpcs.count | int }} <span class="text-muted text-weight-light">/ {{ quotas.max_vpcs.value | int }}</span></p>
                                </div>
                            </div>
                        </nuxt-link>
                    </div>
                </div>
            </div>
            <br />
            <div class="container">
                <list-events :orga="slug" />
            </div>
        </div>
    </div>
</template>

<script>
import Breadcrumb from '~/components/dashboard/breadcrumb'
import ListEvents from '~/components/dashboard/list/events'
import axios from '~/plugins/axios'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Breadcrumb,
    ListEvents
  },
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
    const current = await axios.get('/organizations/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_projects: quotas.data['results'][0], max_vpcs: quotas.data['results'][1]}
    const breadcrumbs = [{name: 'home', url: '/dashboard/'}, {name: slug, url: '/dashboard/organizations/' + slug}]
    return {slug: slug, quotas: quotas, projects: projects.data, vpcs: vpcs.data, current: current.data, breadcrumbs: breadcrumbs}
  }
}
</script>
