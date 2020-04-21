<template>
  <div id="app">
    <transition mode="out-in">
      <mainlayout></mainlayout>
    </transition>
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
  height: 100%;
}

</style>
