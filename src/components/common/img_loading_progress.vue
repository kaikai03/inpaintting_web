<template>
    <div id="progress_main" >
        <div id="progress"  ref="progress_ref">
            <el-progress type="circle" :percentage="percentage" :status="status" :width=width :stroke-width=stroke ></el-progress>
        </div>
    </div>

</template>

<script>
    export default {
        name: "img_loading_progress",
        props: {'success_callback':Function,'error_callback':Function},
        data(){
          return{
              stroke:12,
              width:145,
              status:null,
              count:0,
              percentage:0,
              has_error:false,
              playitems:[{"index":1,"type":"0","img":"http://127.0.0.1:90/imgs/1.jpg","media":"http://127.0.0.1:8020/mv/mv1.mp4"},
                {"index":2,"type":"1","img":"http://127.0.0.1:90/imgs/2.jpg","media":"http://127.0.0.1:8020/gif/gif1.gif"},
                {"index":3,"type":"1","img":"http://127.0.0.1:90/imgs/3.gif~","media":"http://127.0.0.1:8020/gif/gif3.gif"}]
          }
        },
        methods: {
            re_init(){
                this.status = null
                this.count = 0
                this.percentage = 0
                this.has_error = false
            },
            async update() {
                while (!this.has_error) {
                    if (this.percentage < Math.round((this.count / this.playitems.length) * 100)) {
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
            remove() {
                this.$refs.progress_ref.parentNode.removeChild(this.$refs.progress_ref)
            },
            start(src) {
                // TODO:之后，替换掉静态的this.playitems
                this.re_init()
                this.update()
                console.log("start")
                for (let [index, item] of this.playitems.entries()) {
                    sleep(1000 * index).then(() => {
                        let img = new Image()
                        img.src = item.img
                        img.onload = (e) => {
                            if (this.count == this.playitems.length - 1) {
                                console.log("加载OK： ", index + ' : ' + e.target.src)
                                console.log("全部完成")
                                sleep(2500).then(() => {
                                    this.success_callback(this.playitems)
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
                            this.error_callback()
                        }
                    })
                }
            }

        },
        mounted() {

        }
    }

    let sleep = (time) => new Promise((resolve) => setTimeout(resolve, time));



</script>

<style scoped>
    #progress_main{
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

</style>