<template>
    <div class="container">
        <div class="row">
            <div class="col-md-5"></div>
            <div class="col-md-4">
                <h2 class="title">Account created</h2>
            </div>
        </div>
        <div class="row">
            <div class="col-md-5"></div>
            <div class="col-md-4">
                <div class="text-center">
                    <b>{{ username }}</b>, we have generated for you a private key:
                </div>
                <div class="row">
                    <a href="" class="btn btn-block btn-secondary" id="download">Please, save it.</a>
                </div>
                <div class="text-center">
                    <p><small><u>We don't store the private key in our databases.</u></small></p>
                </div>
                <div class="row">
                    <nuxt-link class="btn btn-block btn-danger" role="button" to="/login">Now, you can Log in</nuxt-link>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
function downloadFile (vm) {
  const blob = new Blob([vm.$store.state.private_key], {type: 'text/plain'})
  let a = document.getElementById('download')
  a.download = vm.username + '_default_baguette.rsa'
  a.href = window.URL.createObjectURL(blob)
  a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':')
}

export default {
  layout: 'identification',
  data () {
    return {
      username: ''
    }
  },
  mounted () {
    const vm = this
    if (vm.$store.state.username === null) {
      vm.$router.replace('/signup')
    }
    vm.username = vm.$store.state.username
    downloadFile(vm)
    vm.$store.commit('reset')
  }
}
</script>
