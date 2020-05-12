<template>
  <div id="app" >

<!--    <twinklingimage :imgfile="imgf"></twinklingimage>-->
<!--    <twinklingimage  imgadd="http://127.0.0.1:8888/logo.png" ></twinklingimage>-->
<!--      <iconstable></iconstable>-->
      <mainlayout ></mainlayout >
          <el-button id="dangling" :style="'opacity:'+opacity_dangling"></el-button>
      <div id="bottom_placeholder" />
  </div>
</template>

<script>
  import mainlayout from "~/components/mainlayout";
  import iconstable from "~/components/common/iconstable";
  import twinkling_image from "~/components/common/twinkling_image";
  export default {
      data() {
          return {
              imgf: "",
              dirname: __dirname,
              opacity_dangling:0
          }
      },
      methods: {
          scroll_handle() {
              let pos = document.documentElement.scrollTop

              let window_height = document.documentElement.clientHeight
              let body_height = document.body.clientHeight
              let offset_percent = pos/(body_height-window_height)
              this.opacity_dangling = (offset_percent>0.70)?0.70:offset_percent
          }
      },
      mounted() {
          // this.imgf = require('./assets/logo.png')
          // this.$router.push({name:"first1"})
          window.addEventListener('scroll',this.scroll_handle)
      },
      components: {
          mainlayout, iconstable, twinkling_image
      }
  }
</script>

<style>
    #app {
        margin: 0px auto;
        padding: 0px;
    }

    body {
        margin: 0px auto;
        padding: 0px;
    }

    #dangling {
        position: fixed;
        left: 0px;
        bottom: 0px;
        width: 100%;
        height: 20px;
        background-color: lightgray;
        z-index: 99;
        border: 0px transparent;
    }

    #bottom_placeholder {
        width: 100%;
        height: 25px;

    }
</style>
