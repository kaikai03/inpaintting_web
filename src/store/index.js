import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        name:'black tome',
        host: document.location.hostname
    },
    mutations: {
        edit(state,payload) {
            state.name = 'jack'
            console.log(payload)
        }
    }
})

export default store
