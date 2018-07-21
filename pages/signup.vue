<template>
        <div class="container headtitle">
            <div class="row justify-content-md-center">
                <div class="col-12 col-md-auto">
                    <h1>Sign up</h1>
                </div>
            </div>
            <div class="row justify-content-md-center">
                <div class="col-12 col-md-auto">
                    <h6>One step away to automation</h6>
	    		</div>
            </div>
            <div class="justify-content-md-center">
                <form class="container mt-4" novalidate method="post" v-on:submit.prevent="signup" action="">
                    <div class="row form-group">
                        <div class="col-md-4"></div>
                        <div class="col-md-4">
                            <label for="username" class="sr-only">Username</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text bg-fr-blue border-fr-blue text-white"><i class="fa fa-user fa-fw"></i></div>
                                </div>
                                <input type="text" name="username" v-model="username" class="form-control" placeholder="Username" required="" />
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="validation-error" v-bind:class="{ 'visible': usernameError }">
                                {{ usernameError }}
                            </div>
                        </div>
                    </div>
                    <div class="row form-group">
                        <div class="col-md-4"></div>
                        <div class="col-md-4">
                            <label for="email" class="sr-only">Email</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text bg-fr-white"><i class="fa fa-at fa-fw"></i></div>
                                </div>
                                <input type="text" name="email" v-model="email" class="form-control" placeholder="you@domain.com" required="" />
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="validation-error" v-bind:class="{ 'visible': emailError }">
                                {{ emailError }}
                            </div>
                        </div>
                    </div>
                    <div class="row form-group">
                        <div class="col-md-4"></div>
                        <div class="col-md-4">
                            <label for="password" class="sr-only">Password</label>
                            <div class="input-group">
                                <div class="input-group-prepend">
                                    <div class="input-group-text bg-fr-red border-fr-red text-white"><i class="fa fa-key fa-fw"></i></div>
                                </div>
                                <input type="password" name="password" v-model="password" class="form-control" placeholder="P@ssw0rd!" required="" />
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="validation-error" v-bind:class="{ 'visible': passwordError }">
                                {{ passwordError }}
                            </div>
                        </div>
                    </div>
                    <div class="row"> 
                        <div class="col-md-4"></div>
                        <div class="col-md-4">
                            <input type="submit" class="btn btn-block btn-fr-red" value="Create account" :disabled="disabled" />
                        </div>
                    </div>
                </form>
            </div>
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
      passwordError: false,
      disabled: false
    }
  },
  methods: {
    async signup () {
      const vm = this
      vm.usernameError = false
      vm.emailError = false
      vm.passwordError = false
      vm.disabled = true
      try {
        const payload = await axios.post('/accounts/register/', {
          username: vm.username,
          email: vm.email,
          password: vm.password,
          confirm_password: vm.password
        })
        vm.disabled = false
        let key = payload.data.key.private
        let username = payload.data.account.username
        vm.$store.commit('save_key', key)
        vm.$store.commit('save_username', username)
        vm.$router.replace('/signup_success')
      } catch (error) {
        vm.disabled = false
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

