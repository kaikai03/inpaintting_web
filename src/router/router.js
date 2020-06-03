import Vue from 'vue'
import VueRouter from "vue-router"
Vue.use(VueRouter)

import VueResource from 'vue-resource'
import secondcomponent from "~/components/secondcomponent";
import third from "~/components/third";
import dashboard from "~/components/dashboard";
import uploadtask from "~/components/uploadtask";

Vue.use(VueResource)

const firstview = { template: '<div><h2>我是第 1 个子页面</h2></div>' }

const router = new VueRouter({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      redirect: '/dash'
    },
    {
      path: '/dash',
      components: {main_view:dashboard}
    },
    {
      path: '/upload',
      components: {main_view:uploadtask}
    },
    {
      name: 'first1',
      path: '/first',
      components: {view1:firstview}
    },
    {
      path: '/second',
      components: {view1:secondcomponent}
    },
    {
      name: 'third3',
      path: '/third',
      components: {view1:third,view2:secondcomponent}
    }
  ]
})




export default router;
