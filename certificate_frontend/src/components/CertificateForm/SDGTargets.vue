<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="6"
        ><h3>You selected the following SDGs</h3>

        <div v-for="index in form.sdgs" :key="index">
          <h5 :class="index === currentSdgIndex ? 'bold' : ''">
            {{ sdgs[index - 1].text }}
          </h5>
        </div>
      </b-col>
      <b-col
        ><SubSDGTargets @next="next" :current-sdg-index="currentSdgIndex"
      /></b-col>

    </b-row>

    <b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
          <b-modal ref="proceed-modal" hide-footer>
        <h4>The Certificate: "{{form.name}}" - {{ this.responseMessage }}</h4>
        <b-button @click="addMore" variant="primary"> Add more details</b-button>
        <br>
        <b-button @click="addNew"> Add another Certificate</b-button>
        <br>
        <b-button to="/organization/home">Go to my certificates</b-button>
      </b-modal>
  </b-container>
</template>

<script>
import SubSDGTargets from "@/components/CertificateForm/SubSDGTargets";
import { ServicesFactory } from "@/services/ServicesFactory";
import SdgMixin from "@/mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

const certificateService = ServicesFactory.get("certificates");
export default {
  name: "FormSDGtargets",
  components: { SubSDGTargets },
  data() {
    return {
      currentSdgIndex: null,
      sdgIndex: 0,
      responseMessage: null
    };
  },
  methods: {
    async next() {
      this.sdgIndex++;
      if (this.sdgIndex < this.form.sdgs.length) {
        this.currentSdgIndex = this.form.sdgs[this.sdgIndex];
      } else {
        var req = this.$store.getters.payload;
        var mode = this.$store.getters.mode;

        if (mode == "edit") {
          await certificateService
            .updateCertificate(req)
            .then((response) => (this.responseMessage = response.data.msg));
        } else {
          await certificateService
            .createCertificate(req)
            .then((response) => (this.responseMessage = response.data.msg));
        }

        this.$store.dispatch("resetCertificate");
        //this.$alert(`${this.responseMessage}`);
        this.$refs["proceed-modal"].show();
      }

      //else this.$router.push({name:'formPage3'})
    },
    back() {},
    addMore() {
      this.$router.push({ name: "formPart2" });
    },
    addNew() {
      this.$store.dispatch("resetCertificate");
      this.$router.push({ name: "formPage1" });
    },
  },
  computed: {},
  mounted() {
    this.sdgIndex = 0;
    this.currentSdgIndex = this.form.sdgs[this.sdgIndex];
  },
  mixins: [SdgMixin, CertificateFormMixin],
};
</script>

<style scoped>
.bold {
  color: #41b883;
}
button{
  margin-bottom: 5px;
}
</style>
