<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="key in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ key.name }}</h5>
                <small class="text-muted">Added on {{ key.date_created | format_date }}</small>
            </div>
            <div class="d-flex justify-content-between">
                <div class="p-1">
                    <span class="text-muted">Fingerprint:&nbsp;</span>
                    <span>{{ key.fingerprint }}</span>
                </div>
                <div class="p-1">
                    <button class="btn btn-block btn-danger" role="button">
                        Delete
                    </button>
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
