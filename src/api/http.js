import Vue from "vue"
import vueResource from "vue-resource"

Vue.use(vueResource)

export default {
    getRequest(url, cb, er) {
        var er_ = er
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
    postRequest(url, params, cb) {
        return new Promise((resolve, reject) => {
            Vue.http.post(
                url,
                params,
                {emulateJSON: true}
            )
                .then(cb)
                .catch((err) => {
                    reject(err);
                });
        });
    }
}