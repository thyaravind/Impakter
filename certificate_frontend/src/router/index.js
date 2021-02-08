import Vue from 'vue'
import VueRouter from 'vue-router'
import BasicDetails from "@/components/CertificateForm/BasicDetails";
import Part2 from "@/components/CertificateForm/Part2";
import FormSDGTargets from "@/components/CertificateForm/SDGTargets";
import FormSDGs from "@/components/CertificateForm/SDGs";
import OrgHome from "@/components/Organization/OrgHome";
import Welcome from "@/components/Organization/Welcome";
import Home from "@/components/Home";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: Welcome
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/organization/home',
    name: 'OrgHome',
    component: OrgHome
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
    component: BasicDetails
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
  {
    path: '/certificates/add/part2',
    name: 'formPart2',
    component: Part2
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
