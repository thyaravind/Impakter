<template>
  <div>
      <div id="main_heading">
        <h2>Welcome, {{ organization.organizationName }}</h2>
      </div>
    <br />
    <b-table :fields="fields" :items="certificates">
      <template #head(name)>
        <div class="text-nowrap">Certificate Name</div>
      </template>
      <template #cell(name)="data">
        <a>{{ data.item.name }} </a>
      </template>
      <template #cell(activeStatus)="row">
        <b-form-checkbox
          v-model="row.item.activeStatus"
          name="data.index"
          @change="updateStatus(row.index)"
          switch
        >
          <b>{{ row.item.activeStatus }}</b>
        </b-form-checkbox>
      </template>
      <template #head(computedPriority)>
        <div class="text-nowrap">Priority</div>
      </template>
      <template #head(sdgs)>
        <div class="text-nowrap">SDGs</div>
      </template>
      <template #cell(actions)="data">
        <b-button @click="copy(data.index)" variant="success">Copy</b-button>
        <b-button @click="edit(data.index)" variant="outline-danger"
          >Edit</b-button
        >
        <!--<b-button>See Details</b-button>-->
      </template>
    </b-table>
    <b-button variant="outline-primary" @click="add"> Add Certificate</b-button>
  </div>
</template>


<script>
export default {
  name: "OrgHome",
  data() {
    return {
      certificates: [],
      organization: {},
      organizationIdentifier: null,
      response: null,
      InProgress: true,
      networkConnected: null,
      fields: [
        "name",
        "computedPriority",
        "sdgs",
        "industries",
        "activeStatus",
        "actions",
      ],
    };
  },
  async mounted() {
    this.certificates = this.$store.getters.certificates;
    this.organization = this.$store.getters.organization;
    this.networkConnected = this.$store.getters.isNetworkConnected;
    if (this.networkConnected == false) {
      setTimeout(() => {
        this.$alert("Network failure: Please contact Administrator");
      }, 500);
    }
  },
  methods: {
    add() {
      this.$store.dispatch("changeMode", "new");
      this.$store.dispatch("resetCertificate");
      this.$store.dispatch("resetComputed");
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
    updateStatus(index) {
      this.$store.dispatch("updateCertificateStatus", this.certificates[index]);
      setTimeout(() => {
        this.$alert(this.$store.responseMessage);
      }, 1000);
      this.$store.responseMessage = "_blank_";
    },
  },
};
</script>

<style scoped>
butt CertificateProfileon {
  margin-left: 10px;
}

h2 {
  align-self: left;
}

#main_heading {
  display: flex;
  position: fixed;
  justify-content: flex-start;
  background-color: white;
  z-index: 80;
  width: 100%;
}

table {
  margin-top: 40px;
}
</style>