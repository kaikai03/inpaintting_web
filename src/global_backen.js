const backen = '127.0.0.1'
const port = '9000'
const http_prefix = 'http://'
const https_prefix = 'https://'
const ws_prefix = 'ws://'
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
    randomVideosUrlmaker(num) {
        //TODO： error path for test
        return http_prefix + backen + ":" + port + "/random1/" + num.toString()
    },
    uploadImgUrlmaker() {
        return http_prefix + backen + ":" + port + "/uploadimg/"
    },
    uploadTasksUrlmaker() {
        return http_prefix + backen + ":" + port + "/uploadtask/"
    },
    tasksListUrlmaker(page, pageSize, workState) {
        return http_prefix + backen + ":" + port + "/tasks/?page_size=" + pageSize + "&page=" + page + "&work_status=" + workState
    },
    imgUrlmaker(imgName) {
        return http_prefix + backen + ":" + port + "/cover/" + imgName
    },
    taskStatusChange() {
        return http_prefix + backen + ":" + port + "/taskstatus/change"
    },
    taskDrop() {
        return http_prefix + backen + ":" + port + "/drop/"
    },
    dashboardMonitorSocket(workerName){
        return ws_prefix + backen + ":" + port +'/dashboard/ws/data/' + workerName
    },
    getOnlineWorkers(){
        return http_prefix + backen + ":" + port +'/dashboard/workers'
    }


}