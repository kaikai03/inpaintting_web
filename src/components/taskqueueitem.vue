<template>
    <div :class="{'queue-item':1, 'queue-item-queuing':workState.que==starStat,
                                   'queue-item-high':workState.hi==starStat,
                                  'queue-item-low':workState.low==starStat,
                                  'queue-item-stop':workState.stop==starStat }">

        <div class="del-btn" :style="{'visibility':delBtnVisibility}" >
            <el-button type="text" @click="onDelConfirm">
                <i class="el-icon-error"></i>
            </el-button>
        </div>

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
                        v-model="popVisible"
                        placement="bottom"
                        width="100"
                        trigger="click">
                      <div id="pop">
                        <el-button  type="text" @click="onStarClick(workState.que)" >
                            <i class="el-icon-star-on icon-blue"></i> <div class="pop-btn-text icon-blue">正常</div>
                        </el-button>
                        <el-button  type="text" @click="onStarClick(workState.hi)" >
                            <i class="el-icon-star-on icon-red"></i><span class="pop-btn-text icon-red">插队</span>
                        </el-button>
                          <el-button  type="text" @click="onStarClick(workState.low)" >
                            <i class="el-icon-star-on icon-gray1"></i><span class="pop-btn-text icon-gray1">滞后</span>
                        </el-button>
                          <el-button  type="text" @click="onStarClick(workState.stop)" >
                            <i class="el-icon-star-off icon-gray2"></i><span class="pop-btn-text icon-gray2">暂停</span>
                        </el-button>
                      </div>
                    <el-button class="star" type="text" slot="reference" >
                        <i :class="{'el-icon-star-on':1, 'icon-blue':workState.que==starStat,
                                                         'icon-red':workState.hi==starStat,
                                                          'icon-gray1':workState.low==starStat,
                                                          'icon-gray2':workState.stop==starStat }">
                        </i>
                    </el-button>
                </el-popover>
            </el-col>
            <el-col :span="20" id="img">
<!--                'fill', 'contain', 'cover', 'none', 'scale-down'-->
                <el-image id="image" fit="contain" lazy
                        :src="imgAddr">
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
    let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));
    export default {
        name: "queueItem",
        props: {'index':Number,'name':String,'imgName':String,'progress':Number, 'stat':String, 'time':String, 'taskID':String, 'delCallback':Function[Number]},
        data(){
            return{
                imgAddr:this.backen.imgUrlmaker(this.imgName),
                workState:this.backen.work_stat,
                starStat:this.stat,
                popVisible:false,
                isActive:false,

            };
        },
        computed:{
            delBtnVisibility:{
                // 使用visibility防止相对位置的改变
                get(){
                    if (this.isActive){
                        return 'hidden'
                    }else {
                        return 'visible'
                    }
                }
            }
        },
        methods: {
            onStarClick(stat) {
                console.log(stat)
                this.popVisible = false
                if (this.progress != 0 && this.workState.que == this.stat) {
                    this.$message.error('进行中的任务无法更改列队级别');
                    return;
                }
                if (this.starStat != stat) {
                    //TODO: send command to backen to change the work stat
                    this.changeStatus(stat)
                }

            },
            onDelConfirm() {
                //TODO:to implement
                this.$confirm('确定要这个删除任务？？', 'are you sure', {
                    iconClass:'el-icon-error',
                    confirmButtonText: '坚决删除',
                    cancelButtonText: '不的',
                    type: 'warning',
                    confirmButtonClass:'del-confirm-btn',
                    cancelButtonClass:'del-confirm-btn'
                }).then(() => {
                    const loading = this.$loading({
                          lock: true,
                          text: '正在执行删除指令，请稍后',
                          // spinner: 'el-icon-loading',
                          background: 'rgba(0, 0, 0, 0.6)',
                          target: document.querySelector('#id-'+this.taskID)
                        });
                    this.network.post_request(this.backen.taskDrop(),
                            JSON.stringify({'task_codes':[this.taskID], 'work_status':this.starStat}),
                            (res) => {
                                console.log(res);
                                console.log("del success");
                                sleep(1500).then(() => {
                                    this.$message({message: '任务成功删除', center: true, showClose: true, type: 'success',effect:"dark"});
                                    loading.close();
                                    //此处不延迟的话，会与load的动画互相干扰，不会显示淡出效果
                                    sleep(600).then(() => {
                                        this.delCallback(this.index)
                                    })

                                })
                            },
                            (er) => {
                                console.log(er)
                                sleep(1500).then(() => {
                                    if(er.status == 507 || er.status == 500){
                                        this.$message({message: '服务器存储错误，请刷新页面', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else if(er.status == 406) {
                                        this.$message({message: '任务ID存在问题，请联系管理员', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else if(er.status == 422) {
                                        this.$message({message: '参数错误，请联系管理员', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else {
                                        this.$message({message: '网络错误，请重新加载', center: true, showClose: true, type: 'error' });
                                    }
                                    loading.close();
                                })

                            }
                        )

                }).catch(() => {
                    this.$message({type: 'info', message: '删除--取消'});
                });
            },
            changeStatus(status){
                const loading = this.$loading({
                          lock: true,
                          text: '状态修改中，请稍后',
                          // spinner: 'el-icon-loading',
                          background: 'rgba(0, 0, 0, 0.6)',
                          target: document.querySelector('#id-'+this.taskID)
                        });
                this.network.post_request(this.backen.taskStatusChange(),
                            JSON.stringify({'doc_code':this.taskID, 'changeto_status':status}),
                            (res) => {
                                console.log(res);
                                console.log("change success");
                                sleep(1500).then(() => {
                                    this.$message({message: '任务状态已改变', center: true, showClose: true, type: 'success',effect:"dark"});
                                    this.starStat = status;
                                    loading.close();
                                })

                            },
                            (er) => {
                                console.log(er)
                                sleep(1500).then(() => {
                                    if(er.status == 507 || er.status == 500){
                                        this.$message({message: '服务器存储错误，请刷新页面', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else if(er.status == 406) {
                                        this.$message({message: '任务ID存在问题，请联系管理员', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else if(er.status == 422) {
                                        this.$message({message: '参数错误，请联系管理员', center: true, showClose: true, type: 'error',effect:"dark"});
                                    }else {
                                        this.$message({message: '网络错误，请重新加载', center: true, showClose: true, type: 'error' });
                                    }
                                    loading.close();
                                })

                            }
                        )
            }
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
        border: 1px solid #409EFF;
    }

    .del-btn{
        position: relative;
        float: right;
        right: -5px;
        top: 0px;
        height: 24px;
        width: 24px;
        /*background: red;*/

    }

    .del-btn .el-button{
        height: 100%;
        width:100%;
    }

     .del-btn .el-button--text{
        font-size: 20px;
         padding: 0px;
         color: #909399;
         opacity: 0.4;
    }

    .queue-item-queuing{
        background: #EDF6FF;
    }

    .queue-item-high{
        background: #FDE2E2;
    }

    .queue-item-low{
        background: #F2F2F2;
    }

    .queue-item-stop{
        background: #F2F2F2;
        opacity: 0.6;
    }

    #index{
        padding: 8px 0px 0px 8px;
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
        border: 1px dashed #409EFF40;
    }



    #star {
        height: 50px;
    }
    #star .el-button--text{
        font-size: 25px;
        padding: 5px 8px 26px 5px;
        margin-top: -8px
    }

    .el-popover #pop .el-button{
        float: right;
        width: 100%;
        padding: 5px 0px;
    }

    .el-popover #pop .pop-btn-text{
        font-size: 14px;
        padding: 0px 1px 6px 1px;
         display: inline-block;
    vertical-align: middle;
    }



    .icon-red{
        color: #F56C6C;
    }
    .icon-gray1{
        color: #909399;
    }
    .icon-gray2{
        color: #909399;
        opacity: 0.5;
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
       font-size: 28px;
    }

    .del-confirm-btn{
        background: transparent!important;
        border: unset!important;
        color:#409EFF!important;
    }


   .el-popover .el-icon-star-on {
       font-size: 22px;
    }
   .el-popover .el-icon-star-off {
       font-size: 20px;
    }
    .el-popover[x-placement^="bottom"] {
        margin-top: -12px;
    }
    .el-popover {
        min-width: 80px;
        padding:5px;
    }
    .el-popover[style] {
        width: 80px!important;
    }



</style>