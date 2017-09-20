<template>
    <div style="min-height:500px;">
        <hr />
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <select-organizations :current="slug" :path="'invitations'" />
                </div>
                <div class="col-md-2"></div>
                <div class="col-md-3">
                    <span class="h3 light-h3">Invitations &nbsp;</span>
                    <span class="text-primary"> {{ objects.count | int }}</span>
                </div>
                <div class="col-md-2"></div>
                <create @success="created" :orga="slug" :show.sync="showCreate" @close="showCreate = false" />
                <div class="col-md-2">
                    <button v-if="permissions.is_admin" class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreate = true">
                        Invite
                    </button>
                </div>
            </div>
        </div>
        <br />
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list :objects="objects" @reject="reject" :admin="permissions.is_admin" />
                    <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="objects.count" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import Create from '~/components/dashboard/create/invitation'
import List from '~/components/dashboard/list/invitations_sent'
import Pagination from '~/components/dashboard/pagination'
import SelectOrganizations from '~/components/dashboard/select/organizations'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Create,
    List,
    Pagination,
    SelectOrganizations
  },
  async asyncData ({ params, store, error }) {
    const token = store.state.auth_token
    const slug = params.slug
    const username = store.state.username
    const objects = await axios.get('/invitations/' + slug + '/', {
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
    return { objects: objects.data, slug: slug, permissions: permissions }
  },
  data: function () {
    return {
      offset: 0,
      limit: 10,
      showCreate: false
    }
  },
  methods: {
    created: function (payload) {
      const obj = payload.data.account
      this.$parent.$parent.success(obj, 'Invitation to ', ' sent.')
      this.objects.count += 1
      this.objects.results.unshift(payload.data)
    },
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
    async reject (obj) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        await axios.delete('/invitations/' + vm.slug + '/' + obj + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(obj, 'Invitation to ', ' cancelled.')
        for (let result of vm.objects.results) {
          if (result.account === obj) {
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
