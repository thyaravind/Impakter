import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
    state: {

        certificate: {
            certificateID:null,
            name: "",
            description:"",
            applicationLength: "",
            imagePath:"",
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
        certificates:[],
        organizationID:null,
        mode:"new"

    },
    getters: {
        certificateForm: state => {
            return state.certificate
        },
        payload: state =>{
            return {
                basicDetails:{
                                    certificateID:state.certificate.certificateID,
                payload:{                name: state.certificate.name,
                    organizationID:state.organizationID,
                    description: state.certificate.description,
                    applicationLength:state.certificate.applicationLength,
                    difficulty: state.certificate.difficulty,
                    relevance: state.certificate.relevance,
                    validity:state.certificate.validity,
                    goal: state.certificate.goal,
                    specificity:state.certificate.rating,
                    pricing: state.certificate.pricing,
                    sdgEngagement: state.certificate.sdgEngagement
                },
                sdgs:state.certificate.sdgs,
                sdgTargets:state.certificate.sdgTargets

}

            }
        },
        certificates: state => {
            return state.certificates
        },
        mode: state => {
            return state.mode
        },
        organizationIdentifier: state => {
            return state.organizationID
        },


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
        },

        fetchCertificates(state,payload){
            state.certificates = payload
        },

        setOrganizationID(state,payload){
            state.organizationID = payload
        },

        addCertificate(state,payload){
            state.certificates.Add(payload)
        },
        changeMode(state,payload){
            state.mode = payload
        }

    },
    actions: {
        changeCertificate (context, payload) {
            context.commit("changeCertificate",payload)
        },
        addSdgs(context, payload){
            context.commit("addSdgs",payload)
        },
        addSdgTargets(context, payload){
            context.commit("addSdgTargets",payload)
        },
        addIndustrySectors(context, payload){
            context.commit("addIndustrySectors",payload)
        },
        resetCertificate(context){
            context.commit("resetCertificate")
        },

        setOrganizationID(context,payload){
            context.commit("setOrganizationID",payload)
        },
        fetchCertificates(context,payload){
            context.commit("fetchCertificates",payload)
        },

        addCertificate(context,payload){
            context.commit("addCertificate",payload)
        },
        changeMode(context,payload){
            context.commit("changeMode",payload)
        }


    }
});
