<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="obj in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ obj.organization.name }}</h5>
                <small class="text-muted">Received on {{ obj.date_created | format_date }}</small>
            </div>
            <div class="d-flex justify-content-between">
                <div class="p-1">
                    <span class="text-muted">members:&nbsp;</span>
                    <span>{{ obj.organization.stats.members }}</span>
                </div>
                <div class="p-1">
                    <div class="btn-group" role="group">
                        <button class="btn btn-primary" role="button" @click="$emit('accept', obj.organization.name)">
                            Accept
                        </button>
                        <button class="btn btn-danger" role="button" @click="$emit('reject', obj.organization.name)">
                            Reject
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['objects']
}
</script>
