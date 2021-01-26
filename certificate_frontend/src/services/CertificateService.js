import Api from '@/services/Api'

export default {
    fetchCertificates () {
        return Api().get('certificates')
    }
}
