<template>
    <div>
        <div id="dashboard">
        <div id="el-tab">
            <el-tabs tab-position="top" :v-model="activeTab" @tab-click="tagClick" :before-leave="tagLeave">
                    <el-tab-pane v-for="(worker,index) in workers" :name="worker" >
                        <span slot="label"><i class="el-icon-date"></i>{{worker}}</span>
                    </el-tab-pane>
            </el-tabs>
        </div>
        <div id="dashcontent">
            <dashcontent ></dashcontent>
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
                console.log("tagLeave:",activeName, oldActiveName);
            }
        },
        components: {
            dashcontent:dashcontent,
        }
    }
</script>

<style scoped>
    #dashboard{
        display: flex;
        flex-direction: column;
        height: 100%;
        width: 100%;
    }
    #el-tab{
        background: blue;
        height: 40px;
        margin-top: 5px;
        margin-left: 20px;
        margin-right: 20px;
    }

    #dashcontent{
        background: red;
        height: calc(100% - 40px - 20px);
        margin-top: 5px;
        margin-left: 20px;
        margin-right: 20px;
    }

</style>