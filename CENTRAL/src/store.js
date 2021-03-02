import Vue from "vue";
import Vuex from "vuex";
import { ServicesFactory } from "@/services/ServicesFactory";
const organizationService = ServicesFactory.get("organizations");
const certificateService = ServicesFactory.get("certificates");
import organizationModel from "./models/organization";
import certificateModel from "./models/certificate";

Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        organizations: [],
        certificates: [],
        userID: "aravind",
        organization: new organizationModel(),
        certificate: new certificateModel(),
        mode: "new"

    },
    getters: {
        organizations: state => {
            return state.organizations
        },
        certificates: state => {
            return state.certificates
        },
        organization: state => {
            return state.organization
        },
        mode: state => {
            return state.mode
        },
    },
    mutations: {

        async fetchOrganizations(state) {
            if (state.userID == null && localStorage.getItem("UserID") != null) {
                state.userID = localStorage.getItem("UserID")
            }
            state.organizations = [];
            var organizationsResponse = null;
            await organizationService.fetchOrganizations().then(response => (organizationsResponse = response.data.organizations)).catch((e) =>
                console.log("Error printed:" + e));
            console.log(organizationsResponse)
            if (organizationsResponse == null) {
                state.isNetworkConnected = false
                console.log("response is null")
            }
            else {
                state.isNetworkConnected = true
                for (var i = 0; i < organizationsResponse.length; i++) {
                    var org = new organizationModel()
                    org.map(organizationsResponse[i])
                    state.organizations.push(org)
                }
                
            }


        },
        addOrganization(state, payload) {
            state.organizations.Add(payload)
        },
        async fetchCertificates(state) {
            state.certificates = [];
            var certificatesResponse = null;
            await certificateService.fetchCertificates().then(response => (certificatesResponse = response.data)).catch((e) =>
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
        resetCertificate(state) {
            state.certificate = new certificateModel()
        },
        resetOrganization(state) {
            state.organization = new organizationModel()
        },
        changeOrganization(state,payload){
            state.organization = payload
        }
   
   

    },
    actions: {
        async fetchOrganizations(context, payload) {
            context.commit("fetchOrganizations", payload)
        },
        async fetchCertificates(context, payload) {
            context.commit("fetchCertificates", payload)
        },
        resetCertificate(context) {
            context.commit("resetCertificate")
        },
        resetOrganization(context) {
            context.commit("resetOrganization")
        },
        changeOrganization(context) {
            context.commit("changeOrganization")
        },

    }
});
