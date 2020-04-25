<template>
    <div>
    <div class="box">
<!--        <img :src="require('../../assets/'+imgname)" style="display:block;">-->
        <img v-if="imgfile" :src="imgfile" style="display:block;" >
        <img v-else v-bind:src="imgadd" style="display:block;" >

        <b class="shan"></b>
    </div>
    <img src="../../assets/logo.png" style="display:block;">
       {{imgadd}}

    </div>
</template>

<script>
    export default {
        name: "twinklingimage",
        data(){
            return {}
        },
        props: {'imgadd':String,'imgfile':String},

    }
</script>

<style scoped>
    .box {
        position: relative;
        overflow: hidden;
        cursor: pointer;
        margin: 0 auto;
        width: 1000px;
    }

    @-webkit-keyframes changeImg {
        from {
            left: -100%;
        }
        100% {
            left: 150%;
        }
    }

    .shan {
        position: absolute;
        -webkit-animation: changeImg 3s ease 0s;
        -o-animation: changeImg 3s ease 0s;
        animation: changeImg 3s ease 0s;
        top: 0;
        width: 30%;
        height: 100%;
        content: "";
        background: -webkit-linear-gradient(left, rgba(255, 255, 255, 0) 0, rgba(255, 255, 255, .4) 50%, rgba(255, 255, 255, 0) 100%);
        background: -o-linear-gradient(left, rgba(255, 255, 255, 0) 0, rgba(255, 255, 255, .4) 50%, rgba(255, 255, 255, 0) 100%);
        background: -moz-linear-gradient(left, rgba(255, 255, 255, 0) 0, rgba(255, 255, 255, .4) 50%, rgba(255, 255, 255, 0) 100%);
        background: linear-gradient(to right, rgba(255, 255, 255, 0) 0, rgba(255, 255, 255, .4) 50%, rgba(255, 255, 255, 0) 100%);
        transform: skewX(-45deg);
        animation-iteration-count: infinite;
        -moz-animation-iteration-count: infinite;
        -webkit-animation-iteration-count: infinite;
    }
</style>