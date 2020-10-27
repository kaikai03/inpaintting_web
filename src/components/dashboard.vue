<template>
    <div>
        <div id="dashboard">
        <div id="el-tab">
            <el-tabs tab-position="top" :v-model="activeTab" @tab-click="tagClick" :before-leave="tagLeave">
                    <el-tab-pane v-for="(worker,index) in workers" :name="worker" :key="worker" >
                        <span slot="label"><i class="el-icon-date"></i>{{worker}}</span>
                    </el-tab-pane>
            </el-tabs>
        </div>
        <div id="dashcontent">
            <dashContent ref="dashContent"></dashContent>
        </div>
    </div>
        </div>
</template>

<script>
    import dashcontent from "~/components/dashcontent";
    export default {
        name: "dashboard",
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
                this.$refs.dashContent.startMonitor(activeName)
            }
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
    #dashboard{
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

