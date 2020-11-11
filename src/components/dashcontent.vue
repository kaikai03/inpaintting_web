<template>
    <div>
        <div style="width: 300px;height: 200px;">
            <linesChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                      :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                      :linesShortName="['AVG','C_1','C_2','C_3','C_4']" unitSymbol="%"
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

        <div style="width: 220px;height: 180px;border: 1px solid red;">
            <gaugeChart2 ref="memChart" tag="memChart" title="MEM" tipName="mem" :min=0 :max=100
                             unitSymbol="%"></gaugeChart2 >
        </div>

        <div style="width: 1320px;height: 80px;border: 1px solid red;">
            <romChart ref="romChart" tag="romChart" tipName="ROM"></romChart >
        </div>

        <div style="width: 300px;height: 200px;">
            <linesChart ref="netChart" tag="netChart" title="CPU(%)" :lineCount=2
                      :linesName="['sent','recv']"
                      :linesShortName="['sent','recv']"
                      :yShow="true">
            </linesChart>
        </div>

        <div style="width: 300px;height: 200px;">
            <linesChart ref="ioChart" tag="ioChart" title="CPU(%)" :lineCount=2
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

<!--               {-->
<!--	"cpu": {-->
<!--		"average": 38.73,-->
<!--		"per": [42.4, 26.6, 32.8, 53.1]-->
<!--	},-->
<!--	"memory": {-->
<!--		"virtual": {-->
<!--			"total": 17057574912,-->
<!--			"available": 5507387392,-->
<!--			"percent": 67.7,-->
<!--			"used": 11550187520,-->
<!--			"free": 5507387392-->
<!--		},-->
<!--		"swap": {-->
<!--			"total": 26919690240,-->
<!--			"used": 17541074944,-->
<!--			"free": 9378615296,-->
<!--			"percent": 65.2,-->
<!--			"sin": 0,-->
<!--			"sout": 0-->
<!--		}-->
<!--	},-->
<!--	"disk_used": {-->
<!--		"total": 78896951296,-->
<!--		"used": 27166470144,-->
<!--		"free": 51730481152,-->
<!--		"percent": 34.4-->
<!--	},-->
<!--	"disk_io": {-->
<!--		"read_speed": 311296.0,-->
<!--		"write_speed": 0.0-->
<!--	},-->
<!--	"net_io": {-->
<!--		"sent_speed": 994.0,-->
<!--		"recv_speed": 1892.0-->
<!--	},-->
<!--	"time": 1604667963-->
<!--}-->

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
                // {"memory": {"virtual": {"total": 25679904768, "available": 16036134912, "percent": 37.6, "used": 9643769856, "free": 16036134912}, "swap": {"total": 36472508416, "used": 16790478848, "free": 19682029568, "percent": 46.0, "sin": 0, "sout": 0}},
                // console.log('parse：',strData)
                let items = JSON.parse(strData);
                let cpus = items['cpu']['per'];
                let memVirtual = items['memory']['virtual']['percent'];
                let memSwap = items['memory']['swap']['percent'];
                console.log('memVirtual：',memVirtual);
                console.log('memSwap：',memSwap);
                cpus.splice(0, 0, items['cpu']['average']);
                this.$refs.cpuChart.updateLine({'data':cpus,'time':items['time']});
                this.$refs.memChartVirtual.update(memVirtual)
                this.$refs.memChartSwap.update(memSwap)
                this.$refs.memChart.update(memVirtual,memSwap)

            },
            updateBtn(){
                //this.$refs.cpuChart.updateLine("updateLine")
                //this.$refs.memChart.updateMem("updateMem")
                this.$refs.romChart.update2("update")
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