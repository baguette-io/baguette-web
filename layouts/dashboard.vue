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
