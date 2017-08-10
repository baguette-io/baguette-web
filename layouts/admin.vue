<template>
  <div>
    <admin-navbar />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import AdminNavbar from '../components/adminnavbar'
import DefaultFooter from '../components/defaultfooter'
export default {
  layout: 'default',
  components: {
    AdminNavbar,
    DefaultFooter
  }
}
</script>
