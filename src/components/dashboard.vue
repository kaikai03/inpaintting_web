<template>
    <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="24" class="grid-content bg-purple">
            <div class="dashboard">
                <div id="el-tab">
                    <el-tabs tab-position="top" :v-model="activeTab" @tab-click="tagClick" :before-leave="tagLeave">
                        <el-tab-pane v-for="(worker,index) in workers" :name="worker" :key="worker">
                            <span slot="label"><i class="el-icon-date"></i>{{worker}}</span>
                        </el-tab-pane>
                    </el-tabs>
                </div>
                <div id="dashcontent">
                    <dashContent ref="dashContent"></dashContent>
                </div>
            </div>
        </el-col>
    </el-row>
</template>

<script>
    let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
    import dashcontent from "~/components/dashcontent";
    export default {
        name: "dashboard",
        beforeRouteLeave(to, from, next) {
            console.log("beforeRouteLeave")
              if(this.$refs.dashContent.isConnected){
                  this.$refs.dashContent.backenDisconnect()
              }
              next();
            },
        data(){
            return {
                activeTab:null,
                workers:['worker1','worker2','worker3','worker4']
            }
        },
        methods:{
            tagClick(tab, event){
                console.log("tagClick:",tab, event);
            },
            tagLeave(activeName, oldActiveName){
                if (activeName==0){
                    return
                }
                console.log("tagLeave:",activeName, oldActiveName);
                // if (this.$refs.dashContent.isConnected) {
                //     this.$refs.dashContent.backenDisconnect()
                //     this.$refs.dashContent.ws.close(1000)
                //     sleep(5000).then(() => {
                //         console.log("zhantingjiesu");
                //         this.$refs.dashContent.startMonitor(activeName)
                //     })
                // } else {
                    this.$refs.dashContent.startMonitor(activeName)
                // }

            }
        },
        mounted() {
            const loading = this.$loading({
                          lock: true,
                          text: '正在联系工人，请稍后...',
                          // spinner: 'el-icon-loading',
                          background: 'rgba(0, 0, 0, 0.6)',
                          target: document.querySelector('.el-tab')
                        });
            this.network.get_request(this.backen.getOnlineWorkers(),
                            (res) => {
                                console.log(res);
                                console.log("get workers success");
                                loading.close();
                            },
                            (er) => {
                                console.log(er)
                                if(er.status == 507){
                                    this.$message({message: '服务器存储错误，请刷新页面', center: true, showClose: true, type: 'error',effect:"dark"});
                                }else{
                                    this.$message({message: '网络错误，请重新加载', center: true, showClose: true, type: 'error' });
                                }
                                loading.close();
                            }
                        )
        },
        components: {
            dashContent:dashcontent,
        }
    }
</script>

<!--<link rel="stylesheet" href="http://view.jqueryfuns.com/2015/7/1/ba27e27fe4934e1f15219ad0b58e7c74/css/gizmoMenu.css" type="text/css" />-->
<!--<script src="http://view.jqueryfuns.com/2015/7/1/ba27e27fe4934e1f15219ad0b58e7c74/js/jquery-2.1.3.min.js" ></script >-->
<!--<script src="http://view.jqueryfuns.com/2015/7/1/ba27e27fe4934e1f15219ad0b58e7c74/js/gizmoMenu.js" ></script >-->

<style scoped>
    .row-bg {
    padding: 0px 0;
    background-color: transparent!important;
  }
    .el-col {
        height: 100%;
        border-radius: 4px;
    }
        .bg-purple-dark {
        background: #99a9bf;
    }

    .bg-purple {
        background: #d3dce6;
    }

    .bg-purple-light {
        background: #e5e9f2;
    }

    .grid-content {
        border-radius: 10px;
        min-height: 36px;
    }

    .dashboard{
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    #el-tab{
        /*background: blue;*/
        height: 40px;
        margin-top: 5px;
        margin-left: 20px;
        margin-right: 20px;
    }

    #dashcontent{
        /*background: red;*/
        height: calc(100% - 40px - 20px);
        margin-top: 5px;
        margin-left: 20px;
        margin-right: 20px;
    }

</style>

