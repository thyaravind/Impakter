
<template>
  <div>
    <h4>Industry Description</h4>
    <b-row>

      <b-form-group
        label="Please select the industry description that applies to this certificate:"
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
        <b-button variant="primary" @click="next">{{currentIndustryIndex == form.industries[form.industries.length - 1]?"Review & Submit" : "Next"}}</b-button>
        
    </b-row>
        <certificate-profile
      ref="preview_modal"
      :isSavePreview="true"
    ></certificate-profile>
  </div>
</template>

<script>
import IndustryMixin from "@/mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
import CertificateProfile from "../CertificateProfile.vue";

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
      if(this.currentIndustryIndex == this.form.industries[this.form.industries.length - 1]){
        this.$emit("isLast");
      }
      this.$store.dispatch("addSubIndustries", this.selected);
      this.subindustries = [];
      this.$emit("next");
      window.scrollTo(0, 0);     
 
    },
    back() {
        this.$emit("back");
    },
    skip(){
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
  components:{CertificateProfile}
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
