<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <create @success="created" :orga="slug" :show.sync="showCreate" @close="showCreate = false" />
                <delete :show="showDelete" @delete="remove" @close="showDelete = false" :name="deleteName" />
                <div class="col-md-3">
                    <span class="h3 light-h3">VPCs</span>
                    <div class="row">
                        <div class="col">
                            <span class="text-primary">{{ objects.count | int }}</span>
                            <span class="text-muted text-weight-light">/ {{ quotas.max.value | int }}</span>
                        </div>
                    </div>
                </div>
                <div class="col-md-7"></div>
                <div class="col-md-2">
                    <button class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreate = true">
                        Create VPC
                    </button>
                </div>
            </div>
            <hr />
        </div>
        <div class="container">
            <div class="row">
                <div class="col-md-2"></div>
                <div class="col-md-8">
                    <list :objects="objects" @show-delete="showDeletePopup" />
                    <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="objects.count" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import Create from '~/components/dashboard/create/vpc'
import Delete from '~/components/dashboard/delete/vpc'
import List from '~/components/dashboard/list/vpcs'
import Pagination from '~/components/dashboard/pagination'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Create,
    Delete,
    List,
    Pagination
  },
  async asyncData ({ params, store, error }) {
    const token = store.state.auth_token
    const slug = params.slug
    let quotas = await axios.get('/quotas/', {
      params: {'organization': slug},
      headers: {'Authorization': 'JWT ' + token}
    })
    const objects = await axios.get('/vpcs/' + slug + '/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max: quotas.data['results'][0]}
    return { quotas: quotas, objects: objects.data, slug: slug }
  },
  data: function () {
    return {
      deleteName: '',
      offset: 0,
      limit: 10,
      showCreate: false,
      showDelete: false
    }
  },
  methods: {
    created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Vpc ', ' created.')
      this.objects.count += 1
      this.objects.results.unshift(payload.data)
    },
    showDeletePopup: function (payload) {
      this.deleteName = payload
      this.showDelete = true
    },
    async list (offset, limit) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        const objects = await axios.get('/vpcs/' + vm.slug + '/', {
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
    async remove (obj) {
      const vm = this
      const token = vm.$store.state.auth_token
      vm.showDelete = false
      try {
        await axios.delete('/vpcs/' + vm.slug + '/' + obj + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(obj, 'Vpc ', ' deleted.')
        for (let result of vm.objects.results) {
          if (result.name === obj) {
            const index = vm.objects.results.indexOf(result)
            vm.objects.results.splice(index, 1)
            break
          }
        }
        vm.objects.count -= 1
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(obj, 'Vpc ', ' : ' + data.detail)
      }
    }
  }
}
</script>
