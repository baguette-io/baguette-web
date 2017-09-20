<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <span class="h3 light-h3">Members</span>
                    <div class="row">
                        <div class="col">
                            <span class="text-primary">{{ objects.count | int }}</span>
                        </div>
                    </div>
                </div>
            </div>
            <hr />
        </div>
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list :objects="objects" @promote="promote" @demote="demote" @remove="remove" :account="account" :admin="permissions.is_admin" :owner="permissions.is_owner" />
                    <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="objects.count" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import List from '~/components/dashboard/list/members'
import Pagination from '~/components/dashboard/pagination'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    List,
    Pagination
  },
  async asyncData ({ params, store, error }) {
    const token = store.state.auth_token
    const slug = params.slug
    const username = store.state.username
    const objects = await axios.get('/members/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    let permissions = await axios.get('/members/', {
      params: {
        account: username,
        organization: slug
      },
      headers: {'Authorization': 'JWT ' + token}
    })
    permissions = permissions.data['results'][0]
    return { account: username, objects: objects.data, slug: slug, permissions: permissions }
  },
  data: function () {
    return {
      offset: 0,
      limit: 10,
      showCreate: false
    }
  },
  methods: {
    async list (offset, limit) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        const objects = await axios.get('/invitations/' + vm.slug + '/', {
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
    async promote (username) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        await axios.patch('/members/' + vm.slug + '/', {
          account: username,
          is_admin: true
        }, {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(username, 'Member ', ' promoted.')
        for (let result of vm.objects.results) {
          if (result.account === username) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results[index].is_admin = true
            break
          }
        }
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(username, 'Promotion of ', ' : ' + data.detail)
      }
    },
    async demote (username) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        await axios.patch('/members/' + vm.slug + '/', {
          account: username,
          is_admin: false
        }, {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(username, 'Member ', ' demoted.')
        for (let result of vm.objects.results) {
          if (result.account === username) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results[index].is_admin = false
            break
          }
        }
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(username, 'Demotion of ', ' : ' + data.detail)
      }
    },
    async remove (username) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        await axios.delete('/members/' + vm.slug + '/' + username + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(username, 'Member ', ' removed.')
        for (let result of vm.objects.results) {
          if (result.account === username) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results.splice(index, 1)
            break
          }
        }
        vm.objects.count -= 1
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(username, 'Removal of ', ' : ' + data.detail)
      }
    }
  }
}
</script>
