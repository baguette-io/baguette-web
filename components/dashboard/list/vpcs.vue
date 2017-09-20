<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="obj in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ obj.name }}</h5>
                <small class="text-muted">Added on {{ obj.date_created | format_date }}</small>
            </div>
            <div class="d-flex justify-content-between">
                <div class="p-1">
                    <span class="text-muted">deletable:&nbsp;</span>
                    <span>{{ obj.deletable }}</span>
                </div>
                <div class="p-1" v-if="admin">
                    <button class="btn btn-block btn-danger" :disabled="!obj.deletable" role="button" @click="$emit('show-delete', obj.name)">
                        Delete
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
