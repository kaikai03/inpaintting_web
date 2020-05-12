<template>
<!--    <div class="navigator" @mouseover="mouseover" @mouseleave="mouseleave">-->
    <div class="navigator" v-on="{mouseenter:mouseover,mouseleave:mouseleave}">

        <!--        <el-radio-group v-model="isCollapse" style="margin-bottom: 20px;">-->
        <!--            <el-radio-button :label="false">展开</el-radio-button>-->
        <!--            <br>-->
        <!--            <el-radio-button :label="true">收起</el-radio-button>-->
        <!--        </el-radio-group>-->
        <!--        router :default-active="$route.path"-->
        <el-menu :default-active="$route.path" :router="true" :unique-opened="true" class="el-menu-vertical-demo" @open="handle_open" @close="handleClose"
                 :collapse="isCollapse"  @select="select_item" :active="selected">
            <el-menu-item index="/">
                <i class="el-icon-odometer"></i>
                <span slot="title">dash</span>
            </el-menu-item>
            <el-menu-item index="/first" >
                <i class="el-icon-upload2"></i>
                <span slot="title">upload
                </span>
            </el-menu-item>
            <el-menu-item index="/third" >
                <i class="el-icon-folder-opened"></i>
                <span slot="title">history</span>
            </el-menu-item>
            <el-menu-item index="4" disabled>
                <i class="el-icon-setting"></i>
                <span slot="title">setting</span>
            </el-menu-item>
            <el-menu-item index="5">
                <i class="el-icon-paperclip"></i>
                <span slot="title">论文</span>
            </el-menu-item>
            <el-menu-item index="6"  >
                <i class="el-icon-user"></i>
                <span slot="title">head</span>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<script>
    export default {
        name: "navigator",
        data() {
            return {
                isCollapse: true,
                selected:"1",
                pre_selected:null
            };
        },
        methods: {
            handle_open(key, keyPath) {
                console.log(key, keyPath);
            },
            handleClose(key, keyPath) {
                console.log(key, keyPath);
            },
            mouseover() {
                this.isCollapse= false
            },
            mouseleave() {
                this.isCollapse= true
            },
            select_item(index){
                console.log(index)
            },
            menu_click(item) {

            }

        }
    }
</script>

<style>
    .navigator{
        width: 100%;
    }

    .el-menu{
        background-color: snow;
        border-right: 0px;
    }


  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 130px;
    min-height: 300px;
  }

    .el-menu-item [class^="el-icon-"]{
        font-size: 23px;
    }



</style>