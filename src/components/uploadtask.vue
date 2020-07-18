<template>
    <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="8" id="task-setting" class="grid-content bg-purple">
            <el-form ref="form" :model="form" :rules="rules" label-width="80px" size="medium" status-icon>
                <el-row id="params-setting-row">
                    <el-col style="width: 40%" >
                        <el-form-item label="FPS" prop="fps" >
                            <el-input v-model.number="form.fps" placeholder="帧率" style="width: 90%;"></el-input>
                        </el-form-item>

                        <el-form-item label="总帧数" prop="frames">
                            <el-input v-model.number="form.frames" placeholder="视频长度"  style="width: 90%;"></el-input>
                        </el-form-item>

                        <el-form-item label="扫描行" prop="scan">
                            <el-input v-model.number="form.scan" placeholder="视频高度" style="width: 90%;"></el-input>
                        </el-form-item>

                        <div style="width: 100%;display: flex; justify-content: center">
                            <el-button type="primary" size="mini" class="submit" @click="onSubmitForm('form')">提交任务</el-button>
                        </div>
                    </el-col>

                    <el-col style="width: 60%" >
                        <el-collapse v-model="active_item">
                            <div class="more-videos" v-for="(postfix_, index) in form.postfix">

                                <el-collapse-item class="video-head" :title="'视频'+(index+1)" :name="index">

                                <el-form-item label="名称后缀" :prop="`postfix[${index}]`"  :rules="{required:true, message:'请输入视频名称后缀', trigger: 'change' }">
                                    <el-input v-model="form.postfix[index]" placeholder="名称后缀"
                                              maxlength="12" show-word-limit
                                              style="width: 90%;min-width: 110px;"></el-input>
                                    <el-button class="del-video-btn" type="text" icon="el-icon-delete" @click="onDelVideo(index)"></el-button>
                                </el-form-item>

                                <el-form-item label="轨道深度" style="height: 30px;"  :prop="`track[${index}]`" :rules="{ required:true, trigger: 'blur' }">
                                    <el-input id="zoomx-input" v-model="form.track[index]" style="display: none"></el-input>
                                    <el-col :span="7">
                                        <el-form-item :prop="`zoomx[${index}]`" :rules="{validator: zoomValidator, trigger: 'change' }">
                                        <el-input id="zoomx-input" v-model="form.zoomx[index]" placeholder="X"
                                                  oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                                  style="min-width: 50px; padding-left: 0px"></el-input>
                                            </el-form-item>
                                    </el-col>
                                    <el-col :span="7">
                                        <el-form-item :prop="`zoomy[${index}]`" :rules="{ validator: zoomValidator, trigger: 'change' }">
                                        <el-input id="zoomy-input" v-model="form.zoomy[index]" placeholder="Y"
                                                  oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                                  style="min-width: 50px;"></el-input>
                                            </el-form-item>
                                    </el-col>
                                    <el-col :span="7">
                                        <el-form-item :prop="`zoomz[${index}]`" :rules="{ validator: zoomValidator, trigger: 'change' }">
                                        <el-input id="zoomz-input" v-model="form.zoomz[index]" placeholder="Z"
                                                  oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                                  style="min-width: 50px;"></el-input>
                                            </el-form-item>
                                    </el-col>
                                </el-form-item>

                                <el-form-item label="拍摄轨道" :prop="`track[${index}]`" >
                                    <!--<el-input v-model="form.track[index]" placeholder="请输入内容" style="width: 90%;"></el-input>-->
                                    <el-radio-group v-model="form.track[index]" size="mini" @change="((value)=>{onHandleRadio(value, postfix_, index)})"
                                                    style="width: 95%;min-width: 158px;">
                                        <el-radio class="params-setting-track-radio" label="double-straight-line" border>
                                            Dolly-Zoom
                                        </el-radio>
                                        <el-radio class="params-setting-track-radio" label="straight-line" border>
                                            Straight
                                        </el-radio>
                                        <el-radio class="params-setting-track-radio" label="circle" border>Circle
                                        </el-radio>
                                    </el-radio-group>
                                </el-form-item>
                            </el-collapse-item>
                            </div>
                        </el-collapse>
                        <div style="width: 100%;display: flex; justify-content: left">
                            <el-button plain size="mini" class="add-video" @click="onAddVideo">添加视频</el-button>
                        </div>
                    </el-col>
                </el-row>
            </el-form>

        </el-col>
        <el-col :span="15" id="task-fileupload" class="grid-content bg-purple-light">
              <div class="border-wrapper">
			<div class="border-top"></div>
			<div class="border-left"></div>
			<div class="border-bottom"></div>
			<div class="border-right"></div>
		    <div class="content-wrapper">
            <el-upload
                    name="img"
                    class="upload-file"
                    ref="uploadimg"
                    :action=this.backen.upload_img_urlmaker()
                    :before-upload="onHandleBeforeUpload"
                    :on-preview="onHandlePreview"
                    :on-remove="onHandleRemove"
                    :before-remove="beforeRemove"
                    :on-error="onHandleError"
                    :on-success="onHandleSuccess"
                    multiple
                    drag
                    :limit="6"
                    :on-exceed="onHandleExceed"
                    :file-list="fileList"
                    list-type="picture">
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
                <div class="el-upload__text">支持jpg/png/bmp，最大5M，不多于6个文件</div>

            </el-upload>
                </div>
                  </div>
        </el-col>
    </el-row>


</template>

<script>
    export default {
        name: "uploadtask",
        data() {
            let validatorFrames = (rule, value, callback) => {
                if(!Number.isInteger(value)){
                    callback(new Error('必须为整数'))
                }
                if (value < this.form.fps*5 ) {
                    callback(new Error('总帧数 >= fps*5'));
                }
                callback();
            };
            return {
                // [{name,url}]
                active_item:[0],
                fileList: [],
                limit_flag: false,
                form: {
                    goods:[],
                    fps: 24,
                    frames: 240,
                    scan: 166,
                    postfix: ['Dolly-Zoom'],
                    zoomx: [0.1],
                    zoomy: [0.1],
                    zoomz: [0.1],
                    track: ['double-straight-line']
                },
                rules: {
                    fps: [
                        {required: true, message: '请输入帧率', trigger: 'change'},
                        {type:'number',message: '必须为数字值', trigger: 'change'},
                        {validator(rule, value, callback) {if(!Number.isInteger(value) || value<5 || value>60){callback(new Error('限制5~60帧/秒'))};callback();}, trigger: 'change'}
                    ],
                    frames:[
                        {required: true, message: '总帧数=fps*视频时长', trigger: 'change'},
                        // {type:'number',message: '必须为数字值', trigger: 'blur'},
                        {validator: validatorFrames, trigger: 'change'}
                    ],
                    scan:[
                        {required: true, message: '请输入视频高度', trigger: 'change'},
                        {type:'number',message: '必须为数字值', trigger: 'change'},
                        {validator(rule, value, callback) {if(!Number.isInteger(value) || value<160 || value>1080){callback(new Error('限制160~1080整数'))};callback();}, trigger: 'change'}
                    ],
                    label_star:[
                        {required: true, trigger: 'none'},
                    ],
                }
            };
        },
        beforeRouteLeave(to, from, next) {
            if(this.$refs.uploadimg.uploadFiles.length > 0){
                if (window.confirm('有设置未提交，是否确认离开')) {next()} else {next(false)}
            }else {
                next()
            }

        },
        methods: {
            onHandleBeforeUpload(file) {
                const is_in_condition = (file.type === 'image/jpeg') || (file.type === 'image/png') || (file.type === 'image/bmp');
                const is_in_5M = file.size / 1024 / 1024 < 5;
                if (!is_in_condition) {
                    this.$message.error('上传图片格式非法，请注意限制!');
                    this.limit_flag = true
                }
                if (!is_in_5M) {
                    this.$message.error('上传图片大小不能超过 5MB!');
                    this.limit_flag = true
                }
                return is_in_condition && is_in_5M;
            },
            onHandleSuccess(response, file, fileList) {
                // fileList.push({'name':file.response.origin, 'remote_name':file.response.save_name})
                console.log('handleSuccess:',file);
            },
            onHandleError(err, file, fileList) {
                this.$message.error('上传图片失败!请检查网络');
                console.log('handleError:',err);
            },
            onHandlePreview(file) {
                console.log(this.$refs.uploadimg.uploadFiles);
                console.log('handlePreview:', file);
            },
            onHandleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 6 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            beforeRemove(file, fileList) {
                if(this.limit_flag){
                    this.limit_flag = false
                    return true
                }
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            onHandleRemove(file, fileList) {
                console.log('handleRemove:', file);
            },
            onAddVideo(){
               this.form.zoomx.push(3.0);
               this.form.zoomy.push(3.0);
               this.form.zoomz.push(3.0);
               this.form.track.push('circle');
               this.form.postfix.push('');
               this.active_item.push(this.form.postfix.length-1)
            },
            onDelVideo(index){
                if(this.form.postfix.length<=1){
                    this.$message.warning('至少要生成一个视频');
                    return;
                }
                this.form.zoomx.splice(index, 1);
                this.form.zoomy.splice(index, 1);
                this.form.zoomz.splice(index, 1);
                this.form.track.splice(index, 1);
                this.form.postfix.splice(index, 1);
                this.active_item = this.active_item.filter((x) => x != index)
            },
            onHandleRadio(value, postfix, index){
                if(postfix == '' || postfix == null || postfix == 'Dolly-Zoom' || postfix == 'Straight' || postfix == 'Circle') {
                    if (value == 'double-straight-line'){this.$set(this.form.postfix,index,'Dolly-Zoom')}//this.form.postfix[index]='Dolly-Zoom'
                    if (value == 'straight-line'){this.$set(this.form.postfix,index,'Straight')}//this.form.postfix[index]='Straight'
                    if (value == 'circle'){this.$set(this.form.postfix,index,'Circle')} //this.form.postfix[index]='Circle'
                    //this.$forceUpdate();
                }
            },
            zoomValidator(rule, value, callback) {
                if (value == "") {
                    callback(new Error('禁止为空'));
                }
                if (value >= 1 ||  value <= -1) {
                    callback(new Error('（-1，+1）'));
                }
                callback();
            },
            onSubmitForm(formName) {
                if (this.$refs.uploadimg.uploadFiles.length == 0){
                    this.$message.warning("请先准备好要处理的图片")
                    return false
                }
                this.form.goods.splice(0)
                this.$refs.uploadimg.uploadFiles.forEach((value, index, array)=> {
                    this.form.goods.push(value.response['save_name'])
                })
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        const loading = this.$loading({
                          lock: true,
                          text: '正在上传，请稍后',
                          // spinner: 'el-icon-loading',
                          background: 'rgba(0, 0, 0, 0.6)',
                          target: document.querySelector('.el-main')
                        });
                        // setTimeout(() => {
                        //   loading.close();
                        // }, 10000);
                        this.network.post_request(this.backen.upload_tasks(),
                            JSON.stringify(this.form),
                            (res) => {
                                console.log(res);
                                console.log("network sucess");
                                loading.close();
                            },
                            (er) => {
                                this.$message({
                                    message: '网络错误，请重新加载',
                                    center: true,
                                    showClose: true,
                                    type: 'error'
                                });
                                loading.close();
                            }
                        )
                    }
                });
            },

        }

    }
</script>

<style scoped>
    .el-col {
        height: 100%;
        border-radius: 4px;
    }

    #task-setting {
        /*background-color: teal;*/
        min-width: 420px;
        /*display: flex;*/
        /*justify-content: center;*/
        /*align-items: center;*/
    }

    #params-setting-row{
        position: relative;
        padding-top: 24px;
        padding-bottom: 24px;
    }
    .el-form{
        width: 100%;
    }

    .el-form-item {
        margin-bottom: 22px;
    }
    .more-videos{
        width: 95%;
        border: 1px solid #409EFF;
        margin-bottom: 14px;
    }
    .video-head{
        /*text-align: center;*/
        /*border: 1px solid darkgray;*/
        /*color: gray;*/
        /*margin-bottom: 10px;*/
        background-color: transparent;
    }
    .del-video-btn{
        position: absolute;
        color: #E6A23C;
        font-size: medium;
    }

    .el-collapse{
        border-top:unset;
        border-bottom:unset;
    }

    .el-radio.is-bordered.params-setting-track-radio{
        width: 100%;
        min-width: 148px;
        margin-left: 0px;
        margin-bottom: 3px;
        margin-right: 0px;
    }

    .el-radio.is-bordered{
        border: 1px solid #f4f4f5;
    }

    .el-radio.is-bordered.is-checked {
        border-color: #409EFF;
    }
    .add-video{
        width: 96%;
        min-width: 240px;
        margin-top: -12px;
        color: #a0cfff;
        border-color: #a0cfff;
    }



    #task-fileupload {
        min-width: 380px;
        /*background-color: tomato;*/
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
    .row-bg {
    padding: 0px 0;
    background-color: transparent!important;
  }

    .upload-file{
        height: 100%;

        /*background-color:blue;*/
    }

    .border-wrapper {
        position: relative;
        width: 100%;
        height: 100%;
        background: grey;
        z-index: 90;
        border-radius: 10px;
    }

    .border-top {
        width: calc(100% - 20px);
        left: 10px;
        height: 2px;
        background-image: linear-gradient(to right, #fff 0%, #fff 30%, transparent 50%);
        background-size: 20px 2px;
        background-repeat: repeat-x;
        position: absolute;
    }

    .border-left {
        width: 2px;
        left: 0;
        top: 10px;
        height: calc(100% - 20px);
        background-image: linear-gradient(to top, #fff 0%, #fff 30%, transparent 50%);
        background-size: 2px 20px;
        background-repeat: repeat-y;
        position: absolute;
    }

    .border-bottom {
        width: calc(100% - 20px);
        left: 10px;
        height: 2px;
        bottom: 0;
        background-image: linear-gradient(to right, #fff 0%, #fff 30%, transparent 50%);
        background-size: 20px 2px;
        background-repeat: repeat-x;
        position: absolute;
    }

    .border-right {
        width: 2px;
        right: 0;
        top: 10px;
        height: calc(100% - 20px);
        background-image: linear-gradient(to top, #fff 0%, #fff 30%, transparent 50%);
        background-size: 2px 20px;
        background-repeat: repeat-y;
        position: absolute;
    }

    .content-wrapper {
        position: relative;
        width: calc(100% - 4px);
        height: calc(100% - 4px);
        border-radius: 10px;
        /*background: #ffffff;*/
        background: #e5e9f2;
        top: 2px;
        left: 2px;
    }



</style>

<style>
    .el-upload{
        display:flex;
    }
    .el-upload-dragger {
        width: 100%;
        height: 200px;
        background-color: transparent;
    }
    .el-collapse-item__header {
        padding-left: 45%;
        color: #409EFF;
    }
    .el-collapse-item__wrap{
        background-color: unset;
        border-bottom: unset;
    }
    .el-collapse-item__header{
        height: 28px;
        line-height:28px;
        border-bottom-color: #409EFF;
    }
    .el-collapse-item__content{
        margin-top: 14px;
        padding-bottom: 2px;
    }

    #zoomx-input ,#zoomy-input ,#zoomz-input {
        padding-left: 3px;
        padding-right: 3px;
        text-align: center;
    }

    .el-input__suffix{
        right: -4px;
    }

    .el-input .el-input__count .el-input__count-inner{
        background-color: transparent;
    }

</style>