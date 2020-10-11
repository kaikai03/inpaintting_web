<template>
    <div>
        <div id="dashboard">
        <div id="el-tab">
        <el-tabs  tab-position="top" :v-model="activeTab" @tab-click="tagClick" :before-leave="tagLeave">
            <el-tab-pane name="A">
                <span slot="label"><i class="el-icon-date"></i> AAAA</span>
            </el-tab-pane>
            <el-tab-pane label="BBBB" name="B">

            </el-tab-pane>

            <el-tab-pane label="CCCC" name="C">

            </el-tab-pane>
            <el-tab-pane label="DDDD" name="D"></el-tab-pane>
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
                activeTab:null
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