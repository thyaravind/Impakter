<template>
  <div>
    <b-container>
      <b-row>
        <progress-bar :currentStep="2"> </progress-bar>
      </b-row>
      <b-row class="main_row">
        <b-col> </b-col>
        <b-col cols="8">
          <b-form-group v-slot="{ ariaDescribedby }" label-size="lg" label="Please select all the Susainable Development Goals applicable to this certificate">
            <b-form-checkbox-group
              id="checkbox-group-1"
              v-model="selected"
              :options="sdgs"
              :aria-describedby="ariaDescribedby"
              name="flavour-1"
              stacked
            ></b-form-checkbox-group>
          </b-form-group>
        </b-col>
        <b-col> </b-col>
      </b-row>
      <b-row class="buttons_row">
        <b-button @click="back" class="button_group">Back</b-button>
        <b-button variant="primary" @click="next">Next</b-button>
      </b-row>
    </b-container>
    <!--<b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>-->
  </div>
</template>

<script>
import SdgMixin from "../../mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import FormGuardMixin from "@/mixins/FormGuardMixin";
import ProgressBar from "../Shared/ProgressBar.vue";
export default {
  name: "FormSDGs",
  data() {
    return {
      selected: [],
    };
  },
  methods: {
    next() {
      this.selected.sort((a, b) => a - b);
      this.$store.dispatch("addSdgs", this.selected);
      this.permitNavigation = true;
      this.$router.push({ name: "formPage2-2" });
    },
    back() {
      this.$router.go(-1);
    },
  },
  mounted() {
    this.selected = this.form.sdgs;
  },
  mixins: [SdgMixin, CertificateFormMixin, FormGuardMixin],
  components: { ProgressBar },
};
</script>

<style scoped>
</style>
