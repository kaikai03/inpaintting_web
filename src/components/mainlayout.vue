<template>
  <el-container>
    <!-- 顶栏 -->
    <el-header height="40px" style="display: table">
      <h3 style="display: table-cell ;vertical-align: middle">图像</h3>
      <h5 style="display: table-cell ;vertical-align: middle;text-align: right;">{{area}}&emsp;{{ip}}</h5>
    </el-header>

    <el-container id="carousel_container">
      <carousel></carousel>
    </el-container>
    <!--    <carousel>-->
    <!--    </carousel>-->
    <!-- 嵌套容器 -->
    <el-container id="main_container">
      <!-- 侧边导航菜单 -->
      <el-aside id='aside_left' style="width: auto;">
        <navigator></navigator>
      </el-aside >
      <!-- 内容 -->
      <el-main>
        <!-- 第一列栅格布局 -->
        <el-row>
          <el-col :span="12" class="col1">
            <li>
              <router-link to="/first">“第一页”</router-link>
              <el-button type="danger">主要按钮</el-button>
            </li>
          </el-col>
          <el-col :span="12" class="col2">
            <li>
              <router-link to="/third">“third”</router-link>
            </li>
          </el-col>
        </el-row>
        <!-- 第二列布局 -->
        <el-row>
          <el-col :span="24" class="col3">
            <router-view name="view1"></router-view>
            <router-view name="view2"></router-view>
          </el-col>
        </el-row>
      </el-main>
      <el-aside  id='aside_right' style="width: 200px;">

      </el-aside>
    </el-container>
    <!-- 底栏 -->
    <el-footer height="20px">&copy;  kai_kai03@hotmail.com &nbsp;  2020</el-footer>
  </el-container>

</template>

<script>
    import band_backspace from "~/js/band_backspace"
    import navigator from "~/components/navigator";
    import carousel from "~/components/carousel";

    export default {
        name: "mainlayout",
      data(){
          return{
            ip:null,
            area:null
          }
      },
        mounted() {
          this.ip = sessionStorage.getItem('ip')
          this.area = sessionStorage.getItem('area')
          console.log(this.ip,this.area)
        },
      components:{
          navigator,carousel
        }
    }
</script>


<style>
  #carousel_container {
    height:360px;
    style:"background-color: #8c939d";
  }
  #main_container {
    min-height:800px; height:auto!important; height:900px;
  }
.el-header {
  background-color: snow;
  color: gray;
  width: 100%;
  z-index: 2;
}
.el-footer {
  background-color: snow;
  color: black;
  text-align: center;
}
  .el-aside {
    background-color: snow;
  }
  #aside_left {
    width: auto;
  }
  #aside_right {
    background-color: #3a8ee6;
    z-index: 2;
  }
.el-main {
  background-color: whitesmoke;
  z-index: 2;
}
.el-col {
  height: 200px;
}
.col1 {
  background-color: teal;
}
.col2 {
  background-color: tomato;
}
.col3 {
  background-color: thistle;
}

</style>


