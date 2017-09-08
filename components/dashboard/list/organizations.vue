<template>
    <div class="container">
        <div class="row" v-for="orga in objects.results">
            <div class="col-md-1">
                <img src="/images/orga.svg" class="rounded-circle avatar" alt="orga" />
            </div>
            <div class="col-md-1"></div>
            <div class="col">
                <div class="row font-weight-bold">
                    {{ orga.name }}
                </div>
                <div class="row font-italic">
                    {{ orga.description || "&nbsp;" }}
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
