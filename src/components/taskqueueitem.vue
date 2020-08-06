<template>
    <div class="queue-item">
        <el-row type="flex">
            <el-col :span="4" id="index" > {{index}}</el-col>
            <el-col :span="12" >
                <div id="name">{{name}}</div>
                <div id="time">{{time}}</div>
            </el-col>
        </el-row>

        <el-row >
            <el-col :span="4"  id="star">
                <el-button class="star" type="text" @click="onStarClick(index)">
                    <i :class="{'el-icon-star-on':1, 'icon-red':'red'=='blue', 'icon-blue':'blue'=='blue'}"></i>
                </el-button>
            </el-col>
            <el-col :span="12" id="img"> {{img}} </el-col>
        </el-row>

<!--        <p>{{index}}, {{stat}}</p>-->
<!--        <p>{{name}}, {{time}}</p> class="el-form-item__label"-->
<!--        <p>{{img}}, {{progress}}</p>-->

    </div>
</template>

<script>

    export default {
        name: "queueItem",
        props: {'index':Number,'name':String,'img':String,'progress':Number, 'stat':String, 'time':String},
    }

</script>

<style scoped>
    .queue-item{
        width: 100%;
        height: auto;
        border-radius: 5px;
        background-color: lightblue;

        text-align: left;
        vertical-align: middle;

        font-size: 14px;
        color: #606266;
        padding: 0px 12px 0 0;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }
    #index{
        padding: 8px 0px 0px 8px;
    }
    #star {
        font-size: 1px;
        height: 50px;
    }
    #star .el-button--text{
         /*border-color:red;*/
        /*padding-left: 5px;*/
        /*padding-right: 5px;*/
        /*padding-top: 0px;*/
        /*padding-bottom: 26px;*/
        padding: 0px 5px 26px 5px;
        margin-top: -8px
    }
    .icon-red{
        color: red;
    }
    .icon-blue{
        color: blue;
    }

</style>

<style>
   .el-icon-star-on {
       font-size: 22px;
    }
</style>