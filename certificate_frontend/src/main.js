import Vue from 'vue'
import App from './App.vue'
import BootstrapVue from 'bootstrap-vue'
import VueFormulate from '@braid/vue-formulate'
import VueRouter from 'vue-router'
import store from "./store";
import VueSimpleAlert from "vue-simple-alert";
import ScrollView from 'vue-scrollview'


import './assets/custom_vars.scss'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-search-select/dist/VueSearchSelect.css'
import './assets/formulate.css'
import router from './router'

Vue.use(VueSimpleAlert);
Vue.use(ScrollView)
Vue.use(BootstrapVue)
Vue.config.productionTip = false
Vue.use(VueFormulate)
Vue.use(VueRouter)

new Vue({
  store,
  router,
  render: h => h(App)
}).$mount('#app')
