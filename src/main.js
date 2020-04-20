import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'
Vue.use(ElementUI)


import VueRouter from "vue-router"
Vue.use(VueRouter)

import VueResource from 'vue-resource'
Vue.use(VueResource);


// Vue.config.debug = true;


const firstview = { template: '<div><h2>我是第 1 个子页面</h2></div>' }
import firstcomponent from '~/components/firstcomponent.vue'
import secondcomponent from '~/components/secondcomponent.vue'
import third from "~/components/third";

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      redirect: '/first'
    },
    {
      path: '/first',
      component: firstview
    },
    {
      path: '/second',
      component: secondcomponent
    },
    {
      path: '/third',
      component: third
    },
  ]
})


new Vue({
  el: '#first',
  router: router,
  render: h => h(App)
})
