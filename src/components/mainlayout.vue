<template>
  <el-container>
    <!-- 顶栏 -->
    <el-header height="40px"  style="display: table">
      <h3 style="display: table-cell ;vertical-align: middle">图像</h3>
    </el-header>

    <el-container id="carousel_container">
    <img_loading_progress></img_loading_progress>
    </el-container>
<!--    <carousel>-->
<!--    </carousel>-->
    <!-- 嵌套容器 -->
    <el-container id="main_container">
      <!-- 侧边导航菜单 -->
      <el-aside style="width: auto">
        <navigator></navigator>
      </el-aside>
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
    </el-container>
    <!-- 底栏 -->
    <el-footer height="30px">&copy;究极死胖兽 2019</el-footer>
  </el-container>
</template>

<script>
    import navigator from "~/components/navigator";
    import carousel from "~/components/carousel";
    import img_loading_progress from "~/components/common/img_loading_progress";


    export default {
        name: "mainlayout",
        components:{
          navigator,carousel,img_loading_progress
        }
    }
</script>


<style>
  #carousel_container {
    height:400px;
    style:"background-color: #8c939d";
  }
  #main_container {
    min-height:800px; height:auto!important; height:900px;
  }
.el-header {
  background-color: white;
  color: gray;
  width: 100%;
}
.el-footer {
  background-color: #909399;
  color: black;
  text-align: center;
}
.el-aside {
  background-color: chartreuse;
}
.el-main {
  background-color: darkkhaki;
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


