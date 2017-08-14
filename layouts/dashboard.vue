<template>
  <div>
    <dashboard-navbar />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import DashboardNavbar from '../components/dashboardnavbar'
import DefaultFooter from '../components/defaultfooter'
export default {
  layout: 'default',
  components: {
    DashboardNavbar,
    DefaultFooter
  }
}
</script>
