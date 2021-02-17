<template>
  <div>
    <b-form-group label="Please select all the Industries:" v-slot="{ ariaDescribedby }" label-size="lg">
      <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="industries"
          :aria-describedby="ariaDescribedby"
          name="flavour-1"
          
          stacked
      ></b-form-checkbox-group>
    </b-form-group>

    <b-button  @click="back">Back</b-button>
    <b-button variant="primary" @click="next">Next</b-button>
    <b-card class="mt-3" header="Form result so far">
    <pre class="m-0">{{ form }}</pre>
  </b-card>
  </div>

</template>

<script>
import IndustryMixin from "../../mixins/IndustryMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
export default {
  name: "FormIndustries",
  data() {
    return {
      selected:[]
    }
  },
  methods:{
    next(){
      this.selected.sort();
      this.$store.dispatch("addIndustries", this.selected);
      this.$router.push({name:'formPage3-2'})
    },
    back(){
      this.$router.go(-1)
    }
  },
  mounted(){
    this.selected = this.form.industries
  },
  mixins:[IndustryMixin, CertificateFormMixin]
}
</script>

<style scoped>

#checkbox-group-1 {
  align-content:flex-end;
}

</style>
