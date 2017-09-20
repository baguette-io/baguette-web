<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container" style="width: 300px;">
                        <div class="modal-header text-center">
                            <h5 class="modal-title"><i class="fa fa-cube"></i>&nbsp;Create your project</h5>
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
                                <label for="name" class="sr-only">Name</label>
                                <div class="input-group col">
                                    <div class="input-group-addon"><i class="fa fa-cube"></i></div>
                                    <input type="text" v-model="name" placeholder="Name" required="required" value="" class="form-control" />
                                </div>
                            </div>
                            <br />
                            <div class="form-row">
                                <div class="col-auto">
                                    <label class="custom-control custom-checkbox">
                                        <input type="checkbox" class="custom-control-input" v-model="deletable" />
                                        <span class="custom-control-indicator"></span>
                                        <span class="custom-control-description">Deletable</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="create">Save</button>
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
      name: '',
      deletable: true
    }
  },
  methods: {
    close () {
      this.$emit('close')
      this.error = ''
      this.name = ''
      this.deletable = true
    },
    async create () {
      const vm = this
      const token = vm.$store.state.auth_token
      if (vm.name.length > 0) {
        try {
          const payload = await axios.post('/projects/' + vm.orga + '/', {
            name: vm.name,
            deletable: vm.deletable
          }, {
            headers: {'Authorization': 'JWT ' + token}
          })
          vm.$emit('success', payload)
          this.close()
        } catch (exc) {
          const data = exc.response.data
          Object.keys(data).forEach(function (key) {
            vm.error = data[key][0]
          })
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
