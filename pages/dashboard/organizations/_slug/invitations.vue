<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <span class="h3 light-h3">Invitations</span>
                    <div class="row">
                        <div class="col">
                            <span class="text-primary">{{ objects.count | int }}</span>
                        </div>
                    </div>
                </div>
                <div class="col-md-7"></div>
                <create @success="created" :orga="slug" :show.sync="showCreate" @close="showCreate = false" />
                <div class="col-md-2">
                    <button class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreate = true">
                        Invite
                    </button>
                </div>
            </div>
            <hr />
        </div>
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list :objects="objects" @reject="reject" />
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

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Create,
    List,
    Pagination
  },
  async asyncData ({ params, store, error }) {
    const token = store.state.auth_token
    const slug = params.slug
    const objects = await axios.get('/invitations/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    return { objects: objects.data, slug: slug }
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
