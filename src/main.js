import Vue from 'vue'
import ElementUI from 'element-ui'
// import 'element-ui/lib/theme-chalk/index.css'
import '../theme/index.css'
import router_ from "~/router/router";
import store_ from "~/store";
import App from './App.vue'
Vue.use(ElementUI)

import VueCookies from 'vue-cookies'
Vue.use(VueCookies);

import VideoPlayer from 'vue-video-player'
import 'vue-video-player/src/custom-theme.css'
import 'video.js/dist/video-js.css'
Vue.use(VideoPlayer)

import global_backen from "~/global_backen";
Vue.prototype.backen = global_backen

import tools from "~/tools";
Vue.prototype.tools = tools

import http from "~/api/http";
Vue.prototype.network = http


// Vue.config.debug = true;


import firstcomponent from '~/components/firstcomponent.vue'
import secondcomponent from '~/components/secondcomponent.vue'
import third from "~/components/third";


// Vue.http.interceptors.push((request, next) => {
//   // 请求发送前的处理逻辑
//   request.headers.set('Access-Control-Allow-Origin', '*')
//   next((response) => {
//     // 请求发送后的处理逻辑
//     // 根据请求的状态，response参数会返回给successCallback或errorCallback
//     return response
//   })
// })




new Vue({
  el: '#main',
  router: router_,
  store:store_,
  render: h => h(App)
})
