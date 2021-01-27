<template>
  <div class="home">
    <h3> Test functionality </h3>
    <button @click="get2">Fetch Certificates</button>
    <button @click="postCertificate">Post Certificate</button>
    <button @click="postOrganization">Post Organization</button>
    <p>{{ this.certificates }}</p>
  </div>
</template>

<script>
// @ is an alias to /src

import CertificateService from "@/services/CertificateService";
import { ServicesFactory } from "@/services/ServicesFactory";
const certificateService2 = ServicesFactory.get("certificates");
const organizationService = ServicesFactory.get("organizations");

export default {
  name: "Home",
  data() {
    return {
      certificates: {},
    };
  },
  components: {},
  methods: {
    async getCertificates() {
      const resp = await CertificateService.fetchCertificates(1);
      this.certificates = resp.data;
    },
    async get2() {
      const resp = await certificateService2.fetchCertificates(1);
      this.certificates = resp.data;
    },
    async postCertificate() {
      var req = {
        name: "New Certificate From Vue",
        organizationID: "1",
        description: "Default from Vue",
      };
      await certificateService2.createCertificate(
        req
      ).then(response => (this.responseMessage = response.data.msg))
      console.log(this.responseMessage)
      this.$alert(`${this.responseMessage}`);
    },
      async postOrganization() {
      var req = {
        name: "New Organization From Vue"
      };
      const { ResponseMessage } = await organizationService.createOrganization(
        req
      );
      this.$alert(`${ResponseMessage}`);
    },


  },
};
</script>
