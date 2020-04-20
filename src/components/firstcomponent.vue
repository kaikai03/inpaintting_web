<template>
    <div id="firstcomponent">
        <h1>footer</h1>
        <a>written by {{author}}</a>
    </div>
</template>

<script>
    export default {
        name: "firstcomponent",
        data(){
            return {
                author:'kk'
            }
        }
    }
</script>

<style scoped>
#firstcomponent {
  font-family: Helvetica, sans-serif;
  text-align: right;
}
</style>