<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container">
                        <div class="modal-body">
                            Are you sure you want to delete {{ key }} ?
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="delete_key">Yes</button>
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
  props: ['key', 'show'],
  methods: {
    close () {
      this.$emit('close')
      this.error = ''
    }
  }
}
</script>
