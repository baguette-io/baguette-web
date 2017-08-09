import Vuex from 'vuex'

const store = () => new Vuex.Store({
  state: {
    user: null,
    private_key: null
  },
  mutations: {
    save_key (state, key) {
      state.private_key = key
    }
  }
})

export default store
