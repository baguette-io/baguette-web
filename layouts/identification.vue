<template>
  <div>
    <default-navbar></default-navbar>
    <div class="container identification bg-primary-text">
        <div class="row justify-content-md-center">
            <nuxt />
        </div>
    </div>
    <default-footer />
  </div>
</template>

<script>
import DefaultFooter from '../components/defaultfooter'
import DefaultNavbar from '../components/defaultnavbar'
export default {
  layout: 'identification',
  components: {
    DefaultFooter,
    DefaultNavbar
  }
}
</script>
