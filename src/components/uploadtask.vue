<template>
    <el-upload
            name="img"
            class="upload-file"
            ref="uploadimg"
            :action=this.backen.upload_img_urlmaker()
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :on-error="handleError"
            :on-success="handleSuccess"
            multiple
            :limit="3"
            :on-exceed="handleExceed"
            :file-list="fileList"
            list-type="picture">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>

</template>

<script>
    export default {
        name: "uploadtask",
        data() {
            return {
                // [{name,url}]
                fileList: []
            };
        },
        methods: {
            handleSuccess(response, file, fileList) {
                // fileList.push({'name':file.response.origin, 'remote_name':file.response.save_name})
                console.log('handleSuccess:',file);
            },
            handleError(err, file, fileList) {
                console.log('handleError:',err);
            },
            handlePreview(file) {
                console.log(this.$refs.uploadimg.uploadFiles);
                console.log('handlePreview:', file);
            },
            handleExceed(files, fileList) {
                this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
            },
            beforeRemove(file, fileList) {
                return this.$confirm(`确定移除 ${file.name}？`);
            },
            handleRemove(file, fileList) {
                console.log('handleRemove:', file);
            }
        }
    }
</script>

<style scoped>

</style>