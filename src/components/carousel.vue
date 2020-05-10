<template>
    <div id="carousel_main">

        <div id="progress">
            <transition mode="out-in">
                <img_loading_progress v-if="progress_show" :success_callback="add_carousel_flag" :error_callback="load_img_error" ref="progress"></img_loading_progress>
            </transition>
        </div>


        <div id="carousel">
            <transition mode="out-in">
                <el-carousel v-if="carousel_show" :autoplay="autoplay" :interval="2000" type="card" ref="carousel"
                             arrow="never" @change="((pre, next) => {change(pre, next)})">
                    <el-carousel-item v-for="(item,index) in playitems" :key="item.index" name="index">
                        <div style="height: 100%;width: 100%;" @click="clickitem(item)">
                            <div style="height: 30%;width: 30%; position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); background-color: red"
                                 @click.stop="clickplay(item)">
                                <p class="medium">{{ item }}</p>
                            </div>
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </transition>
        </div>

        <el-button id="refresh_btn_large" v-if="error_refresh_show" icon="el-icon-refresh" @click="refresh_btn_click()" circle> </el-button>

            <transition mode="out-in">
               <el-button id="refresh_btn" icon="el-icon-refresh" @click="refresh_btn_click()" circle> </el-button>
            </transition>


    </div>
</template>


<script>
    import img_loading_progress from "~/components/common/img_loading_progress";
    export default {
        name: "carousel",
        data(){
          return{
            progress_show:true,
            carousel_show:false,
              error_refresh_show:false,
            autoplay:true,
            playitems:[{"index":1,"type":"0","img":"http://127.0.0.1:90/imgs/1.jpg","media":"http://127.0.0.1:8020/mv/mv1.mp4"},
            {"index":2,"type":"1","img":"http://127.0.0.1:90/imgs/2.jpg","media":"http://127.0.0.1:8020/gif/gif1.gif"},
            {"index":3,"type":"1","img":"http://127.0.0.1:90/imgs/3.png","media":"http://127.0.0.1:8020/gif/gif3.gif"}]
          }
        },
        methods: {
            add_carousel_flag(playitems) {
                console.log(playitems)
                this.error_refresh_show = false
                this.progress_show = false
                this.carousel_show = true
            },
            load_img_error() {
                //TODO:show reflash button
                this.error_refresh_show = true
            },
            refresh_btn_click() {
                console.log("btn")
                //TODO:大刷新按钮丢到progress里面
                this.error_refresh_show = false
                this.$refs.progress.start("图片地址")
            },

            clickitem(item) {
                //this.$refs.carousel.setActiveItem(0);
                // this.$refs.carousel.next();
                console.log('clickitem:' + item.index);
                // this.$refs.carousel.interval
                if (this.autoplay == true) {
                    this.autoplay = false;
                    console.log('停止');
                } else {
                    this.autoplay = true;
                    console.log('启动');
                }
            },
            clickplay(item) {
                //this.$refs.carousel.setActiveItem(0);
                console.log('....', item.index);
                console.log('....', this.$refs.carousel.activeIndex);
                if (item.index == this.$refs.carousel.activeIndex + 1) {
                    console.log('有效点击');
                } else {
                    console.log('无效');
                }
            },
            change(pre, next) {
                console.log('change', pre, next);
            }
        },
        mounted() {
            this.$refs.progress.start("图片地址")
        },
        components:{
          img_loading_progress
        }
    }
</script>

<style>
    #carousel_main {
        height: 100%;
        width: 100%;
        position: relative;
    }

    #progress {
        height: 100%;
        width: 100%;
        position: absolute;
        background-color: black;
    }

    #carousel {
        height: 100%;
        width: 100%;
        position: absolute;
    }

    #refresh_btn_large{
        position: absolute;
        z-index: 2;
        left:50%;
        top:50%;

        height: 160px;
        width: 160px;
        margin-top: -80px;
        margin-left: -80px;
        background-color: transparent;
        font-size: 100px;
        border: transparent;
        font-weight:bold;
        opacity:0.1;
        color: #F56C6C;
    }

    #refresh_btn{
        position: absolute;
        z-index: 2;
        left:90%;
        top:80%;

        height: 60px;
        width: 60px;
        background-color: transparent;
        font-size: 40px;
        border: transparent;
        font-weight:bold;
    }

    .el-carousel {
        height: 100%;
        background-color: black;
    }

    .el-carousel--card {
        height: 90%;
        padding-top: 40px;
        padding-bottom: 0px;
        padding-left: 20px;
        padding-right: 50px;
    }

    .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 200px;
        margin: 0;
    }

    .el-carousel__indicators--outside {
        position: absolute;
        bottom: 16px;
        transform: unset;
        left: 0px;
        right: 0px;
    }

    .el-carousel__indicators--outside button {
        background-color: red;
    }

    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }

    .v-enter,
    .v-leave-to {
        opacity: 0;
        transform: scale(1.5);
    }

    .v-enter-active,
    .v-leave-active {
        transition: all 2.5s ease
    }

</style>