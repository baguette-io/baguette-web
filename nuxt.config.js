module.exports = {
  /*
  ** Dependencies
  */
  modules: [
    '@nuxtjs/axios'
  ],
  /*
  ** Envs
  */
  env: {
    endpoint: process.env.ENDPOINT
  },
  /*
  ** Plugins
  */
  plugins: [
    '~plugins/axios'
  ],
  /*
  ** Headers of the page
  */
  head: {
    title: 'baguette.io',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'baguette.io web interface' }
    ],
    script: [
            { src: 'https://code.jquery.com/jquery-3.1.1.slim.min.js'},
            { src: 'https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js'},
            { src: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js'},
            { src: 'https://use.fontawesome.com/93d495b768.js'}
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/images/favicon.ico' },
      { rel: 'stylesheet', href: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css'},
      { rel: 'stylesheet', href: '/css/main.css'}
    ]
  },
  /*
  ** Build configuration
  */
  build: {
    vendor: [
        'axios'
    ],
    /*
    ** Run ESLINT on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
