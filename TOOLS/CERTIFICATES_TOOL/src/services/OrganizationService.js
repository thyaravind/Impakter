import Api from '@/services/Api'

const resource = "/organizations"

export default {
    fetchOrganizations () {
        return Api().get(`${resource}/`);
    },
    fetchOrganization(organizationID){
        return Api().get(`${resource}/${organizationID}`);
    },
    createOrganization(payload){
        return Api().post(`${resource}/`,payload);
    },
    updateOrganization(payload){
        return Api().put(`${resource}/`,payload);
    },
}
