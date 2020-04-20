import Vue from 'vue'
import VueRouter from "vue-router"
Vue.use(VueRouter)

import VueResource from 'vue-resource'
import secondcomponent from "~/components/secondcomponent";
import third from "~/components/third";
Vue.use(VueResource)

const firstview = { template: '<div><h2>我是第 1 个子页面</h2></div>' }

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
      components: {view1:firstview}
    },
    {
      path: '/second',
      components: {view1:secondcomponent}
    },
    {
      path: '/third',
      components: {view2:third}
    },
  ]
})


export default router;
