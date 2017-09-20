<template>
    <div class="dropdown shown">
        <button class="btn dropdown-toggle btn-outline-danger" href="#" role="button" id="dropdownOrganization" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
            <template v-if="current">
              {{ current }}
            </template>
            <template v-else>
              Choose an organization
            </template>
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownOrganization" style="padding-bottom: 0">
            <nuxt-link class="dropdown-item" v-if="orga.organization.name !=current" v-for="orga in orgas" :key="orga.name" v-bind:to="'/dashboard/organizations/' + orga.organization.name + '/' + path">
                {{ orga.organization.name }} 
            </nuxt-link>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  props: ['current', 'path'],
  data: function () {
    return {
      orgas: null
    }
  },
  mounted: async function () {
    const token = this.$store.state.auth_token
    const orgas = await axios.get('/members/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    this.orgas = orgas.data.results
  }
}
</script>
