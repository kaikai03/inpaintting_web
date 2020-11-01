<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <cpuChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                      :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                      :linesShortName="['AVG','C_1','C_2','C_3','C_4']" unitSymbol="%">
            </cpuChart>
        </div>

        <div style="width: 300px;height: 200px;">
            <solidgaugeChart ref="memChart" tag="memChart" title="MEM" tipName="MEM" :min=0 :max=100
                             unitSymbol="%"></solidgaugeChart>
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

        name: "dashcontent",
        data(){
            return {
                isConnected:false,
                ws:null,
                isConnectedError:false,
                curWorker:null,
                reconnectCounter:0
            }
        },
        methods:{
            updateBtn(){
                this.$refs.cpuChart.updateLine("updateLine")
                this.$refs.memChart.updateMem("updateMem")
            },
            startMonitor(workerName){
                this.$refs.cpuChart.updateLine("updateLine")
                this.$refs.memChart.updateMem("updateMem")
                console.log(workerName+":startMonitor")
                this.backenConnect(workerName)
            },
            backenConnect(workerName){
                if(this.isConnected){
                    console.log(this.curWorker+':disconnet')
                    this.backenDisconnect() //change and reconnect
                }
                this.ws = new WebSocket(this.backen.dashboardMonitorSocket(workerName));

                this.ws.onopen = this.onConnect;
                this.ws.onmessage = this.onMessage;
                this.ws.onclose = this.onSocketClose;
                this.ws.onerror = this.onSocketError
                this.curWorker = workerName
            },
            onConnect(evt){
                console.log(this.curWorker+"Connection open ...");
                  // this.ws.send("Hello WebSockets!");
                  this.isConnected = true;
                  this.isConnectedError = false;
                  this.reconnectCounter = 0;
            },
            onMessage(evt){
                console.log(this.curWorker+"Received Message: " + evt.data);
                this.isConnectedError = false;
                this.reconnectCounter = 0;
            },
            onSocketClose(evt){
                console.log(this.curWorker+"Connection closed.");
                if (this.isConnectedError && this.reconnectCounter<5) {
                    console.log("remote connect error.",this.reconnectCounter);
                    this.reconnectCounter +=1
                    this.backenConnect(this.curWorker) //reconnect
                }

            },
            onSocketError(){
                console.log(this.curWorker+'Connection error')
                this.isConnectedError = true
                this.isConnected = false
            },
            backenDisconnect(evt){
                this.isConnectedError = false;
                this.isConnected = false
                this.ws.close(1000);
            }
        },
        components: {
            cpuChart:cpuChart, solidgaugeChart:solidgaugeChart
        }
    }
</script>

<style scoped>

</style>