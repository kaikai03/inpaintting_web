<template>
  <div id="app" >

<!--    <twinklingimage :imgfile="imgf"></twinklingimage>-->
<!--    <twinklingimage  imgadd="http://127.0.0.1:8888/logo.png" ></twinklingimage>-->
<!--      <iconstable></iconstable>-->
      <mainlayout ></mainlayout >
          <el-button class="el-icon-d-arrow-right" id="dangling" :style="'opacity:'+opacity_dangling" @click="totop_click()"></el-button>
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
              this.opacity_dangling = (offset_percent>0.50)?0.50:offset_percent
          },
          totop_click(){
              this.scroll_top()
          },
          scroll_top(){
              let scrollTimer = setInterval(() => {
                  if (document.documentElement.scrollTop > 0) {
                      document.documentElement.scrollTop -=1
                      this.scroll_top()
                  } else {
                      clearInterval(scrollTimer); // 清除计时器
                  }
              }, 25);
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
        left: 96%;
        top: 88%;
        width: 44px;
        background-color: lightgray;
        z-index: 99;
        border: 0px transparent;
        font-size: 20px;
        transform:rotate(270deg);
        padding-left: 13px;
    }

    #bottom_placeholder {
        width: 100%;
        height: 0px;

    }
</style>
