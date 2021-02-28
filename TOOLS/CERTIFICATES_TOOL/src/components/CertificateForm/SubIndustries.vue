<template>
  <b-container>
    <b-row>
      <progress-bar :currentStep="3"> </progress-bar>
    </b-row>
    <b-row>
      <b-col cols="6">
        <div class="position-fixed" id="subb">
          <h3>Selected industries</h3>
          <div
            v-for="(industry, index) in form.computedIndustries"
            :key="index"
          >
            <h5 :class="industry.value === currentIndustry ? 'bold' : ''">
              <i class="far fa-envelope"></i>
              {{ industry.value + ": " + industry.text }}
            </h5>
          </div>
          <br />
          <b-button @click="reselect" variant="outline-primary"
            >Reselect Industries</b-button
          >
        </div>
      </b-col>
      <b-col>
        <scroll-view>
          <template
            ><PartialSubIndustries
              @next="next"
              @back="back"
              @submit="submit"
              :current-industry-index="currentIndustry" /></template
        ></scroll-view>
      </b-col>
    </b-row>

    <!--<b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>-->
    <b-modal ref="proceed-modal" hide-footer>
      <p>Status Message:</p>
      <b-alert v-if="InProgress" show variant="primary"
        >Adding/Updating Certificate...</b-alert
      >
      <b-alert v-if="ProgressCompleted" show variant="success">{{
        this.responseMessage
      }}</b-alert>
      <b-alert v-if="ProgressFailed" show variant="danger">{{
        this.responseMessage
      }}</b-alert>
      <b-row class="buttons_row">
        <b-button @click="addMore" variant="primary">
          Add more details</b-button
        >
        <b-button @click="addNew" variant="primary">
          Add another Certificate</b-button
        >
      </b-row>
      <br />

      <div class="flex_and_center">-Or-</div>
      <b-button id="bottom_button" to="/wait">Go to my certificates</b-button>
    </b-modal>
  </b-container>
</template>

<script>
import PartialSubIndustries from "@/components/CertificateForm/PartialSubIndustries";
import { ServicesFactory } from "@/services/ServicesFactory";
const certificateService = ServicesFactory.get("certificates");

import IndustryMixin from "@/mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import SubmitMixin from "@/mixins/SubmitMixin";
import ProgressBar from "../Shared/ProgressBar.vue";

export default {
  name: "FormSubIndustries",
  components: { PartialSubIndustries, ProgressBar },
  data() {
    return {
      currentIndustry: null,
      industryIndex: 0,
    };
  },
  methods: {
    next() {
      this.industryIndex++;
      if (this.industryIndex < this.form.industries.length) {
        this.currentIndustry = this.form.industries[this.industryIndex];
      } else {
        this.submit()
      }
    },
    async submit(){
        var mode = this.$store.getters.mode;
        var req = this.$store.getters.payload;
        this.InProgress = true;
        this.$refs["proceed-modal"].show();
        if (mode == "edit") {
          //this.$alert("updating the certificate");
          await certificateService.updateCertificate(req).then((response) => {
            this.responseMessage = response.data.msg;
            this.responseStatus = response.data.status;
          });
        } else {
          await certificateService.createCertificate(req).then((response) => {
            this.responseMessage = response.data.msg;
            this.responseStatus = response.data.status;
            this.$store.state.certificate.certificateID =
              response.data.insertId;
          });
        }

        //this.$store.dispatch("resetCertificate");
        this.InProgress = false;
        if (this.responseStatus == 1) {
          this.ProgressCompleted = true;
        } else this.ProgressFailed = true;


    },
    back() {
      if (this.industryIndex == 0) {
        this.$store.dispatch("resetComputed");
        this.$router.go(-1);
      }
      this.industryIndex--;
      this.currentIndustry = this.form.industries[this.industryIndex];
    },
    addMore() {
      this.$router.push({ name: "formPart2" });
    },
    addNew() {
      this.$store.dispatch("resetCertificate");
      this.$store.dispatch("resetComputed");
      this.$router.push({ name: "formPage1" });
    },
    reselect() {
      this.$store.dispatch("resetComputed");
      this.$router.go(-1);
    },
  },
  computed: {},
  mounted() {
    this.industryIndex = 0;
    this.currentIndustry = this.form.industries[this.industryIndex];
  },
  mixins: [IndustryMixin, CertificateFormMixin, SubmitMixin],
};
</script>

<style scoped>
.bold {
  color: #41b883;
}

#subb {
  width: 500px;
}
.flex_and_center {
  display: flex;
  justify-content: center;
}

#bottom_button {
  margin-top: 10px;
  width: 100%;
}
</style>
