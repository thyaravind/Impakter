import Api from '@/services/Api'

const resource = "/certificates"

export default {
    fetchCertificates(organizationID) {
        return Api().get(`${resource}/${organizationID}`);
    },
    createCertificate(payload){
        return Api().post(`${resource}/`,payload);
    },
    updateCertificate(payload){
        return Api().put(`${resource}/`,payload);
    },
    deleteCertificate(ID){
        return Api().delete(`${resource}/${ID}`);
    },


}
