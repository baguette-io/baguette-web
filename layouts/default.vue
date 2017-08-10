<template>
  <div>
    <default-navbar />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import DefaultFooter from '../components/defaultfooter'
import DefaultNavbar from '../components/defaultnavbar'
export default {
  layout: 'default',
  components: {
    DefaultFooter,
    DefaultNavbar
  }
}
</script>
