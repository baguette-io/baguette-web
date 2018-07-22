<template>
    <div class="container headtitle">
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h1>Logging out</h1>
            </div>
        </div>
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h6>Au revoir</h6>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  mounted: function (redirect) {
    this.$store.commit('logout')
    this.$router.replace('/')
  }
}
</script>
