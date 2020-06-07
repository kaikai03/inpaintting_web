const backen = '127.0.0.1'
const port = '9000'
const http_prefix = 'http://'


export default {
    backen,
    port,
    random_videos_urlmaker(num) {
        return http_prefix + backen + ":" + port + "/random1/" + num.toString()
    },
    upload_img_urlmaker() {
        return http_prefix + backen + ":" + port + "/uploadimg/"
    }
}