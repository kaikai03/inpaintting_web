<template>
    <div class="taskqueue">
        <h1>taskqueue</h1>
        <h5>{{author}}</h5>
    </div>
</template>

<script>
    export default {
        name: "taskqueue",
        data(){
            return {
                author:this.$route.path
            }
        }
    }
</script>

<style>
.taskqueue {
    width: 100%;
    height: 100%;
  font-family: Helvetica, sans-serif;
  text-align: center;
}

</style>


<style scoped>

</style>
