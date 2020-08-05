<template>
    <div id="progress-main" >
        <div id="progress"  ref="progress_ref">
            <el-progress type="circle" :percentage="percentage" :status="status" :width=width :stroke-width=stroke :show-text="show_text"></el-progress>
            <el-button id="refresh-btn-large" v-show="has_error" icon="el-icon-refresh" @click="refresh()" circle> </el-button>
        </div>
    </div>

</template>

<script>
    export default {
        name: "imgLoadingProgress",
        props: {'successCallback':Function,'errorCallback':Function},
        data(){
          return{
              current_request_add: null,
              stroke:12,
              width:145,
              status:null,
              count:0,
              percentage:0,
              has_error:false,
              show_text:true,
              success_delay:2500,
              items:[{"index":0,"type":"0","cover":"http://127.0.0.1:90/imgs/1.jpg","src":"http://127.0.0.1:90/v/1.mp4"},
                {"index":1,"type":"1","cover":"http://127.0.0.1:90/imgs/2.jpg","src":"http://127.0.0.1:90/v/2.mp4"},
                {"index":2,"type":"1","cover":"http://127.0.0.1:90/imgs/3.gif","src":"http://127.0.0.1:90/v/3.mp4"}]
          }
        },
        methods: {
            re_init(){
                this.status = null
                this.count = 0
                this.percentage = 0
                this.has_error = false
                this.show_text = true
                this.current_request_add = null
            },
            async update() {
                while (!this.has_error) {
                    if (this.percentage < Math.round((this.count / this.items.length) * 100)) {
                        let step = Math.random()
                        if (this.percentage + step > 100) {
                            this.percentage = 100
                            this.status="success"
                            return
                        }
                        //fuck js 的浮点精度
                        this.percentage = Math.round( (step+this.percentage)*100)/100
                        await sleep(10)
                    } else {
                        await sleep(100)
                    }
                }
            },
            progress_remove() {
                this.$refs.progress_ref.parentNode.removeChild(this.$refs.progress_ref)
            },
            start(api_src) {
                this.re_init()
                this.update()
                this.current_request_add = api_src
                console.log("start")
                this.network.get_request(this.current_request_add,
                    (res) => {
                        this.items = res.body
                        this.download(this.items)
                    },
                    (er) => {
                        this.status = "exception"
                        this.$message({
                            message: '网络错误，请重新加载',
                            center: true,
                            showClose: true,
                            type: 'error'
                        });
                        this.has_error = true
                        this.show_text = false
                        this.errorCallback()
                    }
                )

            },
            download(items){
                for (let [index, item] of items.entries()) {
                    sleep(1000 * index).then(() => {
                        let img = new Image()
                        img.src = item.cover
                        img.onload = (e) => {
                            if (this.count == items.length - 1) {
                                console.log("加载OK： ", index + ' : ' + e.target.src)
                                console.log("全部完成")
                                sleep(this.success_delay).then(() => {
                                    this.successCallback(items)
                                })
                            } else {
                                console.log("加载OK： ", index + ' : ' + e.target.src)
                            }
                            this.count++
                        }
                        img.onloadstart = (e) => {
                            console.log("开始下载：", index + ' : ' + e.target.src)
                        }
                        img.onerror = (e) => {
                            console.log("error：", e.target.src)
                            this.status = "exception"
                            this.$message({
                                message: '网络错误，请重新加载',
                                center: true,
                                showClose: true,
                                type: 'error'
                            });
                            this.has_error = true
                            this.show_text = false
                            this.errorCallback()
                        }
                    })
                }
            },
            refresh(){
                this.start(this.current_request_add)
            }

        },
        mounted() {

        }
    }

    let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));



</script>

<style scoped>
    #progress-main{
        width: 100%;
        height: 100%;
        background-color: transparent;
        display: flex;
        justify-content: center;
        align-items:center;
    }
    #progress{
        width: auto;
        height: auto;
    }

    #refresh-btn-large {
        position: absolute;
        z-index: 2;
        left: 50%;
        top: 50%;

        height: 160px;
        width: 160px;
        margin-top: -80px;
        margin-left: -80px;
        background-color: transparent;
        font-size: 50px;
        border: transparent;
        font-weight: bold;
        opacity: 0.4;
        color: #F56C6C;
    }

</style>