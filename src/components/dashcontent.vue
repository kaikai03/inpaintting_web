<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <linesChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                        :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                        :linesShortName="['AVG','C_1','C_2','C_3','C_4']"
                        :unitFormatter=this.tools.addPercentSymbol
                        :yShow="true">
            </linesChart>
        </div>

        <div style="width: 220px;height: 180px;border: 1px solid red;">
            <gaugeChart  ref="memChartVirtual" tag="memChartVirtual" title="MEM" tipName="memory" :min=0 :max=100
                             unitSymbol="%"></gaugeChart >
        </div>

        <div style="width: 220px;height: 180px;border: 1px solid red;">
            <gaugeChart  ref="memChartSwap" tag="memChartSwap" title="SWAP" tipName="swap" :min=0 :max=100
                             unitSymbol="%"></gaugeChart >
        </div>

<!--        <div style="width: 220px;height: 180px;border: 1px solid red;">-->
<!--            <gaugeChart2 ref="memChart" tag="memChart" title="MEM" tipName="mem" :min=0 :max=100-->
<!--                             unitSymbol="%"></gaugeChart2 >-->
<!--        </div>-->

        <div style="width: 320px;height: 60px;border: 1px solid red;">
            <romChart ref="romChart" tag="romChart" tipName="ROM" :unitFormatter=this.tools.numberToSize ></romChart >
        </div>

        <div style="width: 300px;height: 200px;">
            <linesChart ref="netChart" tag="netChart" title="NetIO" :lineCount=2
                      :linesName="['sent','recv']"
                      :linesShortName="['sent','recv']"
                      :yShow="true">
            </linesChart>
        </div>

        <div style="width: 300px;height: 200px;">
            <linesChart ref="ioChart" tag="ioChart" title="DiskIO" :lineCount=2
                      :linesName="['read','write']"
                      :linesShortName="['read','write']"
                      :yShow="true">
            </linesChart>
        </div>



        <span>
            <el-button type="primary" size="mini" class="submit" @click="updateBtn">update</el-button>

        </span>
    </div>
</template>


<script>
    import linesChart from "~/components/common/multiLinesChart";
    import solidGaugeChart from "~/components/common/solidgaugeChart";
    import solidgaugeChart2 from "~/components/common/solidgaugeChart2";
    import transverseColumn from "~/components/common/transverseColumn";

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
            updateCharts(strData){
                //"disk_used": {"total": 78896951296, "used": 27170922496, "free": 51726028800, "percent": 34.4}, "disk_io": {"read_s
                //peed": 0.0, "write_speed": 823296.0}, "net_io": {"sent_speed": 583.0, "recv_speed": 931.0}, "time": 1605158658514
                // console.log('parse：',strData)
                let items = JSON.parse(strData);
                let cpus = items['cpu']['per'];
                cpus.splice(0, 0, items['cpu']['average']);
                let mem = items['memory']
                let rom = items['disk_used'];
                let net_io = items['net_io'];
                let disk_io = items['disk_io'];



                this.$refs.cpuChart.updateLine({'data':cpus,'time':items['time']});
                this.$refs.memChartVirtual.update(mem['virtual']['percent'])
                this.$refs.memChartSwap.update(mem['swap']['percent'])
                //this.$refs.memChart.update(memVirtual,memSwap)

                this.$refs.romChart.update({'data': rom['used'],'time':items['time']},{"min":0,"max":rom['total']})
                this.$refs.netChart.updateLine({'data':[net_io["sent_speed"],net_io["recv_speed"]],'time':items['time']});
                this.$refs.ioChart.updateLine({'data':[net_io["read_s"],net_io["write_speed"]],'time':items['time']});
            },
            updateBtn(){
                //this.$refs.cpuChart.updateLine("updateLine")
                //this.$refs.memChart.updateMem("updateMem")
                // this.$refs.romChart.update2("update")
            },
            startMonitor(workerName){
                //this.$refs.cpuChart.updateLine("updateLine")
                //this.$refs.memChart.updateMem("updateMem")
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
                if(evt.data.substr(0,1) === '{'){
                    this.updateCharts(evt.data);
                }

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
            linesChart:linesChart, gaugeChart:solidGaugeChart,gaugeChart2:solidgaugeChart2,romChart:transverseColumn
        }
    }
</script>

<style scoped>

</style>