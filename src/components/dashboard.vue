<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <cpuChart ref="cpuChart"></cpuChart>
        </div>
        <div style="width: 300px;height: 200px;">
            <memChart ref="memChart"></memChart>
        </div>
        <span>
            <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>

        </span>
    </div>
</template>

<script>
    import cpuChart from "~/components/common/cpuChart";
    import memChart from "~/components/common/memChart";
    export default {
        name: "dashboard",
        methods:{
            updateBtn(){
                this.$refs.cpuChart.updateLine("updateLine")
                this.$refs.memChart.updateMem("updateMem")

            }
        },
        components: {
            cpuChart:cpuChart, memChart:memChart
        }
    }
</script>

<style scoped >


</style>