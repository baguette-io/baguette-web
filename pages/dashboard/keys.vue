<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                <create-key @success="key_created" :show="showCreateKey" @close="showCreateKey = false" />
                <div class="col-md-3">
                    <span class="h3 light-h3">SSH Keys</span>
                    <div class="row">
                        <div class="col">
                            <span class="text-primary">{{ keys.count | int }}</span>
                            <span class="text-muted text-weight-light">/ {{ quotas.max_keys.value | int }}</span>
                        </div>
                    </div>
                </div>
                <div class="col-md-7"></div>
                <div class="col-md-2">
                    <button class="btn btn-block btn-danger" role="button" v-on:click="showCreateKey = true">
                        Import key
                    </button>
                </div>
            </div>
            <hr />
        </div>
        <div class="container">
            <div class="row">
               <div class="col-md-6">
                    <list-keys :objects="keys" />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
import CreateKey from '~/components/dashboard/create/key'
import ListKeys from '~/components/dashboard/list/keys'

export default {
  middleware: 'auth',
  layout: 'dashboard',
  components: {
    CreateKey,
    ListKeys
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
    return { quotas: quotas, keys: keys.data }
  },
  data: function () {
    return {
      showCreateKey: false
    }
  },
  methods: {
    key_created: function (payload) {
      const obj = payload.data.name
      this.$parent.$parent.success(obj, 'Key ', ' imported.')
      this.keys.count += 1
    }
  }
}
</script>
