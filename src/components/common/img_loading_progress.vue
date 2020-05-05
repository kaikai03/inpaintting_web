<template>
    
</template>

<script>
    export default {
        name: "img_loading_progress",
        data(){
          return{
              count:0,
              playitems:[{"index":1,"type":"0","img":"http://127.0.0.1:90/imgs/1.jpg","media":"http://127.0.0.1:8020/mv/mv1.mp4"},
                {"index":2,"type":"1","img":"http://127.0.0.1:90/imgs/2.jpg","media":"http://127.0.0.1:8020/gif/gif1.gif"},
                {"index":3,"type":"1","img":"http://127.0.0.1:90/imgs/3.png","media":"http://127.0.0.1:8020/gif/gif3.gif"}]
          }
        },
        mounted() {
            console.log("mounted")
            for (let item of this.playitems){
                let img = new Image()
                img.src = item.img
                img.onload = (e)=>{
                    if(this.count == this.playitems.length-1){
                        console.log("全部完成")
                        // this.$router.push({name:"third3"})
                    }else{
                        console.log("加载OK： ",this.count+' : '+e.target.src)
                    }
                    this.count++
                }
                img.onloadstart = (e)=>{
                    console.log("开始下载：",this.count+' : '+e.target.src)
                }
                img.onerror = (e)=>{
                    console.log("error：",e.target.src)
                }
            }
        }
    }
</script>

<style scoped>

</style>