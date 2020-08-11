<template>
    <div class="queue-item">
        <el-row type="flex">
            <el-col :span="4" id="index" >
                <span id="index-text">
                    {{index}}
                </span>
            </el-col>
            <el-col :span="18" >
                <div id="name" :alt="name">{{name}}</div>
                <div id="time">{{time}}</div>
            </el-col>
        </el-row>

        <el-row >
            <el-col :span="4" id="star">
                <el-popover
                        placement="bottom"
                        width="100"
                        trigger="focus">
                      <div style="text-align: right; margin: 0">
                        <el-button  type="text" @click="onStarClick('正常')" >
                            <i class="el-icon-star-on icon-red"> </i>
                        </el-button>
                        <el-button  type="text" @click="onStarClick('插队')" >
                            <i class="el-icon-star-on icon-blue"> </i>
                        </el-button>
                          <el-button  type="text" @click="onStarClick('滞后')" >
                            <i class="el-icon-star-on icon-blue"> </i>
                        </el-button>
                          <el-button  type="text" @click="onStarClick('暂停')" >
                            <i class="el-icon-star-on icon-blue"> </i>
                        </el-button>
                      </div>

                    <el-button class="star" type="text" slot="reference">
                        <i :class="{'el-icon-star-on':1, 'icon-red':'red'==btnStat, 'icon-gray':'gray'==btnStat }"></i>
                    </el-button>
                </el-popover>
            </el-col>
            <el-col :span="20" id="img">
<!--                'fill', 'contain', 'cover', 'none', 'scale-down'-->
                <el-image id="image" fit="contain" lazy
                        src="https://fuss10.elemecdn.com/a/3f/3302e58f9a181d2509f3dc0fa68b0jpeg.jpeg">
                    <div slot="placeholder" class="image-slot">
                        加载中<span class="dot">...</span>
                    </div>
                    <div slot="error" class="image-slot">
                        <i class="el-icon-picture-outline"></i>
                    </div>
                </el-image>
            </el-col>
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
        data(){
            return{
                btnStat:"blue",
            };
        },
        methods:{
            onStarClick(event){
              console.log("click",event.target.c);
                if(this.btnStat=='red'){
                    this.btnStat='gray';
                }else {
                    this.btnStat='red';
                }
            },
        }
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
        padding: 1px 0px 0px 10px;
        font-size: 18px;
        font-weight: bold;
        color: darkgray;
    }
    #index #index-text{
        display: block;
        text-align: center;
            width: 20px;
            height: auto;
            border-radius: 50%;
        border: 1px solid darkgray;
    }

    #star {
        height: 50px;
    }
    #star .el-button--text{
         /*border-color:red;*/
        /*padding-left: 5px;*/
        /*padding-right: 5px;*/
        /*padding-top: 0px;*/
        /*padding-bottom: 26px;*/
        font-size: 25px;
        padding: 0px 5px 26px 5px;
        margin-top: -8px
    }
    .icon-red{
        color: #F56C6C;
    }
    .icon-gray{
        color: #909399;
    }
    .icon-black{
        color: #333333;
    }
    #time{
        font-size: 12px;
        color:grey;
        margin-left: 14px;
    }

    #name{
        font-weight:bold;
        text-overflow:ellipsis;
        white-space:nowrap;
        overflow:hidden;
        margin-bottom: 2px;
        margin-top: 2px;
    }
    #name:hover:before{
        cursor: help;
        content:attr(alt);


        width: auto;
        background-color: rgba(0, 0, 0, 0.7);
        font-size: 12px;
        font-weight: normal;
        line-height: 15px;
        padding: 8px 10px;
        color: #fff;
        position: absolute;
        z-index: 10001;
        -webkit-border-radius: 3px;
        -moz-border-radius: 3px;
        border-radius: 3px;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        box-sizing: border-box;
        text-align: center;

        top: 25px;
        /*margin-top: 20px;*/
        /*right: 0px;*/
        left: 20%;
        }

    #name:hover:after {
        /*content: "";*/
        /*position: absolute;*/
        /*left: 0%;*/
        /*width: 0;*/
        /*height: 0;*/
        /*border-right: 8px solid #d9444a;*/
        /*border-top: 8px solid transparent;*/
        /*border-bottom: 8px solid transparent;*/

        font-size: 14px;
        font-weight: normal;
        line-height: 14px;
        color: #fff;
        text-align: center;

        content: '';
        position: absolute;
        width: 0;
        height: 0;
        border-style: solid;

        border-width: 0 9px 10px 9px;
        border-color: transparent transparent rgba(0, 0, 0, 0.7) transparent;
        top: 15px;
        /*left: 50%;*/
        margin-left: -9px;

        right: auto;
        left: 30%;
        margin-right: 9px;
    }

    #img .el-image{
        width: 100%;
        height: 120px;
        background: rgba(99, 99, 99, 0.2);

        position: relative;
        display: inline-block;
        overflow: hidden;

        margin-top: 4px;
        margin-bottom: 4px;
    }

    #img .image-slot {
        font-size: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
        height: 100%;
        background: rgba(250, 250, 250, 0.3);
        color: #909399;
    }
     #img .el-icon-picture-outline{
         font-size: 40px;
     }



</style>

<style>
   .el-icon-star-on {
       font-size: 22px;
    }
</style>