<template>
    <div class="list-group">
        <div class="list-group-item list-group-item-action flex-column align-items-start" v-for="key in objects.results">
            <div class="d-flex justify-content-between">
                <h5 class="mb-1">{{ key.name }}</h5>
                 <small class="text-muted">Added on {{ key.date_created | format_date }}</small>
            </div>
            <p class="mb-1">Fingerprint:{{ key.fingerprint }}</p>
        </div>
    </div>
</template>

<script>
export default {
  props: ['objects']
}
</script>
