<template>
  <div>
    <h2>Welcome Rain Forest Alliance</h2>
    <br />
    <b-table :fields="fields" :items="certificates">
            <template #cell(status)>
<b-form-checkbox v-model="activeStatus" name="data.index" switch>
      <b>Active</b>
    </b-form-checkbox>
      </template>
      <template #cell(actions)="data">
        <b-button @click="copy(data.index)" variant="success">Copy</b-button>
        <b-button @click="edit(data.index)" variant="outline-danger">Edit</b-button>
        <!--<b-button>See Details</b-button>-->
      </template>

    </b-table>
    <b-button variant="outline-primary" @click="add"> Add Certificate</b-button>
  </div>
</template>


<script>
import { ServicesFactory } from "@/services/ServicesFactory";
const certificateService = ServicesFactory.get("certificates");

export default {
  name: "OrgHome",
  data() {
    return {
      certificates: [],
      organizationIdentifier: null,
      response: null,
      fields: ["name", "difficulty", "relevance", "validity","status", "actions"],
      activeStatus:true
    };
  },
  async mounted() {
    this.organizationIdentifier = this.$store.getters.organizationIdentifier;
    this.response = await certificateService.fetchCertificates(
      this.organizationIdentifier
    );

    this.$store.dispatch("fetchCertificates", this.response.data);

    this.certificates = this.$store.getters.certificates;
  },
  methods: {
    add() {
      this.$store.dispatch("changeMode", "new");
      this.$router.push({ name: "formPage1" });
    },
    copy(index) {
      this.$store.dispatch("changeMode", "new");
      this.$store.dispatch("changeCertificate", this.certificates[index]);
      this.$router.push({ name: "formPage1" });
    },
    edit(index) {
      this.$store.dispatch("changeCertificate", this.certificates[index]);
      this.$store.dispatch("changeMode", "edit");
      this.$router.push({ name: "formPage1" });
    },
  },
};
</script>

<style scoped>
button {
  margin-left: 10px;
}

h2 {
  align-self: left;
}
</style>