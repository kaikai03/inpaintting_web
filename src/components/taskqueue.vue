<template>
    <div class="task-queue">
        <div class="infinite-list" >
            <div class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">
                <div v-for="i in taskItem" class="list-item">
                    <queue-item :index=i :name="`QQ截图20200720184455.png${i}`" :img="`addr${i}`"
                                :progress=0.0 stat="queuing"
                                :time="`2020-8-6 15:21:06${i}`"
                                :delCallback="itemDelCallback"
                    ></queue-item>
                </div>

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
                taskItem:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                count: 25,
                loading: false
            }
        },
        computed: {
            noMore() {
                return this.taskItem.length >= 35
            },
            disabled() {
                return this.loading || this.noMore
            }
        },
        methods: {
            load() {
                this.loading = true
                setTimeout(() => {
                    this.taskItem.push(this.taskItem.length)
                    this.taskItem.push(this.taskItem.length)
                    this.loading = false
                }, 2000)
                // this.count += 2
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

</style>
