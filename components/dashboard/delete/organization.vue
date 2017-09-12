<template>
    <div v-show="show">
        <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">
                    <div class="modal-container" style="width: 650px;">
                        <div class="modal-header text-center">
                            <h5 class="modal-title"><i class="fa fa-remove text-danger"></i> Are you sure you want to delete the organization <b>{{ name }}</b> ?</h5>
                        </div>
                        <div class="modal-body text-center">
                            <p>This operation cannot be <b class="text-uppercase">undone</b>.</p>
                            All the projects will be destroyed.
                            <br />
                            All the vpcs will be destroyed.
                            <br />
                            All the running apps will be destroyed.
                        </div>
                        <div class="modal-footer">
                            <button class="btn btn-primary" @click="$emit('delete-organization', name)">Yes</button>
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
