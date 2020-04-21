<template>
  <div id="app">
      <mainlayout></mainlayout>
  </div>
</template>

<script>
  import mainlayout from "~/components/mainlayout";
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
      mainlayout
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
