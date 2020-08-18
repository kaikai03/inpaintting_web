const backen = '127.0.0.1'
const port = '9000'
const http_prefix = 'http://'
const work_stat = {
    cpl: 'completed',
    stop: 'stopped',
    hi: 'high',
    low: 'low',
    que: 'queuing', //normal
    err: 'error'
}



export default {
    backen,
    port,
    work_stat,
    random_videos_urlmaker(num) {
        //TODO： error path for test
        return http_prefix + backen + ":" + port + "/random1/" + num.toString()
    },
    upload_img_urlmaker() {
        return http_prefix + backen + ":" + port + "/uploadimg/"
    },
    upload_tasks() {
        return http_prefix + backen + ":" + port + "/uploadtask/"
    }
}