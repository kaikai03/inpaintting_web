<template>
    <div class="task-queue">
        <div class="infinite-list" >
            <div class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">

                 <transition-group appear name="queue-move" >
                    <div v-for="(content,i) in taskItem" class="list-item" :id="'id-'+content['doc_code']" :key="content['doc_code']">


                        <queue-item :index=i :name="`${content['task_name']}`" :imgName="content.img"
                                    :progress=0.0 :stat="content.status"
                                    :time="content.created"
                                    :delCallback="itemDelCallback"
                                    :task-i-d="content.doc_code"

                        ></queue-item>

                    </div>
                 </transition-group>


                <p v-if="loading" class="list-loading">加载中...</p>
                <p v-if="noMore" class="list-noMore">没有更多了</p>
            </div>
        </div>
    </div>
</template>

<script>
    import queueItem from "~/components/taskqueueitem";
    export default {
        name: "taskQueue",
        data() {
            return {
                workState:this.backen.work_stat,
                taskItem:[],
                fullPage: 999,
                fullElement:999,
                curPage:0,
                loading: false,
                netError: false,
            }
        },
        computed: {
            noMore() {
                return this.taskItem.length >= this.fullElement ||  this.curPage >= this.fullPage
            },
            disabled() {
                return this.loading || this.noMore|| this.netError
            }
        },
        methods: {
            load() {
                this.loading = true
                setTimeout(() => {
                    console.log("start",this.curPage+1,this.taskItem.length,this.fullPage)
                    if (this.curPage+1>this.fullPage){
                        console.log("large")
                        return
                    }
                    this.network.get_request(this.backen.tasksListUrlmaker(this.curPage+1,10, this.workState.que),
                    (res) => {
                        console.log("chenggong")
                        console.log(res.body['page_info'])
                        console.log(res.body['contents'])
                        this.fullPage = res.body['page_info']['page_all']
                        this.fullElement = res.body['page_info']['element_all']
                        this.curPage = res.body['page_info']['cur_page']
                        Array.prototype.push.apply(this.taskItem, res.body['contents'])
                        console.log(this.taskItem)
                    },
                    (er) => {
                        this.$message({
                            message: '网络错误，无法获取任务,请刷新页面',
                            center: true,
                            showClose: true,
                            type: 'error'
                        });
                        this.netError = true
                    }
                    );
                    this.loading = false
                }, 1000)
            },
            itemDelCallback(index){
                console.log("del",index)
                this.taskItem.splice(index, 1);
                this.$message({type: 'success', message: '删除成功!'});
            }
        },
        components:{
          queueItem
        }
    }
</script>

<style>



</style>


<style scoped>
    .task-queue {
        position: relative;
        padding-top: 20px;
        padding-right: 4px;
        padding-bottom: 20px;
        height: 800px;
        overflow: hidden;
    }
    .infinite-list{
        background-color: #F56C6C;
        height: 100%;
        width: 100%;
        overflow-y: scroll;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none;  /* IE 10+ */
    }

    .infinite-list::-webkit-scrollbar { /* WebKit */
        width: 0;
        height: 0;
    }

    .infinite-list .list{
        height: 100%;
        width: 100%;

    }

    .infinite-list .list-item {
        display: flex;
        align-items: center;
        justify-content: center;
        /*height: 100px;*/
        /*width: 100%;*/
        /*background: #e8f3fe;*/
        margin: 3px;
        /*color: #7dbcfc;*/
        /*border-radius: 5px;*/
    }

    .infinite-list .list .list-noMore {
        display: flex;
        align-items: center;
        justify-content: center;


    }

    .infinite-list .list .list-loading {
        display: flex;
        align-items: center;
        justify-content: center;


    }

    .queue-move-enter {
        transform: translateY(20px);
        opacity: 0;
    }
    .queue-move-enter-active {
        transition: all 0.3s ease;
    }
    .queue-move-enter-to {
    }
    .queue-move-leave{
    }
    .queue-move-leave-active {
        position: absolute;
        width: 96.5%;
        transition: opacity 0.6s;
        transform: scale(1);
        opacity: 0;
    }

    .queue-move-leave-to {
        transform: scale(0);
        opacity: 0;
    }

    .queue-move-move {
        transition: all 0.50s cubic-bezier(1.0,0.7,0.4,1.8);
    }


</style>
