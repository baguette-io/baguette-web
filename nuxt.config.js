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
    '~plugins/axios',
    '~plugins/filters'
  ],
  /*
  ** Headers of the page
  */
  head: {
    title: 'Baguette',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'baguette.io web interface' }
    ],
    script: [
            { src: 'https://code.jquery.com/jquery-3.3.1.slim.min.js'},
            { src: 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js'},
            { src: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js'},
            { src: 'https://use.fontawesome.com/93d495b768.js'}
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/images/baguette.png' },
      { rel: 'stylesheet', href: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css'},
      { rel: 'stylesheet', href: '/css/breadcrumb.css'},
      { rel: 'stylesheet', href: '/css/dashboard.css'},
      { rel: 'stylesheet', href: '/css/footer.css'},
      { rel: 'stylesheet', href: '/css/home.css'},
      { rel: 'stylesheet', href: '/css/identification.css'},
      { rel: 'stylesheet', href: '/css/main.css'},
      { rel: 'stylesheet', href: '/css/modal.css'},
      { rel: 'stylesheet', href: '/css/navbar.css'},
      { rel: 'stylesheet', href: '/css/pagination.css'},
      { rel: 'stylesheet', href: '/css/ribbon.css'},
      { rel: 'stylesheet', href: '/css/window.css'}
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
