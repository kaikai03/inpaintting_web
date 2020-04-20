import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    state: {
        name: 'helloVueX'
    },
    mutations: {
        edit(state,payload) {
            state.name = 'jack'
            console.log(payload)
        }
    }
})

export default store
