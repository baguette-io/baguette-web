<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container">
                        <div class="modal-body">
                            Are you sure you want to delete {{ name }} ?
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary">Yes</button>
                            <button class="btn btn-secondary" @click="close">No</button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
export default {
  data () {
    return {
      error: ''
    }
  },
  props: ['name', 'show'],
  methods: {
    close () {
      this.$emit('close')
      this.error = ''
    }
  }
}
</script>
