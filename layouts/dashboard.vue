<template>
  <div class="dashboard">
	    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light">
          <div class="container">
                <a class="navbar-brand" href="/">
                    <img src="/images/baguette.png" width="40" height="40" alt="">
                </a>
                <ul class="navbar-nav">
                    <li class="">
                        <a class="nav-link text-dark" href="#">Get Started</a>
                    </li>
                    <li class="">
                        <a class="nav-link text-dark" href="#">Documentation</a>
                    </li>
                    <li class="">
                        <a class="btn btn-fr-red" href="/logout" role="button">Log out</a>
                    </li>
                </ul>
            </div>
            <div class="collapse navbar-collapse">
                <ul class="navbar-nav mx-auto">
                    <dashboard-notif :show.sync="show" :prefix.sync="notifPrefix" :suffix.sync="notifSuffix" :isSuccess.sync="isSuccess" :isError.sync="isError" :obj.sync="notifObj" @hide="hide" />
                </ul>
            </div>
        </nav>
    </div>
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
      show: false,
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
      const vm = this
      this.notifObj = obj
      this.notifPrefix = prefix
      this.notifSuffix = suffix
      this.isError = false
      this.isSuccess = true
      this.show = true
      setTimeout(function () {
        vm.show = false
      }, 3000)
    },
    error: function (obj, prefix, suffix) {
      const vm = this
      this.notifObj = obj
      this.notifPrefix = prefix
      this.notifSuffix = suffix
      this.isSuccess = false
      this.isError = true
      this.show = true
      setTimeout(function () {
        vm.show = false
      }, 3000)
    },
    hide: function () {
      this.show = false
    }
  }
}
</script>
