<template>
    <div style="min-height:500px;">
        <hr />
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <select-organizations :current="''" :path="'invitations'" />
                </div>
                <div class="col-md-2"></div>
                <div class="col-md-3">
                    <span class="h3 light-h3">Invitations &nbsp;</span>
                    <span class="text-primary"> {{ objects.count | int }}</span>
                </div>
            </div>
        </div>
        <br />
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list :objects="objects" @accept="accept" @reject="reject" />
                    <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="objects.count" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import List from '~/components/dashboard/list/invitations'
import Pagination from '~/components/dashboard/pagination'
import SelectOrganizations from '~/components/dashboard/select/organizations'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    List,
    Pagination,
    SelectOrganizations
  },
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    const objects = await axios.get('/invitations/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    return { objects: objects.data }
  },
  data: function () {
    return {
      offset: 0,
      limit: 10
    }
  },
  methods: {
    async accept (obj) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        await axios.put('/invitations/' + obj + '/', {}, {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(obj, 'Invitation to ', ' accepted.')
        for (let result of vm.objects.results) {
          if (result.organization.name === obj) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results.splice(index, 1)
            break
          }
        }
        vm.objects.count -= 1
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(obj, 'Invitation to ', ' : ' + data.detail)
      }
    },
    async list (offset, limit) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        const objects = await axios.get('/invitations/', {
          params: {
            limit: limit,
            offset: offset
          },
          headers: {'Authorization': 'JWT ' + token}
        })
        vm.total = objects.data.count
        vm.objects = objects.data
        vm.limit = limit
        vm.offset = offset
      } catch (exc) {
        console.log(exc)
      }
    },
    async reject (obj) {
      const vm = this
      const token = vm.$store.state.auth_token
      const username = vm.$store.state.username
      try {
        await axios.delete('/invitations/' + obj + '/' + username + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(obj, 'Invitation to ', ' rejected.')
        for (let result of vm.objects.results) {
          if (result.organization.name === obj) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results.splice(index, 1)
            break
          }
        }
        vm.objects.count -= 1
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(obj, 'Invitation to ', ' : ' + data.detail)
      }
    }
  }
}
</script>
