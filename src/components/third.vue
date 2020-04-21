<template>
    <div id="third">
        <h1>third</h1>
        <a>written by {{$store.state.name}}</a><br>
        <a>author by {{author}}</a>
    </div>
</template>

<script>
    export default {
        name: "third",
        data(){
            return {
                author:this.$route.path
            }
        },
        beforeRouteLeave(to, from, next) {
            const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
            if (answer) {
                next()
            } else {
                next(false)
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
