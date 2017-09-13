<template>
    <div class="list-group">
        <nuxt-link v-bind:to="'/dashboard/organizations/' + obj.organization.name + '/'" :key="obj.organization.name" class="list-group-item list-group-item-action flex-column align-items-start" v-for="obj in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ obj.organization.name }}&nbsp;<small class="text-muted">{{ obj.organization.description }}</small></h5>
                <small class="text-muted">Added on {{ obj.organization.date_created | format_date }}</small>
            </div>
            <div class="row">
                <div class="col-6">
                    <span class="text-muted">
                        <template v-if="obj.is_owner">owner</template>
                        <template v-else-if="obj.is_admin">admin</template>
                        <template v-else="obj.is_admin">member</template>
                    </span>
                </div>
                <div class="col-4">
                    <div class="row">
                        <div class="col-xs-12">
                            <i class="fa fa-user-o"></i>&nbsp;<span class="text-muted">{{ obj.organization.stats.members }}</span>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-xs-12">
                            <i class="fa fa-envelope-o"></i>&nbsp;<span class="text-muted">{{ obj.organization.stats.invitations }}</span>
                        </div>
                    </div>
                </div>
                <div class="col-2">
                    <button class="btn btn-block btn-danger" role="button" v-if="obj.is_owner" :disabled="!obj.organization.deletable" @click.prevent="$emit('show-delete-organization', obj.organization.name)">
                        Delete
                    </button>
                </div>
            </div>
        </nuxt-link>
    </div>
</template>

<script>
export default {
  props: ['objects']
}
</script>
