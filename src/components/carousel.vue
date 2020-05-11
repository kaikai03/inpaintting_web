<template>
    <div id="carousel_main">

        <div id="progress">
            <transition mode="out-in">
                <img_loading_progress v-show="progress_show" :success_callback="add_carousel_flag" :error_callback="load_img_error" ref="progress"></img_loading_progress>
            </transition>
        </div>


        <div id="carousel">
            <transition mode="out-in">
                <el-carousel v-show="carousel_show" :autoplay="autoplay" :interval="3000" type="card" ref="carousel"
                             arrow="never" @change="((pre, next) => {change(pre, next)})">
                    <el-carousel-item v-for="(item,index) in playitems" :key="item.index" name="index">
                        <div class="videoPlay" style="height: 100%;width: 100%;">
<!--                            <div style="height: 30%;width: 30%; position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); background-color: red"-->
<!--                                 @click.stop="clickplay(item)">-->
<!--                                <p class="medium">{{ item.img }}</p>-->
<!--                            <el-image :src=item.img fit="scale-down" style="height: 100%;width: 100%;"></el-image>-->
                            <video-player class="video-player vjs-custom-skin"
                                          ref="videoPlayer"
                                          :playsinline="true"
                                          :options="playerOptions"
                            ></video-player>
<!--                            </div>-->
                        </div>
                    </el-carousel-item>
                </el-carousel>
            </transition>
        </div>


            <transition mode="out-in">
               <el-button id="refresh_btn" icon="el-icon-refresh" @click="refresh_btn_click()" circle> </el-button>
            </transition>


    </div>
</template>


<script>
    import img_loading_progress from "~/components/common/img_loading_progress";
    export default {
        name: "carousel",
        data() {
            return {
                progress_show: true,
                carousel_show: false,
                autoplay: true,
                playitems: [],
                playerOptions: {
                    playbackRates: [0.7, 1.0, 1.5, 2.0], //播放速度
                    autoplay: false, //如果true,浏览器准备好时开始回放。
                    muted: false, // 默认情况下将会消除任何音频。
                    loop: false, // 导致视频一结束就重新开始。
                    preload: 'auto', // 建议浏览器在<video>加载元素后是否应该开始下载视频数据。auto浏览器选择最佳行为,立即开始加载视频（如果浏览器支持）
                    language: 'zh-CN',
                    // aspectRatio: '16:9', // 将播放器置于流畅模式，并在计算播放器的动态大小时使用该值。值应该代表一个比例 - 用冒号分隔的两个数字（例如"16:9"或"4:3"）
                    // fluid: true, // 当true时，Video.js player将拥有流体大小。换句话说，它将按比例缩放以适应其容器。
                    sources: [{
                        type: "",//这里的种类支持很多种：基本视频格式、直播、流媒体等，具体可以参看git网址项目
                        src: "http://127.0.0.1:90/v/1.mp4" //url地址
                    }],
                    poster: "http://127.0.0.1:90/imgs/1.jpg", //你的封面地址
                    // width: document.documentElement.clientWidth, //播放器宽度
                    notSupportedMessage: '此视频暂无法播放，请稍后再试', //允许覆盖Video.js无法播放媒体源时显示的默认信息。
                    controlBar: {
                        timeDivider: true,
                        durationDisplay: true,
                        remainingTimeDisplay: false,
                        fullscreenToggle: true  //全屏按钮
                    }
                }
            }
        },
        methods: {
            add_carousel_flag(playitems) {
                console.log(playitems)
                this.playitems = playitems
                this.progress_show = false
                this.carousel_show = true
                this.autoplay = true
            },
            load_img_error() {

            },
            refresh_btn_click() {
                console.log("btn")
                this.progress_show = true
                this.carousel_show = false
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



    #refresh_btn{
        position: absolute;
        z-index: 2;
        left:95%;
        top:80%;

        height: 60px;
        width: 60px;
        background-color: transparent;
        font-size: 40px;
        border: transparent;
        font-weight:bold;
    }


    .video-js .vjs-icon-placeholder .video-player {
        width: 100%;
        height: 100%;
        padding-top: 0px;
    }

    .videoPlay {
        /* padding-top: 40px; */
        box-sizing: border-box;
        position: absolute !important;
        height: 100%;
        width: 100%;
        border: 2px solid #aaa;
    }

    .videoOut {
        background-color: blue;
        display: block;
         height: 100%;
         width: 100%;
    }

    /*重要 配合aspectRatio视频比例可以让视频适应盒子大小-------start*/
    .vjs-custom-skin {
        height: 100% ;
    }

    .vjs-custom-skin /deep/ .video-js {
        width: 100% ;
        height: 100%;
    }

    .vjs-custom-skin > .video-js{
        height: 100%;
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
        /*background-color: red;*/
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