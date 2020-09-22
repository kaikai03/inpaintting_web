<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <cpuChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                      :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                      :linesShortName="['AVG','C_1','C_2','C_3','C_4']" unitSymbol="%">
            </cpuChart>
        </div>
        <div style="width: 300px;height: 200px;">
            <solidgaugeChart ref="memChart" tag="memChart" title="MEM" :min=0 :max=100 unitSymbol="%"></solidgaugeChart>
        </div>
        <span>
            <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>

        </span>
    </div>
</template>

<script>
    import cpuChart from "~/components/common/multiLinesChart";
    import solidgaugeChart from "~/components/common/solidgaugeChart";
    export default {
        name: "dashboard",
        methods:{
            updateBtn(){
                this.$refs.cpuChart.updateLine("updateLine")
                this.$refs.memChart.updateMem("updateMem")

            }
        },
        components: {
            cpuChart:cpuChart, solidgaugeChart:solidgaugeChart
        }
    }
</script>

<style scoped >


</style>