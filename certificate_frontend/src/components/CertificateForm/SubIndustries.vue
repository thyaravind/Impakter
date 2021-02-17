<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="6"
        ><h3>You selected the following Industries</h3>
        <div v-for="(industry,index) in form.computedIndustries" :key="index">
          <h5 :class="industry.value === currentIndustry ? 'bold' : ''">
            {{ industry.value + ": " + industry.text }}
          </h5>
        </div>
      </b-col>
      <b-col
        ><PartialSubIndustries
          @next="next"
          :current-industry-index="currentIndustry"
      /></b-col>
    </b-row>

    <b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
    <b-modal ref="proceed-modal" hide-footer>
      <b-alert v-if="InProgress" show variant="primary">Updating Certificate...</b-alert>
      <b-alert v-if="ProgressCompleted" show variant="success">{{ this.responseMessage }}</b-alert>
      <b-alert v-if="ProgressFailed" show variant="danger">{{ this.responseMessage }}</b-alert>
      <b-button @click="addMore" variant="primary"> Add more details</b-button>
      <br />
      <b-button @click="addNew"> Add another Certificate</b-button>
      <br />
      <b-button to="/wait">Go to my certificates</b-button>
    </b-modal>
  </b-container>
</template>

<script>
import PartialSubIndustries from "@/components/CertificateForm/PartialSubIndustries";
import { ServicesFactory } from "@/services/ServicesFactory";
import IndustryMixin from "@/mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

const certificateService = ServicesFactory.get("certificates");
export default {
  name: "FormSubIndustries",
  components: { PartialSubIndustries },
  data() {
    return {
      currentIndustry: null,
      industryIndex: 0,
      responseMessage: null,
      responseStatus: null,
      InProgress: false,
      ProgressCompleted: false,
      ProgressFailed: false
    };
  },
  methods: {
    async next() {
      this.industryIndex++;
      if (this.industryIndex < this.form.industries.length) {
        this.currentIndustry = this.form.industries[this.industryIndex];
      } else {
        var mode = this.$store.getters.mode;
        var req = this.$store.getters.payload;          
        this.InProgress = true
        this.$refs["proceed-modal"].show();
        if (mode == "edit") {
          //this.$alert("updating the certificate");
          await certificateService
            .updateCertificate(req)
            .then((response) => {
              this.responseMessage = response.data.msg
              this.responseStatus = response.data.status
              });
        } else {
          await certificateService
            .createCertificate(req)
            .then((response) => {
            this.responseMessage = response.data.msg
            this.responseStatus = response.data.status});
        }

        this.$store.dispatch("resetCertificate");
        this.InProgress = false
        if(this.responseStatus == 1) {
            this.ProgressCompleted = true
        }
        else this.ProgressFailed = true
        
        
      }

      //else this.$router.push({name:'formPage3'})
    },
    back() {},
    addMore() {
      this.$router.push({ name: "formPart2" });
    },
    addNew() {
      this.$store.dispatch("resetCertificate");
      this.$store.dispatch("resetComputed");
      this.$router.push({ name: "formPage1" });
    },
  },
  computed: {},
  mounted() {
    this.industryIndex = 0;
    this.currentIndustry = this.form.industries[this.industryIndex];
  },
  mixins: [IndustryMixin, CertificateFormMixin],
};
</script>

<style scoped>
.bold {
  color: #41b883;
}
button {
  margin-bottom: 5px;
}
</style>
