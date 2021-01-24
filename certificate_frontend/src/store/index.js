import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {

        certificate: {
            name: "",
            applicationLength: "",
            difficulty: null,
            relevance: null,
            validity: null,
            region: null,
            countries:[],
            goal:null,
            rating:"P3",
            pricing:"",
            sdgEngagement:"",
            sdgs:[],
            sdgTargets:[],
            industries:[],
            industrySectors:[]
        }

    },
    getters: {
        certificateForm: state => {
            return state.certificate
        }
    },
    mutations: {
        changeCertificate (state, payload) {
            state.certificate = payload
        },
        addSdgs(state, payload){
            state.certificate.sdgs = payload
        },
        addSdgTargets(state, payload){
            state.certificate.sdgTargets = payload
        },
        addIndustrySectors(state, payload){
            state.certificate.sdgTargets = payload
        },

        resetCertificate (state){
            state.certificate = {
                name: "",
                applicationLength: "",
                difficulty: null,
                relevance: null,
                validity: null,
                region: null,
                countries:[],
                goal:null,
                rating:"P3",
                pricing:"",
                sdgEngagement:"",
                sdgs:[],
                sdgTargets:[],
                industries:[],
                industrySectors:[]
            }
        }

    },
    actions: {}
});
