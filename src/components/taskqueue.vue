<template>
    <div class="task-queue">
        <div class="infinite-list" >
            <div class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">

                 <transition-group appear name="queue-move" tag="queue-item">
                    <div v-for="(content,i) in taskItem" class="list-item" :key="content">


                        <queue-item :index=i :name="`QQ截图20200720184455.png${content}`" :img="`addr${i}`"
                                    :progress=0.0 stat="queuing"
                                    :time="`2020-8-6 15:21:06${i}`"
                                    :delCallback="itemDelCallback"

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
                taskItem:["0", "3", "5", "6", "7", "11", "13", "17", "19", "21", "22", "23", "35", "56", "87", "89", "90", "96", "97", "99"],
                count: 18,
                loading: false
            }
        },
        computed: {
            noMore() {
                return this.taskItem.length >= 25
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
                }, 1000)
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
        position: absolute;
        transform: translateX(0px);
        transform: translateY(0px);
    }
    .queue-move-leave-active {
        /*transition: all .38s ease;*/
        position: absolute;
        width: 96.5%;
        transform: translateX(0px);
        transform: translateY(0px);
    }

    .queue-move-leave-to {
        transform: translateX(0px);
        transform: translateY(0px);
        opacity: 0;
    }

    .queue-move-move {
        transition: all 0.58s ease;
    }


</style>
