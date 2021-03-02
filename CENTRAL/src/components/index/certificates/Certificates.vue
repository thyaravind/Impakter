<template>
  <div>
    <div id="main_heading">
      <h2>Certificates</h2>
    </div>
    <br />
    <b-container>
        <b-row>
            <span>filter by organization: </span>
            <b-form-select v-model="selectedOrganization" :options="computedOrganizations" @change="filterByOrg"></b-form-select>
            <!--<b-form-select v-model="selectedCountry" :options="countries"></b-form-select>-->
        </b-row>
      <b-row>
        <b-table
          :fields="fields"
          :items="certificates"
          :head-variant="light"
          :bordered="false"
          id="main_table"
          :per-page="perPage"
          :current-page="currentPage"
        >
          <template #head(name)>
            <div class="text-nowrap">Certificate Name</div>
          </template>
          <template #cell(name)="data">
            <a>{{ data.item.name }} </a>
          </template>
          <template #head(activeStatus)>
            <div
              class="text-nowrap"
              v-b-tooltip.hover
              title="Whether the certificate is currently active or not"
              variant="secondary"
            >
              Active
            </div>
          </template>
          <template #cell(activeStatus)="row">
            <span></span>
            <b-form-checkbox
              v-model="row.item.activeStatus"
              name="data.index"
              @change="updateStatus(row.index)"
              switch
            >
              <!--<b>{{ row.item.activeStatus }}</b>-->
            </b-form-checkbox>
          </template>
          <template #head(computedPriority)>
            <div
              class="text-nowrap"
              v-b-tooltip.hover
              title="How important is it to attain this certificate for a given company?"
              variant="secondary"
            >
              Priority
            </div>
          </template>
          <template #head(sdgs)>
            <div
              class="text-nowrap"
              v-b-tooltip.hover
              title=" United Nations - Sustainable Development Goals"
              variant="secondary"
            >
              SDGs
            </div>
          </template>
          <template #cell(sdgs)="data">
            <div>
              <span v-for="(sdg, index) in data.item.sdgs" :key="index"
                >{{ sdg
                }}<span v-if="index != data.item.sdgs.length - 1"
                  >,
                </span></span
              >
            </div>
          </template>
          <template #head(industries)>
            <div
              class="text-nowrap"
              v-b-tooltip.hover
              title="The ISIC Industry sectors where this ceritificate is valid in"
              variant="secondary"
            >
              Industries
            </div>
          </template>

          <template #cell(industries)="data">
            <div>
              <span
                v-for="(industry, index) in data.item.industries"
                :key="index"
                >{{ industry
                }}<span v-if="index != data.item.industries.length - 1"
                  >,
                </span></span
              >
            </div>
          </template>
          <template #cell(actions)="data">
            <b-button @click="copy(data.index)" variant="success"
              >Copy</b-button
            >
            <b-button @click="edit(data.index)" variant="outline-danger"
              >Edit</b-button
            >
            <!--<b-button>See Details</b-button>-->
          </template>
        </b-table>
      </b-row>

      <div id="paginate">
        <b-pagination
          v-model="currentPage"
          :total-rows="rows"
          :per-page="perPage"
          aria-controls="main_table"
          align="center"
          pills
        ></b-pagination>
      </div>
      <b-button variant="outline-primary" @click="add">
        Add New Certificate</b-button
      >
    </b-container>
  </div>
</template>


<script>
export default {
  name: "Certificates",
  data() {
    return {
      perPage: 6,
      currentPage: 1,
      certificates: [],
      organizations: [],
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
      selectedOrganization: "All",
      selectedCountry: "select country",
      countries:["select country","USA"],
      wholeSelectedOrganization: null
    };
  },
  async mounted() {
    this.$store.dispatch("fetchOrganizations")
    this.organizations = this.$store.getters.organizations;
    this.$store.dispatch("fetchCertificates")
    this.certificates = this.$store.getters.certificates;
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
    filterByOrg(){
        console.log("filtering by Org")
        this.certificates = this.$store.getters.certificates;
        if(this.selectedOrganization.value != "All"){
            this.wholeSelectedOrganization = this.organizations.filter(x => x.name == this.selectedOrganization)
            this.certificates = this.certificates.filter(x => x.organizationID == this.wholeSelectedOrganization[0].organizationID)
        }
        
    }
  },
  computed: {
    rows() {
      return this.certificates.length;
    },
    computedOrganizations(){
        var newOrgs = this.organizations.map(x=>  x.name)
        newOrgs.unshift("All")
        return newOrgs
    }
  },
};
</script>

<style scoped>
#main_head {
  display: flex;
  position: fixed;
  justify-content: flex-start;
  background-color: white;
  z-index: 80;
  width: 100%;
}

table {
  margin-top: 0px;
}

select{
    display: inline;
}
</style>