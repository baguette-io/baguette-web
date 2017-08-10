import Vuex from 'vuex'

const store = () => new Vuex.Store({
  state: {
    auth_token: null,
    username: null,
    private_key: null
  },
  mutations: {
    save_key (state, key) {
      state.private_key = key
    },
    save_username (state, username) {
      state.username = username
    },
    login (state, username, token) {
      state.username = username
      state.auth_token = token
    },
    logout (state, token) {
      state.username = null
      state.auth_token = null
    }
  }
})

export default store
