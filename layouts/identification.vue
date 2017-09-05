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
import DefaultFooter from '~/components/footer'
import DefaultNavbar from '~/components/navbar'
export default {
  layout: 'identification',
  components: {
    DefaultFooter,
    DefaultNavbar
  }
}
</script>
