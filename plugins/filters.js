import Vue from 'vue'

Vue.filter('int', function (value) {
  return parseInt(value)
})

Vue.filter('format_date', function (value) {
  const date = new Date(value)
  return date.toLocaleDateString()
})
