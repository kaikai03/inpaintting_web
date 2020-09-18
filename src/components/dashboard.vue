<template>
    <div>
    <div>芜湖dash</div>
        <lineChart ref="lineChart"></lineChart>
        <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>
    </div>
</template>

<script>
    import areasplineChart from "~/components/common/areasplineChart";
    export default {
        name: "dashboard",
        methods:{
            updateBtn(){
                this.$refs.lineChart.updateLine("updateLine")
            }
        },
        components: {
            lineChart:areasplineChart
        }
    }
</script>

<style scoped >


</style>