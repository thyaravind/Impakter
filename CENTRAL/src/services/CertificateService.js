import Api from '@/services/Api'

const resource = "/certificates"

export default {
    fetchCertificates() {
        return Api().get(`${resource}/`);
    },
    fetchCertificate(organizationID) {
        return Api().get(`${resource}/${organizationID}`);
    },
    createCertificate(payload){
        return Api().post(`${resource}/`,payload);
    },
    updateCertificate(payload){
        return Api().put(`${resource}/`,payload);
    },

}
