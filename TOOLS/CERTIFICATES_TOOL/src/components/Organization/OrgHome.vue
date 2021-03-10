<template>
  <div>
    <!--<div >
        <b-card no-body>
    <b-tabs pills card vertical>
      <b-tab title="My Certificates" active>
        <b-card-text>
        <b-table
          :fields="fields"
          :items="certificates"
          :head-variant="light"
          :bordered="false"
          id="main_table"
          :per-page="perPage"
          :current-page="currentPage"
          hover
        >
          <template #head(name)>
            <div class="text-nowrap">Certificate Name</div>
          </template>
          <template #cell(name)="data">
            <p
              @click="
                view(data.index);
                $refs.preview_modal.showModal();
              "
              class="certificateName"
            >
              {{ data.item.name }}
            </p>
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
            
          </template>
        </b-table>
        </b-card-text>
        </b-tab>
      <b-tab title="My Profile"><b-card-text>Tab contents 2</b-card-text></b-tab>
      <b-tab title="Tab 3"><b-card-text>Tab contents 3</b-card-text></b-tab>
    </b-tabs>
  </b-card>
    </div>-->
    <br />
    <b-container>
      <b-row>
        <b-col
          ><h2>Welcome, {{ organization.organizationName }}</h2>
        </b-col>
        <b-col cols="3">
          <b-button variant="outline-primary" @click="add">
            Add New Certificate</b-button
          >
        </b-col>
      </b-row>
      <b-row>
        <p></p>
      </b-row>

      <b-row> </b-row>
      <b-row>
        <b-table
          :fields="fields"
          :items="certificates"
          :head-variant="light"
          :bordered="false"
          id="main_table"
          :per-page="perPage"
          :current-page="currentPage"
          hover
        >
          <template #head(name)>
            <div class="text-nowrap">Certificate Name</div>
          </template>
          <template #cell(name)="data">
            <p
              @click="
                view(data.item);
                $refs.preview_modal.showModal();
              "
              class="certificateName"
            >
              {{ data.item.name }}
            </p>
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
              @change="updateStatus(row.item)"
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
            <b-button @click="copy(data.item)" variant="success">Copy</b-button>
            <b-button @click="edit(data.item)" variant="outline-danger"
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
    </b-container>
    <certificate-profile
      ref="preview_modal"
      :isSavePreview="false"
      @edit="editFromProfile"
      @delete="delet"
    ></certificate-profile>
  </div>
</template>


<script>
import compute from "@/models/compute";
import CertificateProfile from "../CertificateProfile.vue";

export default {
  name: "OrgHome",
  data() {
    return {
      showModal: false,
      perPage: 5,
      currentPage: 1,
      sortBy: "name",
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
    this.certificates = this.$store.getters.certificates.sort(
      compute.compareByName
    );
    this.organization = this.$store.getters.organization;
    this.networkConnected = this.$store.getters.isNetworkConnected;
    if (this.networkConnected == false) {
      setTimeout(() => {
        this.$alert("Network failure: Please contact Administrator");
      }, 500);
    }
  },
  components: { CertificateProfile },
  methods: {
    add() {
      this.$store.dispatch("changeMode", "new");
      this.$store.dispatch("resetCertificate");
      this.$store.dispatch("resetComputed");
      this.$router.push({ name: "formPage1" });
    },
    copy(item) {
      this.$store.dispatch("changeMode", "new");
      this.$store.dispatch("changeCertificate", item);
      this.$router.push({ name: "formPage1" });
    },
    edit(item) {
      this.$store.dispatch("changeCertificate", item);
      this.$store.dispatch("changeMode", "edit");
      this.$router.push({ name: "formPage1" });
    },
    updateStatus(item) {
      this.$store.dispatch("updateCertificateStatus", item);
      setTimeout(() => {
        this.$alert(this.$store.responseMessage);
      }, 1000);
      this.$store.responseMessage = "_blank_";
    },
    view(item) {
      console.log(item);
      this.$store.dispatch("changeCertificate", item);
      setTimeout(() => {}, 500);
    },
    view2(record, index) {
      this.$store.dispatch("changeCertificate", this.certificates[index]);
      this.$router.push({ name: "CertificateProfile" });
    },
    delet() {
      this.$store.dispatch("deleteCertificate");
        setTimeout(() => {
        this.$alert(this.$store.responseMessage);
      }, 3000);
      this.$store.responseMessage = "_blank_";
    },
    editFromProfile() {
      this.$store.dispatch("changeMode", "edit");
      this.$router.push({ name: "formPage1" });
    },
  },
  computed: {
    rows() {
      return this.certificates.length;
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

.certificateName {
  cursor: pointer;
}

#main_heading {
  justify-content: flex-start;
}
</style>