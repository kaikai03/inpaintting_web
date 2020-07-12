import Vue from "vue"
import vueResource from "vue-resource"

Vue.use(vueResource)

// Vue.http.interceptors.push((request, next) => {
//     //请求发送前的处理逻辑
//     request.headers.set('Origin', document.location.hostname)
//     next((response) => {
//         //请求发送后的处理逻辑
//         //根据请求的状态，response参数返回给successCallback或errorCallback
//         return response
//     })
// })


export default {
    get_request(url, cb, er) {
        let er_ = er
        if(typeof(er_) != "function"){
            er_ = (err) => {console.log(err);}
        }

        return new Promise((resolve, reject) => {
            Vue.http.get(
                url,
                {emulateJSON: true}
            )
                .then(cb)
                .catch(er_);
        });
    },
    post_request(url, params, cb, er) {
        let er_ = er
        if(typeof(er_) != "function"){
            er_ = (err) => {console.log(err);}
        }
        return new Promise((resolve, reject) => {
            Vue.http.post(
                url,
                params,
                {emulateJSON: true}
            )
                .then(cb)
                .catch(er_);
        });
    }
}