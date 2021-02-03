<template>
  <div>

      <b-form-group
        label-cols="4"
        label-cols-lg="3"
        label="Please enter your Organization Unique Identifier:"
        label-for="Identifier"
        label-align-sm="left"
        description="Ex: XHKHSDAISRKLA"
      >
        <b-form-input
          id="identifier"
          v-model="identifier"
          placeholder="Unique Identifier"
          required
        ></b-form-input>
      </b-form-group>
<b-button @click="fetch">Fetch Certificates</b-button>
  </div>
</template>

<script>
import { ServicesFactory } from "@/services/ServicesFactory";
const certificateService = ServicesFactory.get("certificates");

export default {
  name: "Welcome",
  data() {
    return {
      identifier:null,
    };
  },
  methods: {
    async fetch() {
      this.$store.dispatch("setOrganizationID",this.identifier)
      await certificateService
        .fetchCertificates(this.identifier)
        .then((response) =>
          this.$store.dispatch("fetchCertificates", response.data)
        );
        this.$router.push({name:'OrgHome'})
    },
  },
};
</script>