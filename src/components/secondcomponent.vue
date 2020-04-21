<template>
    <div id="secondcomponent">
        <el-card class="box-card">
            <div slot="header" class="clearfix">
                <h2 style="line-height: 36px; color: #20A0FF">豆瓣电影排行榜</h2>
            </div>
            <div v-for="article in articles" class="text item">
                {{article.title}}
            </div>
        </el-card>
        <h1>second footer</h1>
        <a>written by {{author}}</a>
    </div>
</template>





<script>
    import http from "~/api/http";
    export default {
        name: "secondcomponent",
        data(){
            return {
                author:'second',
                articles:[]
            }
        },
        mounted: function() {
            // https://api.apiopen.top/getWangYiNews
            http.getRequest('127.0.0.1:8010/ffff',
                (res) => {
                    this.articles = res.data.result
                    console.log(res)
                })
            // this.$http.get('https://api.apiopen.top/getWangYiNews', {}, {
            //     headers: {
            //
            //     },
            //     emulateJSON: true
            // }).then(function(response) {
            //   // 这里是处理正确的回调
            //
            //     this.articles = response.data.result
            //     // this.articles = response.data["subjects"] 也可以
            //     console.log(this.articles)
            // }, function(response) {
            //     // 这里是处理错误的回调
            //     console.log(response)
            // });
        }
    }
</script>

<style scoped>
#secondcomponent {
  font-family: Helvetica, sans-serif;
  text-align: center;
}
</style>
