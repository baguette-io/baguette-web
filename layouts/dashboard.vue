<template>
  <div class="dashboard">
    <nav class="navbar navbar-expand-lg navbar-light">
	    <div class="container">
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mx-auto">
                    <dashboard-notif :prefix.sync="notifPrefix" :suffix.sync="notifSuffix" :isSuccess.sync="isSuccess" :isError.sync="isError" :obj.sync="notifObj" />
                </ul>
                <ul class="navbar-nav navbar-right">
                    <li class="">
                        <a class="btn btn-danger" href="/logout" role="button">Log out</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    <nuxt/>
    <default-footer />
  </div>
</template>

<script>
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
    error: function (obj, prefix, suffix) {
      this.notifObj = obj
      this.notifPrefix = prefix
      this.notifSuffix = suffix
      this.isSuccess = false
      this.isError = true
    }
  }
}
</script>
