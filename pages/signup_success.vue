<template>
    <div class="container">
        <div class="row">
            <div class="offset-md-5 col-md-4">
                <h2 class="title">Account created</h2>
            </div>
        </div>
        <div class="row">
            <div class="offset-md-5 col-md-4">
                <div class="row">
                    We have generated for you a private key:
                </div>
                <div class="row">
                    <a v-bind:href="url" class="col-md-10 btn btn-block btn-secondary text-danger" id="download">Please, save it.</a>
                </div>
                <p><small><u>We don't store the private key in our databases.</u></small></p>
            </div>
        </div>
    </div>
</template>

<script>
function downloadFile (vm) {
  const blob = new Blob([vm.$store.state.private_key], {type: 'text/plain'})
  let a = document.getElementById('download')
  a.download = 'default_baguette.rsa'
  a.href = window.URL.createObjectURL(blob)
  a.dataset.downloadurl = ['text/plain', a.download, a.href].join(':')
  vm.$store.state.private_key = null
}

export default {
  layout: 'identification',
  data () {
    return {
      url: ''
    }
  },
  mounted () {
    console.log('mounted')
    const vm = this
    downloadFile(vm)
  }
}
</script>

