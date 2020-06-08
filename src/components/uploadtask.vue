<template>
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
            :limit="10"
            :on-exceed="handle_exceed"
            :file-list="fileList"
            list-type="picture">
        <el-button size="small" type="primary"><i class="el-icon-upload"></i></el-button>
        <div slot="tip" class="el-upload__tip">支持jpg/png/bmp，最大5M</div>
    </el-upload>

</template>

<script>
    export default {
        name: "uploadtask",
        data() {
            return {
                // [{name,url}]
                fileList: [],
                limit_flag:false
            };
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
                this.$message.warning(`当前限制选择 10 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
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
            }

        }
    }
</script>

<style scoped>

</style>