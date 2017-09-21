<template>
    <div style="min-height:500px;">
        <div class="container">
            <div class="row">
                Logout...
            </div>
        </div>
    </div>
</template>

<script>
export default {
  mounted: function (redirect) {
    this.$store.commit('logout')
    this.$router.replace('/login')
  }
}
</script>
