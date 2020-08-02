<template>
    <div class="taskqueue">
        <div class="infinite-list" style="overflow:auto" >
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
                count: 10,
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
                // this.loading = true
                // setTimeout(() => {
                //     this.count += 2
                //     this.loading = false
                // }, 2000)
                this.count += 2
            }
        }
    }
</script>

<style>
.taskqueue {
    width: 100%;
    max-height: 100px;
  font-family: Helvetica, sans-serif;
  text-align: center;
}

</style>


<style scoped>

</style>
