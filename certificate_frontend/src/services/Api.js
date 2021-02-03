import axios from 'axios'


export default() => {
    return axios.create({
        baseURL: `http://54.211.156.101/api`
    })
}
