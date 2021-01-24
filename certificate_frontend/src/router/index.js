import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import FormBasicDetails from "@/components/CertificateForm/FormBasicDetails";
import FormSDGTargets from "@/components/CertificateForm/FormSDGTargets";
import FormSDGs from "@/components/CertificateForm/FormSDGs";


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../components/About.vue')
  },
  {
    path: '/certificates/add',
    name: 'formPage1',
    component: FormBasicDetails
  },
  {
    path: '/certificates/add/sdgs',
    name: 'formPage2-1',
    component: FormSDGs
  },
  {
    path: '/certificates/add/sdgtargets',
    name: 'formPage2-2',
    component: FormSDGTargets
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
