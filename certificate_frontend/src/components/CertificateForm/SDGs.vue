<template>
  <div>
    <b-container>
      <b-row>
        <h4>
          Please select all the Sustainable Development Goals (SDGs) applicable
          to this certificate
        </h4>
      </b-row>
      <b-row>
        <b-col> </b-col>
        <b-col cols="6">
          <b-form-group v-slot="{ ariaDescribedby }" label-size="lg">
            <b-form-checkbox-group
              id="checkbox-group-1"
              v-model="selected"
              :options="sdgs"
              :aria-describedby="ariaDescribedby"
              name="flavour-1"
              stacked
            ></b-form-checkbox-group>
          </b-form-group>

          <b-button @click="back">Back</b-button>
          <b-button variant="primary" @click="next">Next</b-button>
        </b-col>
        <b-col> </b-col>
      </b-row>
    </b-container>
    <b-card class="mt-3" header="Form result so far">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
import SdgMixin from "../../mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import FormGuardMixin from "@/mixins/FormGuardMixin";
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
};
</script>

<style scoped>
#checkbox-group-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}
</style>
