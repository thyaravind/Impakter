
<template>
  <div>
    <h4>Please select sub industry sectors for each industry</h4>
    <p>Current Industry: {{ currentIndustryIndex }}</p>
    <b-row>

      <b-form-group
        label="Please select all the sub industries that applies to this certificate:"
        v-slot="{ ariaDescribedby }"
      >
        <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="computedSubIndustries"
          :aria-describedby="ariaDescribedby"
          name="flavour-1"
          stacked
        ></b-form-checkbox-group>
      </b-form-group>
    </b-row>

    <b-row class="buttons_row">
        <b-button @click="back">Previous</b-button>
        <b-button variant="primary" @click="next">{{currentIndustryIndex == form.industries[form.industries.length - 1]?"Submit" : "Next"}}</b-button>
        <b-button @click="skip" variant="outline-primary">Skip & Submit</b-button>
    </b-row>
  </div>
</template>

<script>
import IndustryMixin from "@/mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

export default {
  name: "PartialSubIndustries",
  data() {
    return {
      selected: [],
      subindustries: [],
    };
  },
  methods: {
    next() {
      this.$store.dispatch("addSubIndustries", this.selected);
      this.subindustries = [];
      this.$emit("next");
      window.scrollTo(0, 0);
    },
    back() {
        this.$emit("back");
    },
    skip(){
      this.$emit("submit");
    }
  },
  props: { currentIndustryIndex: String },
  computed: {
    computedSubIndustries() {
      this.subIndustries.forEach((element) => {
        if (element.section == this.currentIndustryIndex) {
          this.subindustries.push({
            value: element.code,
            text: element.description,
          });
        }
      });
      return this.subindustries;

      //return this.sdgs[this.currentIndustryIndex].targets
    },
  },
  mounted() {
    this.selected = this.form.industrySectors;
  },
  mixins: [IndustryMixin,CertificateFormMixin],
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
