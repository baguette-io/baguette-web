<template>
    <div style="min-height:500px;">
        <hr />
        <div class="container">
            <div class="row">
                <create-organization @success="created" :show.sync="showCreate" @close="showCreate = false" />
                <delete-organization :show="showDelete" @delete-organization="remove" @close="showDelete = false" :name="deleteName" />
                <leave-organization :show="showLeave" @leave-organization="leave" @close="showLeave = false" :name="leaveName" />
                <div class="col-md-3">
                    <select-organizations :current="''" :path="''" />
                </div>
                <div class="col-md-2"></div>
                <div class="col-md-3">
                    <span class="h3 light-h3">Organizations &nbsp;</span>
                    <span class="text-primary"> {{ orgas.count | int }}</span>
                    <span class="text-muted text-weight-light">/ {{ quotas.max_orgas.value | int }}</span>
                </div>
                <div class="col-md-2"></div>
                <div class="col-md-2">
                    <button class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreate = true">
                        Create organization
                    </button>
                </div>
            </div>
        </div>
        <br />
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list-organizations :objects="orgas" @show-delete-organization="showPopup" @show-leave-organization="leavePopup" />
                    <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="orgas.count" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import CreateOrganization from '~/components/dashboard/create/organization'
import DeleteOrganization from '~/components/dashboard/delete/organization'
import LeaveOrganization from '~/components/dashboard/leave'
import ListOrganizations from '~/components/dashboard/list/organizations'
import Pagination from '~/components/dashboard/pagination'
import SelectOrganizations from '~/components/dashboard/select/organizations'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    CreateOrganization,
    DeleteOrganization,
    LeaveOrganization,
    ListOrganizations,
    Pagination,
    SelectOrganizations
  },
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const orgas = await axios.get('/members/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_orgas: quotas.data['results'][1]}
    return { quotas: quotas, orgas: orgas.data }
  },
  data: function () {
    return {
      deleteName: '',
      leaveName: '',
      offset: 0,
      limit: 10,
      showCreate: false,
      showDelete: false,
      showLeave: false
    }
  },
  methods: {
    created: function (payload) {
      this.$parent.$parent.success(payload.data.name, 'Organization ', ' created.')
      this.orgas.count += 1
      const result = {is_owner: true, is_admin: true, organization: payload.data, stats: {members: 1, invitations: 0}}
      this.orgas.results.unshift(result)
    },
    showPopup: function (payload) {
      this.deleteName = payload
      this.showDelete = true
    },
    leavePopup: function (payload) {
      this.leaveName = payload
      this.showLeave = true
    },
    async list (offset, limit) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        const organizations = await axios.get('/members/', {
          params: {
            limit: limit,
            offset: offset
          },
          headers: {'Authorization': 'JWT ' + token}
        })
        vm.total = organizations.data.count
        vm.orgas = organizations.data
        vm.limit = limit
        vm.offset = offset
      } catch (exc) {
        console.log(exc)
      }
    },
    async remove (organization) {
      const vm = this
      const token = vm.$store.state.auth_token
      vm.showDelete = false
      try {
        await axios.delete('/organizations/' + organization + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(organization, 'Organization ', ' deleted.')
        for (let result of vm.orgas.results) {
          if (result.organization.name === organization) {
            const index = vm.orgas.results.indexOf(result)
            vm.orgas.results.splice(index, 1)
            break
          }
        }
        vm.orgas.count -= 1
      } catch (exc) {
        console.log(exc.response)
        let detail = 'not found.'
        if (exc.response.status === 403) {
          detail = 'undeletable.'
        }
        vm.$parent.$parent.error(organization, 'Organization ', ' : ' + detail)
      }
    },
    async leave (organization) {
      const vm = this
      const token = vm.$store.state.auth_token
      vm.showLeave = false
      try {
        await axios.delete('/members/' + organization + '/' + vm.$store.state.username + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(organization, 'Organization ', ' leaved.')
        for (let result of vm.orgas.results) {
          if (result.organization.name === organization) {
            const index = vm.orgas.results.indexOf(result)
            vm.orgas.results.splice(index, 1)
            break
          }
        }
        vm.orgas.count -= 1
      } catch (exc) {
        console.log(exc.response)
        let detail = 'not found.'
        if (exc.response.status === 403) {
          detail = 'unleavable.'
        }
        vm.$parent.$parent.error(organization, 'Organization ', ' : ' + detail)
      }
    }
  }
}
</script>
