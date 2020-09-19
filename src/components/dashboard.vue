<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <cpuChart ref="cpuChart"></cpuChart>
        </div>
        <div style="width: 300px;height: 200px;">
            <gaugeChart ref="gaugeChart"></gaugeChart>
        </div>
        <div>
            <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>

        </div>
    </div>
</template>

<script>
    import cpuChart from "~/components/common/cpuChart";
    import gaugeChart from "~/components/common/gaugeChart";
    export default {
        name: "dashboard",
        methods:{
            updateBtn(){
                this.$refs.cpuChart.updateLine("updateLine")
                this.$refs.gaugeChart.updateMem("updateMem")

            }
        },
        components: {
            cpuChart:cpuChart, gaugeChart:gaugeChart
        }
    }
</script>

<style scoped >


</style>