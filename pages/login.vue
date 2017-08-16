<template>
    <div class="container">
        <div class="row">
            <div class="offset-md-5 col-md-4">
                <h2 class="title">Log in</h2>
            </div>
        </div>
        <form class="form-horizontal" method="post" v-on:submit.prevent="login" action="">
            <div class="form-group row" v-bind:class="{ 'has-danger': generalError }">
                <template v-if="generalError">
                    <div class="col-md-4"></div>
                    <label for="error" class="sr-only">Error</label>
                    <div class="col-md-4">
                        <div class="text-center text-danger">
                        {{ generalError }}
                        </div>
                    </div>
                </template>
            </div>
            <div class="form-group row" v-bind:class="{ 'has-danger': usernameError }">
                <div class="col-md-4"></div>
                <label for="username" class="sr-only">Username</label>
                <div class="input-group col-md-4">
                    <div class="input-group-addon"><i class="fa fa-user"></i></div>
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
            <div class="form-group row" v-bind:class="{ 'has-danger': passwordError }">
                <div class="col-md-4"></div>
                <label for="password" class="sr-only">Password</label>
                <div class="input-group col-md-4">
                    <div class="input-group-addon"><i class="fa fa-key"></i></div>
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
                <div class="offset-md-4 col-md-4">
                    <input type="submit" class="btn btn-block btn-secondary text-danger" value="Log in" />
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

