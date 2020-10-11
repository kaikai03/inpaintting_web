<template>
    <div>
        <el-tabs :tab-position="top" style="height: 200px; width: 100%">
            <el-tab-pane label="AAAA">
                <div style="width: 300px;height: 200px;">
                    <cpuChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                              :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                              :linesShortName="['AVG','C_1','C_2','C_3','C_4']" unitSymbol="%">
                    </cpuChart>
                </div>
            </el-tab-pane>
            <el-tab-pane label="BBBB">
                <div style="width: 300px;height: 200px;">
                    <solidgaugeChart ref="memChart" tag="memChart" title="MEM" tipName="MEM" :min=0 :max=100
                                     unitSymbol="%"></solidgaugeChart>
                </div>
            </el-tab-pane>

            <el-tab-pane label="CCCC">角色管理</el-tab-pane>
            <el-tab-pane label="DDDD">定时任务补偿</el-tab-pane>
        </el-tabs>



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