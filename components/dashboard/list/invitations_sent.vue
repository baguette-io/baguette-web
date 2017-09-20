<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="obj in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ obj.account }}</h5>
                <small class="text-muted">Sent on {{ obj.date_created | format_date }}</small>
            </div>
            <div class="d-flex justify-content-between">
                <div class="p-1">
                </div>
                <div class="p-1" v-if="admin">
                    <button class="btn btn-block btn-danger" role="button" @click="$emit('reject', obj.account)">
                        Cancel
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['admin', 'objects']
}
</script>
