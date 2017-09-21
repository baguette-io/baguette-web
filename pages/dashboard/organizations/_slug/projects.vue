
<template>
    <div>
        <div style="min-height:500px;">
            <div class="container">
                <div class="row">
                    <create @success="created" :orga="slug" :show.sync="showCreate" @close="showCreate = false" />
                    <delete :show="showDelete" @delete="remove" @close="showDelete = false" :name="deleteName" />
                    <div class="col-md-4">
                        <breadcrumb :items="breadcrumbs" />
                    </div>
                    <div class="col-md-1"></div>
                    <div class="col-md-3">
                        <span class="h3 light-h3">Projects &nbsp;</span>
                        <span class="text-primary"> {{ objects.count | int }}</span>
                        <span class="text-muted text-weight-light">/ {{ quotas.max.value | int }}</span>
                    </div>
                    <div class="col-md-2"></div>
                    <div class="col-md-2">
                        <button v-if="permissions.is_admin" class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreate = true">
                            Create a project
                        </button>
                    </div>
                </div>
            </div>
            <br />
            <div class="container">
                <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-8">
                        <list :objects="objects" @show-delete="showDeletePopup" :admin="permissions.is_admin" />
                        <pagination @page-change="list" :limit.sync="limit" :offset.sync="offset" :total.sync="objects.count" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import Breadcrumb from '~/components/dashboard/breadcrumb'
import Create from '~/components/dashboard/create/project'
import Delete from '~/components/dashboard/delete/project'
import List from '~/components/dashboard/list/projects'
import Pagination from '~/components/dashboard/pagination'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Breadcrumb,
    Create,
    Delete,
    List,
    Pagination
  },
  async asyncData ({ params, store, error }) {
    const token = store.state.auth_token
    const slug = params.slug
    const username = store.state.username
    let quotas = await axios.get('/quotas/', {
      params: {'organization': slug},
      headers: {'Authorization': 'JWT ' + token}
    })
    const objects = await axios.get('/projects/' + slug + '/', {
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
    quotas = {max: quotas.data['results'][0]}
    const breadcrumbs = [{name: 'home', url: '/dashboard/'}, {name: slug, url: '/dashboard/organizations/' + slug}, {name: 'projects', url: '/dashboard/organizations/' + slug + '/projects'}]
    return { quotas: quotas, objects: objects.data, permissions: permissions, slug: slug, breadcrumbs: breadcrumbs }
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
      this.$parent.$parent.success(obj, 'Project ', ' created.')
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
        const objects = await axios.get('/projects/' + vm.slug + '/', {
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
        await axios.delete('/projects/' + vm.slug + '/' + obj + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.success(obj, 'Project ', ' deleted.')
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
        vm.$parent.$parent.error(obj, 'Project ', ' : ' + data.detail)
      }
    }
  }
}
</script>
