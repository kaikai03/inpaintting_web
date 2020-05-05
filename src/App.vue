<template>
  <div id="app">

<!--    <twinklingimage :imgfile="imgf"></twinklingimage>-->
<!--    <twinklingimage  imgadd="http://127.0.0.1:8888/logo.png" ></twinklingimage>-->
<!--      <iconstable></iconstable>-->
      <mainlayout></mainlayout>
  </div>
</template>

<script>
  import mainlayout from "~/components/mainlayout";
  import iconstable from "~/components/common/iconstable";
  import twinkling_image from "~/components/common/twinkling_image";
  export default {
    data(){
      return {
        imgf:"",
        dirname:__dirname
      }
    },
      methods: {},
      mounted() {
          this.imgf = require('./assets/logo.png')
          // this.$router.push({name:"first1"})
      },
      components: {
          mainlayout, iconstable, twinkling_image
      }
  }
</script>

<style>
#app{
  margin:0px auto;
  padding:0px;
}
body{
  margin:0px auto;
  padding:0px;
}

</style>
