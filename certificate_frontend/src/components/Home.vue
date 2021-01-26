<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src

import CertificateService from "@/services/CertificateService";

export default {
  name: 'Home',
  data(){
    return {
      certificates:[]
    }

  },
  components: {

  },
  methods:{
    async getCertificates () {
      const response = await CertificateService.fetchCertificates()
      this.certificates= response.data
    }
  }
}
</script>
