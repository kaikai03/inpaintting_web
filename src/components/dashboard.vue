<template>
    <div>
    <div>芜湖dash</div>
        <cpuChart ref="cpuChart"></cpuChart>
        <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>
    </div>
</template>

<script>
    import cpuChart from "~/components/common/cpuChart";
    export default {
        name: "dashboard",
        methods:{
            updateBtn(){
                this.$refs.cpuChart.updateLine("updateLine")
            }
        },
        components: {
            cpuChart:cpuChart
        }
    }
</script>

<style scoped >


</style>