<template>
  <div>
    <div id="main_heading">
      <h2>Certificate Providers</h2>
    </div>
    <br />
    <b-container>
      <b-row>
        <b-table
          :fields="fields"
          :items="organizations"
          :head-variant="light"
          :bordered="false"
          id="main_table"
          :per-page="perPage"
          :current-page="currentPage"
        >
          <template #head(name)>
            <div class="text-nowrap">Organization Name</div>
          </template>
          <template #cell(name)="data">
            <a>{{ data.item.name }} </a>
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
      </div >
      <b-row class="buttons_row">      
          <b-button variant="outline-primary" @click="add">
        Add New Organization</b-button
      ></b-row>

    </b-container>
  </div>
</template>


<script>
export default {
  name: "CertOrgs",
  data() {
    return {
      perPage: 6,
      currentPage: 1,
      organizations: [],
      organization: {},
      organizationIdentifier: null,
      response: null,
      InProgress: true,
      networkConnected: null,
      fields: [
        "name",
        "accessToken",
        "website",
        
      ],
    };
  },
  async mounted() {
    this.$store.dispatch("fetchOrganizations")
    this.organizations = this.$store.getters.organizations;
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
      this.$store.dispatch("resetOrganization");
      this.$store.dispatch("setOrgType","certificate");
      this.$router.push({ name: "OrgFormPage1" });
    },
    edit(index) {
      this.$store.dispatch("changeOrganization", this.organizations[index]);
      this.$store.dispatch("changeMode", "edit");
      this.$router.push({ name: "OrgFormPage1" });
    },

  },
  computed: {
    rows() {
      return this.organizations.length;
    },
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
</style>