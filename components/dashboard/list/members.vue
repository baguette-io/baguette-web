<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="obj in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ obj.account }}</h5>
                <small class="text-muted">Joined on {{ obj.date_created | format_date }}</small>
            </div>
            <div class="d-flex justify-content-between">
                <div class="p-1">
                    <span class="text-muted">
                        <template v-if="obj.is_owner">
                          owner
                        </template>
                        <template v-else-if="obj.is_admin">
                          admin
                        </template>
                        <template v-else>
                          member
                        </template>
                        <template v-if="obj.account === account">
                          (you)
                        </template>
                    </span>
                </div>
                <div class="p-1" v-if="admin">
                    <div class="btn-group" role="group">
                        <button class="btn btn-primary" role="button" @click="$emit('promote', obj.account)" v-if="!obj.is_admin">
                            Promote
                        </button>
                        <button class="btn btn-secondary" role="button" @click="$emit('demote', obj.account)" v-if="obj.is_admin && obj.account!=account">
                            Demote
                        </button>
                        <button class="btn btn-danger" role="button" @click="$emit('remove', obj.account)" v-if="!obj.is_owner && obj.account!=account">
                            Remove
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  props: ['account', 'admin', 'objects', 'owner']
}
</script>
