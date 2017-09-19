<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container" style="width: 300px;">
                        <div class="modal-header text-center">
                            <h5 class="modal-title"><i class="fa fa-user-o"></i>&nbsp;Invite someone</h5>
                        </div>
                        <div class="modal-body">
                            <div class="form-row" v-bind:class="{ 'has-danger': error }">
                                <template v-if="error">
                                    <label for="error" class="sr-only">Error</label>
                                    <div class="col">
                                        <div class="text-center text-danger">{{ error }}</div>
                                    </div>
                                </template>
                            </div>
                            <div class="form-row">
                                <label for="username" class="sr-only">Username</label>
                                <div class="input-group col">
                                    <div class="input-group-addon"><i class="fa fa-user-o"></i></div>
                                    <input type="text" v-model="username" placeholder="Username" required="required" value="" class="form-control" />
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="create">Invite</button>
                            <button class="btn btn-secondary" @click="close">Close</button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import axios from '~/plugins/axios'
export default {
  props: ['orga', 'show'],
  data () {
    return {
      error: '',
      username: ''
    }
  },
  methods: {
    close () {
      this.$emit('close')
      this.error = ''
      this.username = ''
    },
    async create () {
      const vm = this
      const token = vm.$store.state.auth_token
      if (vm.username.length > 0) {
        try {
          const payload = await axios.post('/invitations/', {
            organization: vm.orga,
            account: vm.username
          }, {
            headers: {'Authorization': 'JWT ' + token}
          })
          vm.$emit('success', payload)
          this.close()
        } catch (exc) {
          if (exc.response.status === 409) {
            vm.error = 'Already a member'
          } else if (exc.response.status === 404) {
            vm.error = 'User not found'
          } else {
            console.log(exc.response)
            const data = exc.response.data
            Object.keys(data).forEach(function (key) {
              vm.error = data[key]
            })
          }
        }
      }
    }
  },
  mounted: function () {
    document.addEventListener('keydown', (e) => {
      if (this.show && e.keyCode === 13) {
        this.create()
      }
    })
  }
}
</script>
