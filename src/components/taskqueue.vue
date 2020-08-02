<template>
    <div class="taskqueue">
        <div class="infinite-list" >
            <ul class="list" v-infinite-scroll="load" infinite-scroll-disabled="disabled">
                <li v-for="i in count" class="list-item">{{ i }}</li>
            </ul>
            <p v-if="loading">加载中...</p>
            <p v-if="noMore">没有更多了</p>
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
                return this.count >= 202
            },
            disabled() {
                return this.loading || this.noMore
            }
        },
        methods: {
            load() {
                this.loading = true
                setTimeout(() => {
                    this.count += 2
                    this.loading = false
                }, 1000)
                // this.count += 2
            }
        }
    }
</script>

<style>
.taskqueue {
     position: relative;
     padding-top: 24px;
     padding-bottom: 24px;
}
    .infinite-list{
        background-color: #F56C6C;
        height: 800px;
        overflow-y: scroll;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none;  /* IE 10+ */
    }

    .infinite-list::-webkit-scrollbar { /* WebKit */
        width: 0;
        height: 0;}



</style>


<style scoped>

</style>
