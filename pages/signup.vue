<template>
    <div class="container" style="min-height: 500px;">
        <div class="row">
            <div class="col-md-5"></div>
            <div class="col-md-4">
                <h2 class="title">Sign up</h2>
            </div>
        </div>
        <form class="form-horizontal" method="post" v-on:submit.prevent="signup" action="">
            <div class="form-group row" v-bind:class="{ 'has-danger': usernameError }">
                <div class="col-md-4"></div>
                <label for="username" class="sr-only">Username</label>
                <div class="input-group col-md-4">
                    <div class="input-group-addon"><i class="fa fa-user fa-fw"></i></div>
                    <input type="text" name="username" v-model="username" class="form-control" placeholder="Username" required="" />
                </div>
                <div class="col-md-4">
                    <div class="form-control-feedback">
                        <template v-if="usernameError">
                            <span class="text-danger align-middle">
                                <i class="fa fa-close">{{ usernameError }}</i>
                            </span>
                        </template>
                    </div>
                </div>
            </div>
            <div class="form-group row" v-bind:class="{ 'has-danger': emailError }">
                <div class="col-md-4"></div>
                <label for="email" class="sr-only">Email</label>
                <div class="input-group col-md-4">
                    <div class="input-group-addon"><i class="fa fa-at fa-fw"></i></div>
                    <input type="text" name="email" v-model="email" class="form-control" placeholder="you@domain.com" required="" />
                </div>
                <div class="col-md-4">
                    <div class="form-control-feedback">
                        <template v-if="emailError">
                            <span class="text-danger align-middle">
                                <i class="fa fa-close">{{ emailError }}</i>
                            </span>
                        </template>
                    </div>
                </div>
            </div>
            <div class="form-group row" v-bind:class="{ 'has-danger': passwordError }">
                <div class="col-md-4"></div>
                <label for="password" class="sr-only">Password</label>
                <div class="input-group col-md-4">
                    <div class="input-group-addon"><i class="fa fa-key fa-fw"></i></div>
                    <input type="password" name="password" v-model="password" class="form-control" placeholder="P@ssw0rd!" required="" />
                </div>
                <div class="col-md-4">
                    <div class="form-control-feedback">
                        <template v-if="passwordError">
                            <span class="text-danger align-middle">
                                <i class="fa fa-close">{{ passwordError }}</i>
                            </span>
                        </template>
                    </div>
                </div>
            </div>
            <div class="row"> 
                <div class="col-md-4"></div>
                <div class="col-md-4">
                    <input type="submit" class="btn btn-block btn-outline-danger" value="Create account" />
                </div>
            </div>
        </form>
    </div>
</template>

<script>
import axios from '~/plugins/axios'

export default {
  layout: 'identification',
  data () {
    return {
      username: '',
      email: '',
      password: '',
      usernameError: false,
      emailError: false,
      passwordError: false
    }
  },
  methods: {
    async signup () {
      const vm = this
      vm.usernameError = false
      vm.emailError = false
      vm.passwordError = false
      try {
        const payload = await axios.post('/accounts/register/', {
          username: vm.username,
          email: vm.email,
          password: vm.password,
          confirm_password: vm.password
        })
        let key = payload.data.key.private
        let username = payload.data.account.username
        vm.$store.commit('save_key', key)
        vm.$store.commit('save_username', username)
        vm.$router.replace('/signup_success')
      } catch (error) {
        const data = error.response.data
        Object.keys(data).forEach(function (key) {
          if (key === 'username') {
            vm.usernameError = data[key][0]
          } else if (key === 'email') {
            vm.emailError = data[key][0]
          } else if (key === 'password') {
            vm.passwordError = data[key][0]
          }
        })
      }
    }
  }
}
</script>

