<template>
    <div>
    <div>芜湖dash</div>
        <lineChart></lineChart>
    </div>
</template>

<script>
    import areasplineChart from "~/components/common/areasplineChart";
    export default {
        name: "dashboard",
        components: {
            lineChart:areasplineChart
        }
    }
</script>

<style scoped >


</style>