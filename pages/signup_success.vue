<template>
    <div class="container headtitle">
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h1>Account created</h1>
            </div>
        </div>
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h6>Enjoy baguette</h6>
            </div>
        </div>
            
        <div class="row justify-content-md-center  mt-4">
            <div class="text-center">
                <b>{{ username }}</b> we have generated for you a private key
            </div>
        </div>
        <div class="row justify-content-md-center  mt-4">
            <div class="text-center">
                <a href="" class="btn btn-block btn-fr-blue" id="download">Please, save it.</a>
            </div>
        </div>
        <div class="row justify-content-md-center">
            <div class="text-center">
                <span class="text-muted bt-link" style="font-size: 80%;">We don't store it in our database</span>
            </div>
        </div>
        <div class="row justify-content-md-center  mt-4">
            <div class="text-center">
                <nuxt-link class="btn btn-block btn-fr-red" role="button" to="/login">Now, you can log in</nuxt-link>
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
