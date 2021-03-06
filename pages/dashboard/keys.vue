<template>
    <div>
        <div style="min-height:500px;">
            <div class="container">
                <div class="row">
                    <create-key @success="key_created" :show.sync="showCreateKey" @close="showCreateKey = false" />
                    <delete-key :show="showDeleteKey" @delete-key="deleteKey" @close="showDeleteKey = false" :name="deleteKeyName" />
                    <div class="col-md-4">
                        <breadcrumb :items="breadcrumbs" />
                    </div>
                    <div class="col-md-1"></div>
                    <div class="col-md-3">
                        <span class="h3 light-h3">SSH Keys &nbsp;</span>
                        <span class="text-primary"> {{ keys.count | int }}</span>
                        <span class="text-muted text-weight-light">/ {{ quotas.max_keys.value | int }}</span>
                    </div>
                    <div class="col-md-2"></div>
                    <div class="col-md-2">
                        <button class="btn btn-block btn-outline-danger" role="button" v-on:click="showCreateKey = true">
                            Import key
                        </button>
                    </div>
                </div>
            </div>
            <br />
            <div class="container">
                <div class="row">
                    <div class="col-md-2"></div>
                    <div class="col-md-8">
                        <list-keys :objects="keys" @show-delete-key="showDeleteKeyPopup" />
                        <pagination @page-change="listKeys" :limit.sync="limit" :offset.sync="offset" :total.sync="keys.count" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import Breadcrumb from '~/components/dashboard/breadcrumb'
import CreateKey from '~/components/dashboard/create/key'
import DeleteKey from '~/components/dashboard/delete/key'
import ListKeys from '~/components/dashboard/list/keys'
import Pagination from '~/components/dashboard/pagination'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    Breadcrumb,
    CreateKey,
    DeleteKey,
    ListKeys,
    Pagination
  },
  async asyncData ({ store, error }) {
    const token = store.state.auth_token
    let quotas = await axios.get('/quotas/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    const keys = await axios.get('/keys/', {
      headers: {'Authorization': 'JWT ' + token}
    })
    quotas = {max_keys: quotas.data['results'][0]}
    return { quotas: quotas, keys: keys.data, breadcrumbs: [{name: 'home', url: '/dashboard/'}, {name: 'keys', url: '/dashboard/keys'}] }
  },
  data: function () {
    return {
      deleteKeyName: '',
      offset: 0,
      limit: 10,
      showCreateKey: false,
      showDeleteKey: false
    }
  },
  methods: {
    key_created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Key ', ' imported.')
      this.keys.count += 1
      this.keys.results.unshift(payload.data)
    },
    showDeleteKeyPopup: function (payload) {
      this.deleteKeyName = payload
      this.showDeleteKey = true
    },
    async listKeys (offset, limit) {
      const vm = this
      const token = vm.$store.state.auth_token
      try {
        const keys = await axios.get('/keys/', {
          params: {
            limit: limit,
            offset: offset
          },
          headers: {'Authorization': 'JWT ' + token}
        })
        vm.total = keys.data.count
        vm.keys = keys.data
        vm.limit = limit
        vm.offset = offset
      } catch (exc) {
        console.log(exc)
      }
    },
    async deleteKey (key) {
      const vm = this
      const token = vm.$store.state.auth_token
      vm.showDeleteKey = false
      try {
        await axios.delete('/keys/' + key + '/', {
          headers: {'Authorization': 'JWT ' + token}
        })
        this.$parent.$parent.error(key, 'Key ', ' deleted.')
        for (let result of vm.keys.results) {
          if (result.name === key) {
            const index = vm.keys.results.indexOf(result)
            vm.keys.results.splice(index, 1)
            break
          }
        }
        vm.keys.count -= 1
      } catch (exc) {
        const data = exc.response.data
        vm.$parent.$parent.error(key, 'Key ', ' : ' + data.detail)
      }
    }
  }
}
</script>
