<template>
  <div>
    <default-navbar />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import DefaultFooter from '~/components/footer'
import DefaultNavbar from '~/components/navbar'
export default {
  layout: 'default',
  components: {
    DefaultFooter,
    DefaultNavbar
  }
}
</script>
