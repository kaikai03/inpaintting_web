<template>
    <div class="taskqueue">
        <div class="infinite-list" >
            <div class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">
                <p v-for="i in count" class="list-item">{{ i }}</p>

                <p v-if="loading" class="list-item">加载中...</p>
                <p v-if="noMore" class="list-item">没有更多了</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "taskqueue",
        data() {
            return {
                count: 40,
                loading: false
            }
        },
        computed: {
            noMore() {
                return this.count >= 80
            },
            disabled() {
                return this.loading || this.noMore
            }
        },
        methods: {
            load() {
                this.loading = true
                setTimeout(() => {
                    this.count += 4
                    this.loading = false
                }, 1000)
                // this.count += 2
            }
        }
    }
</script>

<style>



</style>


<style scoped>
    .taskqueue {
        position: relative;
        padding-top: 24px;
        padding-bottom: 24px;
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

    .infinite-list .list .list-item {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100px;
        /*width: 100%;*/
        background: #e8f3fe;
        margin: 2px;
        color: #7dbcfc;
        border-radius: 5px;
    }

</style>
