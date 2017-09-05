<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container">
                        <div class="modal-header text-center">
                            <h5 class="modal-title"><i class="fa fa-home"></i>&nbsp;Create your organization</h5>
                        </div>
                        <div class="modal-body">
                            <div class="form-group row" v-bind:class="{ 'has-danger': error }">
                                <template v-if="error">
                                    <label for="error" class="sr-only">Error</label>
                                    <div class="col">
                                        <div class="text-center text-danger">{{ error }}</div>
                                    </div>
                                </template>
                            </div>
                            <div class="form-group row">
                                <label for="name" class="sr-only">Name</label>
                                <div class="input-group col">
                                    <div class="input-group-addon"><i class="fa fa-home"></i></div>
                                    <input type="text" v-model="name" placeholder="Name" required="required" value="" class="form-control" />
                                </div>
                            </div>
                            <div class="form-group row">
                                <label for="description" class="sr-only">Description</label>
                                <div class="input-group col">
                                    <div class="input-group-addon"><i class="fa fa-pencil"></i></div>
                                    <input type="text" v-model="description" placeholder="Description" value="" class="form-control" />
                                </div>
                            </div>
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="create_organization">Save</button>
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
  data () {
    return {
      description: '',
      error: '',
      name: ''
    }
  },
  props: ['show'],
  methods: {
    close () {
      this.$emit('close')
      this.description = ''
      this.error = ''
      this.name = ''
    },
    async create_organization () {
      const vm = this
      const token = vm.$store.state.auth_token
      if (vm.name.length > 0) {
        try {
          const payload = await axios.post('/organizations/', {
            name: vm.name,
            description: vm.description
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
        this.create_organization()
      }
    })
  }
}
</script>
