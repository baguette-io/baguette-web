<template>
  <div class="dashboard">
    <dashboard-navbar />
    <hr />
    <dashboard-notif :prefix.sync="notifPrefix" :suffix.sync="notifSuffix" :isSuccess.sync="isSuccess" :isError.sync="isError" :obj.sync="notifObj" />
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
import DashboardNavbar from '~/components/dashboard/navbar'
import DashboardNotif from '~/components/dashboard/notif'
import DefaultFooter from '~/components/footer'
export default {
  layout: 'dashboard',
  data: function () {
    return {
      isSuccess: false,
      isError: false,
      notifObj: '',
      notifPrefix: '',
      notifSuffix: ''
    }
  },
  components: {
    DashboardNavbar,
    DashboardNotif,
    DefaultFooter
  },
  methods: {
    success: function (obj, prefix, suffix) {
      this.notifObj = obj
      this.notifPrefix = prefix
      this.notifSuffix = suffix
      this.isError = false
      this.isSuccess = true
    },
    error: function (payload) {
      this.isError = true
      this.isSuccess = false
    }
  }
}
</script>
