<template>
    <div>
        <h2 class="title ml-sm-5">Sign up</h2>
        <form class="form-horizontal" method="post" v-on:submit.prevent="signup" action="">
            <div class="form-group row">
                <label for="username" class="sr-only">Username</label>
                <div class="input-group mb-2 mr-sm-2 mb-sm-0">
                    <div class="input-group-addon"><i class="fa fa-user"></i></div>
                    <input type="text" name="username" v-model="username" class="form-control" placeholder="Username" required="" />
                </div>
            </div>
            <div class="form-group row">
                <label for="email" class="sr-only">Email</label>
                <div class="input-group mb-2 mr-sm-2 mb-sm-0">
                    <div class="input-group-addon"><i class="fa fa-at"></i></div>
                    <input type="text" name="email" v-model="email" class="form-control" placeholder="you@domain.com" required="" />
                </div>
            </div>
            <div class="form-group row">
                <label for="password" class="sr-only">Password</label>
                <div class="input-group mb-2 mr-sm-2 mb-sm-0">
                    <div class="input-group-addon"><i class="fa fa-key"></i></div>
                    <input type="password" name="password" v-model="password" class="form-control" placeholder="P@ssw0rd!" required="" />
                </div>
            </div>
            <div class="row">
                <input type="submit" class="btn btn-block btn-secondary text-danger" value="Create account" />
            </div>
        </form>
    </div>
</template>

<script>
import axios from '../plugins/axios'

export default {
  layout: 'identification',
  data () {
    return {
      username: '',
      email: '',
      password: ''
    }
  },
  methods: {
    async signup () {
      console.log(axios)
      await axios.post('/accounts/register/', {
        username: this.username,
        email: this.email,
        password: this.password,
        confirm_password: this.password
      })
    }
  }
}
</script>

