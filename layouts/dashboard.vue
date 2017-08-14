<template>
  <div class="dashboard">
    <dashboard-navbar />
    <select class="custom-select">
        <option selected="">Choose an organization</option>
    </select>
    <h1>Dashboard</h1>
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
