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
        },
            sdgs: [{value:0,text:"SDG 1 No Poverty",targets:[
                    {value:1.1,text:"1.1 By 2030, eradicate extreme poverty for all people everywhere, currently measured as people living on less than $1.25 a day"},
                    {value:1.2,text:"1.2 By 2030, reduce at least by half the proportion of men, women and children of all ages living in poverty in all its dimensions according to national definitions"},
                    {value:1.3,text:"1.3 Implement nationally appropriate social protection systems and measures for all, including floors, and by 2030 achieve substantial coverage of the poor and the vulnerable"}]},
                {value:1,text:"SDG 2 Zero Hunger",targets:[{value:2.1,text:"2.1 By 2030, end hunger and ensure access by all people, in particular the poor and people in vulnerable situations, including infants, to safe, nutritious and sufficient food all year round"}]},
                {value:2,text:"SDG 3 Good Health and Well-Being",targets:[{value:3.1,text:"3.1 By 2030, reduce the global maternal mortality ratio to less than 70 per 100,000 live births"}]},
                {value:3,text:"SDG 4 Quality Education",targets:[]},
                {value:4,text:"SDG 5 Gender Equality",targets:[]},
                {value:5,text:"SDG 6 Clean Water and Sanitation",targets:[]}
            ]


    },
    getters: {
        certificateForm: state => {
            return state.certificate
        },
        sdgs: state => {
            return state.sdgs
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
