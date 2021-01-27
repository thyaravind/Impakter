import Api from '@/services/Api'

const resource = "/organizations"

export default {
    fetchOrganizations () {
        return Api().get(`${resource}/`);
    },
    createOrganization(payload){
        return Api().post(`${resource}/`,payload);
    }
}
