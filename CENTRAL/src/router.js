import Vue from 'vue'
import VueRouter from 'vue-router'

import CertificateOrganizations from "@/components/index/certificates/CertOrgs";
import Certificates from "@/components/index/certificates/Certificates";

Vue.use(VueRouter)

const routes = [
    {
        path: '/index/certificates/orgs',
        name: 'CertificateOrganizations',
        component: CertificateOrganizations
      },
      {
        path: '/index/certificates/all',
        name: 'Certificates',
        component: Certificates
      },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  
  
  export default router