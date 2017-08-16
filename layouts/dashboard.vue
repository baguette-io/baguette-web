<template>
  <div class="dashboard">
    <dashboard-navbar />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import DashboardNavbar from '../components/dashboard/navbar'
import DefaultFooter from '../components/footer'
export default {
  layout: 'default',
  components: {
    DashboardNavbar,
    DefaultFooter
  }
}
</script>
