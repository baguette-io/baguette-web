<template>
    <div class="container headtitle">
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h1>Log in</h1>
            </div>
        </div>
        <div class="row justify-content-md-center">
            <div class="col-12 col-md-auto">
                <h6>Let's bake</h6>
            </div>
        </div>
        <div class="justify-content-md-center">
            <form class="container mt-4" novalidate method="post" v-on:submit.prevent="login" action="">
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
                        <div class="validation-error" v-bind:class="{ 'visible': generalError }">
                            {{ generalError }}
                        </div>
                    </div>
                </div>
                <div class="row form-group">
                    <div class="col-md-4"></div>
                    <div class="col-md-4">
                        <label for="password" class="sr-only">Password</label>
                        <div class="input-group">
                            <div class="input-group-prepend">
                                <div class="input-group-text bg-fr-white"><i class="fa fa-key fa-fw"></i></div>
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
                        <input type="submit" class="btn btn-block btn-fr-red" value="Log in" />
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
      password: '',
      usernameError: false,
      passwordError: false,
      generalError: false
    }
  },
  methods: {
    async login () {
      const vm = this
      vm.usernameError = false
      vm.passwordError = false
      vm.generalError = false
      try {
        let payload = await axios.post('/accounts/login/', {
          username: vm.username,
          password: vm.password
        })
        const token = payload.data.token
        const username = vm.username
        vm.$store.commit('login', {username, token})
        vm.$router.replace('/dashboard/')
      } catch (error) {
        const data = error.response.data
        Object.keys(data).forEach(function (key) {
          if (key === 'username') {
            vm.usernameError = data[key][0]
          } else if (key === 'password') {
            vm.passwordError = data[key][0]
          } else if (key === 'non_field_errors') {
            vm.generalError = data[key][0]
          }
        })
      }
    }
  }
}
</script>

