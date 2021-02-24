import Vue from "vue";
import Vuex from "vuex";
import { ServicesFactory } from "@/services/ServicesFactory";
import axios from 'axios'

const certificateService = ServicesFactory.get("certificates");
const organizationService = ServicesFactory.get("organizations");
import certificateModel from "../models/certificate";
import {awsConfig} from "@/models/constants"

Vue.use(Vuex);

export default new Vuex.Store({
    state: {

        certificateArchived: {
            certificateID: null,
            name: "",
            description: "",
            priority: "",
            applicationLength: "",
            imagePath: "",
            difficulty: null,
            relevance: null,
            validity: null,
            region: null,
            countries: [],
            goal: null,
            rating: "P3",
            pricing: "",
            sdgEngagement: "",
            sdgs: [],
            sdgTargets: [],
            industries: [],
            industrySectors: [],
            activeStatus: true
        },
        certificate: new certificateModel(),
        organizationName: null,
        certificates: null,
        organizationID: null,
        mode: "new",
        IsloggedIn: false,
        isNetworkConnected: null,
        uploadPolicy: null,
        orgLoginFailed: false

    },
    getters: {
        certificateForm: state => {
            state.certificate.setOrganizationID(state.organizationID)
            console.log(state.organizationID)
            return state.certificate
        },
        payloadArchived: state => {
            return {
                certificateID: state.certificate.certificateID,
                basicDetails: {
                    name: state.certificate.name,
                    organizationID: state.organizationID,
                    description: state.certificate.description,
                    priority: state.certificate.priority,
                    activeStatus: state.certificate.activeStatus
                },
                sdgs: state.certificate.sdgs,
                sdgTargets: state.certificate.sdgTargets,
                additionalDetails: {
                    applicationLength: state.certificate.applicationLength,
                    difficulty: state.certificate.difficulty,
                    relevance: state.certificate.relevance,
                    validity: state.certificate.validity,
                    goal: state.certificate.goal,
                    specificity: state.certificate.rating,
                    pricing: state.certificate.pricing,
                    sdgEngagement: state.certificate.sdgEngagement
                }

            }


        },
        payload: state => {
            var payload = state.certificate.getCertificatePayload()
            return payload
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
        isNetworkConnected: state => {
            return state.isNetworkConnected
        },
        organization: state => {
            return {
                organizationID: state.organizationID,
                organizationName: state.organizationName
            }
        },
        uploadPolicy: state => {
            return state.uploadPolicy
        }
    },
    mutations: {
        changeCertificate(state, payload) {
            state.certificate = payload
        },
        addSdgs(state, payload) {
            state.certificate.sdgs = payload
            state.certificate.computeSdgs()
        },
        addSdgTargets(state, payload) {
            state.certificate.sdgTargets = payload
        },
        addIndustries(state, payload) {
            state.certificate.industries = payload
            state.certificate.computeIndustries()
        },
        addSubIndustries(state, payload) {
            state.certificate.industrySectors = payload
        },

        resetCertificate(state) {
            state.certificate = new certificateModel()

        },

        async fetchCertificates(state) {
            if (state.organizationID == null && localStorage.getItem("OrganizationID") != null) {
                state.organizationID = localStorage.getItem("OrganizationID")
            }
            state.certificates = [];
            var certificatesResponse = null;
            await certificateService.fetchCertificates(state.organizationID).then(response => (certificatesResponse = response.data)).catch((e) =>
                console.log("Error printed:" + e));
            console.log(certificatesResponse)
            if (certificatesResponse == null) {
                state.isNetworkConnected = false
            }
            else {
                state.isNetworkConnected = true
                for (var i = 0; i < certificatesResponse.length; i++) {
                    var cert = new certificateModel()
                    cert.change(certificatesResponse[i])
                    state.certificates.push(cert)
                }
                
            }


        },

        async fetchOrganization(state) {
            if (state.organizationID == null && localStorage.getItem("OrganizationID") != null) {
                state.organizationID = localStorage.getItem("OrganizationID")
                state.organizationName = localStorage.getItem("OrganizationName")
            }
            else {
                var organizationResponse
                await organizationService.fetchOrganization(state.organizationID).then(response => (organizationResponse = response.data.organizationDetails[0]));
                if(organizationResponse == undefined){
                    state.orgLoginFailed = true

                }
                else {
                window.localStorage.setItem('OrganizationID', organizationResponse.organizationID)
                window.localStorage.setItem('OrganizationName', organizationResponse.name)
                state.organizationID = localStorage.getItem("OrganizationID")
                state.organizationName = localStorage.getItem("OrganizationName")
                }

            }

        },

        setOrganizationID(state, payload) {
            state.organizationID = payload
        },

        addCertificate(state, payload) {
            state.certificates.Add(payload)
        },
        changeMode(state, payload) {
            state.mode = payload
        },
        changeLoginStatus(state) {
            if (localStorage.getItem("OrganizationID") == null) {
                state.IsloggedIn = false
            }
            else state.IsloggedIn = true
        },
        resetComputedSdgs(state) {
            state.certificate.computedSdgs = []
        },

        async updateCertificateStatus(state, payload) {
            state.certificate = payload
            state.certificate.mode = "statusChange"
            var req = state.certificate.getCertificatePayload()

            await certificateService.updateCertificate(req).then((response) => {
                this.responseMessage = response.data.msg
                this.responseStatus = response.data.status
            });
            console.log(this.responseMessage)
            state.certificate = new certificateModel()

        },

        fetchSignatureAndPolicy(state,payload){
            state.uploadPolicy = awsConfig.policy
            state.uploadPolicy.content_type = payload.content_type
            state.uploadPolicy.key = `certificateLogos/${state.organizationName}_${payload.filename}`
        },
        async uploadImage(payload){
            let { data } = await axios.post(awsConfig.s3bucketUrl, payload)
            console.log(data)
        }

    },
    actions: {
        changeCertificate(context, payload) {
            context.commit("changeCertificate", payload)
        },
        addSdgs(context, payload) {
            context.commit("addSdgs", payload)
        },
        addSdgTargets(context, payload) {
            context.commit("addSdgTargets", payload)
        },
        addIndustries(context, payload) {
            context.commit("addIndustries", payload)
        },
        addSubIndustries(context, payload) {
            context.commit("addSubIndustries", payload)
        },

        resetCertificate(context) {
            context.commit("resetCertificate")
        },

        setOrganizationID(context, payload) {
            context.commit("setOrganizationID", payload)
        },
        async fetchCertificates(context, payload) {
            context.commit("fetchCertificates", payload)
        },
        async fetchOrganization(context, payload) {
            context.commit("fetchOrganization", payload)
        },

        addCertificate(context, payload) {
            context.commit("addCertificate", payload)
        },
        changeMode(context, payload) {
            context.commit("changeMode", payload)
        },
        changeLoginStatus(context) {
            context.commit("changeLoginStatus")
        },
        resetComputed(context) {
            context.commit("resetComputedSdgs")
        },
        updateCertificateStatus(context, payload) {
            context.commit("updateCertificateStatus", payload)
        }


    }
});
