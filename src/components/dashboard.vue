<template>
    <div>
    <div style="width: 400px;height: 200px;">
        <cpuChart ref="cpuChart"></cpuChart>
    </div>
        <div>
        <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>

    </div>
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