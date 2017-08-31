import Vue from 'vue'

Vue.filter('int', function (value) {
  return parseInt(value)
})
