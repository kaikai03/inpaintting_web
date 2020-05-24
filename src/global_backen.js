const backen = '127.0.0.1'
const port = '9000'

export default {
    backen,
    port,
  random_videos_urlmaker(num) {
      return "http://"+backen+":"+port+"/random/"+num.toString()
  },
}