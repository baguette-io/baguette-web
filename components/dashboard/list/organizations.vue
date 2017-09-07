<template>
    <div class="container">
        <div class="row" v-for="orga in orgas.results">
            {{ orga.name }}
        </div>
    </div>
</template>

<script>
export default {
  props: ['orgas']
}
</script>
