<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container" style="width: 650px;">
                        <div class="modal-header text-center">
                            <h5 class="modal-title"><i class="fa fa-remove text-danger"></i> Are you sure you want to leave the organization <b>{{ name }}</b> ?</h5>
                        </div>
                        <div class="modal-body text-center">
                            <p>This operation cannot be <b class="text-uppercase">undone</b>.</p>
                            You won't have access anymore to the projects.
                            <br />
                            You won't be able to push on the organization repositories.
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="$emit('leave-organization', name)">Yes</button>
                            <button class="btn btn-secondary" @click="$emit('close')">No</button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
export default {
  props: ['name', 'show']
}
</script>
