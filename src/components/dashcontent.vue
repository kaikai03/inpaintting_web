<template>
    <div id="dashContent">
        <div class="transverse" id="rom">
            <romChart ref="romChart" tag="romChart" tipName="ROM" :unitFormatter=this.tools.numberToSize ></romChart >
        </div>

        <div class="lines" id="cpuLines" >
            <linesChart ref="cpuChart" tag="cpuChart" title="CPU(%)" :lineCount=5
                        :linesName="['CPU','CPU-1','CPU-2','CPU-3','CPU-4']"
                        :linesShortName="['AVG','C_1','C_2','C_3','C_4']"
                        :unitFormatter=this.tools.addPercentSymbol
                        :yShow="true">
            </linesChart>
        </div>


        <div class="lines" id="netio" >
            <linesChart ref="netChart" tag="netChart" title="NetIO" :lineCount=2
                        :linesName="['sent','recv']"
                        :linesShortName="['sent','recv']"
                        :unitFormatter=this.tools.numberToSize
                        :yShow="true">
            </linesChart>
        </div>

        <div class="lines" id="diskio">
            <linesChart ref="ioChart" tag="ioChart" title="DiskIO" :lineCount=2
                        :linesName="['read','write']"
                        :linesShortName="['read','write']"
                        :unitFormatter=this.tools.numberToSize
                        :yShow="true">
            </linesChart>
        </div>

<!--            <div id="memS">-->
        <div class="gauge" id="memV">
            <gaugeChart  ref="memChartVirtual" tag="memChartVirtual" title="MEM" tipName="memory" :min=0 :max=100
                             unitSymbol="%"></gaugeChart >
        </div>

        <div class="gauge" id="Swap">
            <gaugeChart  ref="memChartSwap" tag="memChartSwap" title="SWAP" tipName="swap" :min=0 :max=100
                             unitSymbol="%"></gaugeChart >
        </div>
<!--                </div>-->


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
    #dashContent {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .lines {
        box-sizing:border-box;
        width: 50%;
        height: 220px;
        padding: 5px 5px 5px 0px;

    }
    .gauge {
        width: 220px;
        height: 150px;
        border: 1px solid red;
    }
    .transverse{
        width: 100%;
        height: 60px;
        border: 1px solid red;
    }

    #cpuLines {

    }

    #memV {

    }

    #memS {

    }

    #rom {

    }

    #netio {

    }

    #diskio {

    }

</style>