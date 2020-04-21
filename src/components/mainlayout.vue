<template>
  <el-container>
    <!-- 顶栏 -->
    <el-header height="60px">
      <h2>Element 页面布局</h2>
    </el-header>
    <!-- 嵌套容器 -->
    <el-container>
      <!-- 侧边导航菜单 -->
      <el-aside width="150px"></el-aside>
      <!-- 内容 -->
      <el-main>
        <!-- 第一列栅格布局 -->
        <el-row>
          <el-col :span="12" class="col1">
            <li>
              <router-link to="/first">“第一页”</router-link>
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
    import firstcomponent from "~/components/firstcomponent";
    import secondcomponent from "~/components/secondcomponent";
    import third from "~/components/third";
    export default {
        name: "mainlayout"
    }
</script>


<style>
  .el-container {
    min-height:800px; height:auto!important; height:900px;
  }
.el-header {
  background-color: #409EFF;
  color: white;
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


