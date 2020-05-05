<template>
  <el-carousel :autoplay="autoplay" :interval="1000" type="card" height="400px" ref="carousel" arrow="never" @change="((pre, next) => {change(pre, next)})">
    <el-carousel-item v-for="(item,index) in 6" :key="item" name="index">
      <div style="height: 100%;width: 100%;" @click="clickitem(item)">
        <div style="height: 30%;width: 30%; position: absolute; top: 50%; left: 50%; transform: translate(-50%,-50%); background-color: red" @click.stop="clickplay(item)">
          <h3 class="medium">{{ item }}</h3>
        </div >
      </div>
    </el-carousel-item>
  </el-carousel>
</template>


<script>
    export default {
        name: "carouselcomponent",
        data(){
          return{
            autoplay:true
          }
        },
        methods:{
          clickitem(item) {
            //this.$refs.carousel.setActiveItem(0);
            // this.$refs.carousel.next();
            console.log('clickitem:'+item);
            // this.$refs.carousel.interval
            if (this.autoplay==true){
              this.autoplay=false;
              console.log('停止');
            } else {
              this.autoplay=true;
              console.log('启动');
            }
          },
          clickplay(item) {
            //this.$refs.carousel.setActiveItem(0);
            console.log('....', item);
            console.log('....', this.$refs.carousel.activeIndex);
            if(item == this.$refs.carousel.activeIndex+1){
              console.log('有效点击');
            }else {console.log('无效');}
          },
          change(pre, next){
            console.log('change',pre, next);
          }
        },
        watch: {
          change(val, oldVal) {
            // this.resetItemPosition(oldVal);
            // this.$emit('change', val, oldVal);

            console.log("change")
          },
        }
    }
</script>

<style >
    .el-carousel {
        background-color: black;
    }
    .el-carousel--card {
      padding-top: 10px;
      padding-bottom: 10px;
      padding-left:20px;
      padding-right:60px;
    }
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__indicators--outside{
    position: absolute;
    bottom: 16px;
    transform: unset;
    left: 0px;
    right: 0px;
  }
    .el-carousel__indicators--outside button{
    background-color: red;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

</style>