<template>
    <div id="third">
        <h1>third</h1>
        <a>written by {{$store.state.name}}</a>
    </div>
</template>

<script>
    export default {
        name: "third",
        data(){
            return {
                author:'third'
            }
        }
    }
</script>

<style scoped>
#third {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
</style>
