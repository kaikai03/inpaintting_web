<template>
    <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="8" id="task-setting" class="grid-content bg-purple">

            <el-form ref="form" :model="form" label-width="80px" size="medium">
                <el-row id="params-setting-row">
                    <el-col style="width: 40%" >
                        <el-form-item label="FPS">
                            <el-input v-model.number="form.fps" placeholder="请输入内容" style="width: 90%;"></el-input>
                        </el-form-item>

                        <el-form-item label="总帧数">
                            <el-input v-model.number="form.frames" placeholder="请输入内容" style="width: 90%;"></el-input>
                        </el-form-item>

                        <el-form-item label="扫描行">
                            <el-input v-model.number="form.scan" placeholder="请输入内容" style="width: 90%;"></el-input>
                        </el-form-item>
                    </el-col>

                    <el-col style="width: 60%" >
                        <el-collapse v-model="active_item">
                            <div class="more_videos" v-for="(postfix, index) in form.postfix">

                                <el-collapse-item class="video_head"  :title="'视频'+(index+1)" :name="index">

                                <el-form-item label="名称后缀">
                                    <el-input v-model="form.postfix[index]" placeholder="视频文件的tag" :ref="'postfix'+index"
                                              maxlength="8" show-word-limit
                                              style="width: 90%;min-width: 110px;"></el-input>
                                    <el-button class="del_video_btn" type="text" icon="el-icon-delete" @click="del_video(index)"></el-button>
                                </el-form-item>

                                <el-form-item label="轨道深度">
                                    <el-input v-model="form.zoomx[index]" placeholder="X" oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                              style="width: 30.5%;min-width: 50px;"></el-input>
                                    <el-input v-model="form.zoomy[index]" placeholder="Y" oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                              style="width: 30.5%;min-width: 50px;"></el-input>
                                    <el-input v-model="form.zoomz[index]" placeholder="Z" oninput="if(isNaN(value)) { value = null } if(value.indexOf('.')>0){value=value.slice(0,value.indexOf('.')+4)}"
                                              style="width: 30.5%;min-width: 50px;"></el-input>
                                </el-form-item>

                                <el-form-item label="拍摄轨道">
                                    <!--<el-input v-model="form.track[index]" placeholder="请输入内容" style="width: 90%;"></el-input>-->
                                    <el-radio-group v-model="form.track[index]" size="mini"
                                                    style="width: 95%;min-width: 158px;">
                                        <el-radio class="params-setting-track-radio" label="double-straight-line" border>
                                            dolly
                                        </el-radio>
                                        <el-radio class="params-setting-track-radio" label="straight-line" border>
                                            straight
                                        </el-radio>
                                        <el-radio class="params-setting-track-radio" label="circle" border>circle
                                        </el-radio>
                                    </el-radio-group>
                                </el-form-item>
                            </el-collapse-item>
                            </div>
                        </el-collapse>
                        <div style="width: 100%;display: flex; justify-content: left">
                            <el-button type="primary" size="mini" class="add_video" @click="add_video">添加视频</el-button>
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
                    :before-upload="before_upload"
                    :on-preview="handle_preview"
                    :on-remove="handle_remove"
                    :before-remove="before_remove"
                    :on-error="handle_error"
                    :on-success="handle_success"
                    multiple
                    drag
                    :limit="6"
                    :on-exceed="handle_exceed"
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
            return {
                // [{name,url}]
                active_item:[0],
                fileList: [],
                limit_flag: false,
                form: {
                    fps: 24,
                    frames: 240,
                    scan: '',
                    postfix: [''],
                    zoomx: [0.1],
                    zoomy: [0.1],
                    zoomz: [0.1],
                    track: ['double-straight-line','straight-line']
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
            before_upload(file) {
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
            handle_success(response, file, fileList) {
                // fileList.push({'name':file.response.origin, 'remote_name':file.response.save_name})
                console.log('handleSuccess:',file);
            },
            handle_error(err, file, fileList) {
                console.log('handleError:',err);
            },
            handle_preview(file) {
                console.log(this.$refs.uploadimg.uploadFiles);
                console.log('handlePreview:', file);
            },
            handle_exceed(files, fileList) {
                this.$message.warning(`当前限制选择 6 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            before_remove(file, fileList) {
                if(this.limit_flag){
                    this.limit_flag = false
                    return true
                }
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            handle_remove(file, fileList) {
                console.log('handleRemove:', file);
            },
            add_video(){
               this.form.zoomx.push(3.0);
               this.form.zoomy.push(3.0);
               this.form.zoomz.push(3.0);
               this.form.track.push('circle');
               this.form.postfix.push('');
               this.active_item.push(this.form.postfix.length-1)
            },
            del_video(index){
                console.log(this.active_item,index)
                this.form.zoomx.splice(index, 1);
                this.form.zoomy.splice(index, 1);
               this.form.zoomz.splice(index, 1);
               this.form.track.splice(index, 1);
               this.form.postfix.splice(index, 1);
                this.active_item = this.active_item.filter((x) => x != index)
            }

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
    .more_videos{
        width: 95%;
        border: 1px solid #409EFF;
        margin-bottom: 14px;
    }
    .video_head{
        /*text-align: center;*/
        /*border: 1px solid darkgray;*/
        /*color: gray;*/
        /*margin-bottom: 10px;*/
        background-color: transparent;
    }
    .del_video_btn{
        position: absolute;
        color: #E6A23C;
        font-size: larger;
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
    .add_video{
        width: 93%;
        min-width: 240px;
        /*margin-top: -20px;*/
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
        z-index: 9999;
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

</style>