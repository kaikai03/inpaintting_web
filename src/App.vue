<template>
  <div id="app">
      <iconstable></iconstable>
      <mainlayout></mainlayout>
  </div>
</template>

<script>
  import mainlayout from "~/components/mainlayout";
  import iconstable from "~/components/common/iconstable";

  export default {
    data(){
      return {
        msg:'export',
        dirname:__dirname
      }
    },
    methods: {

    },
    components:{
      mainlayout,iconstable
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
