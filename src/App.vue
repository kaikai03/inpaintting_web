<template>
  <div id="app">

<!--    <twinklingimage imgname="logo.png"></twinklingimage>-->
    <twinklingimage :imgfile="imgf"></twinklingimage>
<!--      <iconstable></iconstable>-->
<!--      <mainlayout></mainlayout>-->
  </div>
</template>

<script>
  import mainlayout from "~/components/mainlayout";
  import iconstable from "~/components/common/iconstable";
  import twinklingimage from "~/components/common/twinklingimage";
  export default {
    data(){
      return {
        imgf:require('./assets/logo.png'),
        dirname:__dirname
      }
    },
    methods: {

    },
    components:{
      mainlayout,iconstable,twinklingimage
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
