<template>
  <div id="app">
    <img src="./assets/logo.png">
    <div>
      <p>{{msg}},{{dirname}}</p>
      <el-button @click="startHacking">Start</el-button>
      <el-input v-model="msg"></el-input>
    </div>
    <firstcomponent></firstcomponent>
    <ul>
      <li> <router-link to="/first">“第一页” </router-link> </li>
      <li> <router-link to="/second">“第二页” </router-link> </li>
      <!-- 带查询参数，下面的结果为 /second?xxx=private -->
      <li> <router-link to="/third" >“third” </router-link> </li>
    </ul>
    <router-view class="view"></router-view>
  </div>
</template>

<script>
  import firstcomponent from "~/components/firstcomponent";
  export default {
    data(){
      return {
        msg:'export',
        dirname:__dirname
      }
    },
    methods: {
      startHacking () {
        this.$notify({
          title: 'It works!',
          type: 'success',
          message: 'We\'ve laid the ground work for you. It\'s time for you to build something epic!',
          duration: 5000
        })
      }
    },
    components:{
      firstcomponent
    }
  }
</script>

<style>
  #app {
    font-family: Helvetica, sans-serif;
    text-align: center;
  }
  .router-link-active{
    background-color: beige;
    font-size: 30px;
  }
</style>
