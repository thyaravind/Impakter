<template>
  <div>
    <b-form-group label="Please select all the SDGs:" v-slot="{ ariaDescribedby }" label-size="lg">
      <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="sdgs"
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
import SdgMixin from "../../mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";
export default {
  name: "FormSDGs",
  data() {
    return {
      selected:[]
    }
  },
  methods:{
    next(){
      this.selected.sort((a,b)=>a-b);
      this.$store.dispatch("addSdgs", this.selected);
      this.$router.push({name:'formPage2-2'})
    },
    back(){
      this.$router.go(-1)
    }
  },
  mounted(){
  },
  mixins:[SdgMixin, CertificateFormMixin]
}
</script>

<style scoped>

#checkbox-group-1 {
  align-content:flex-end;
}

</style>
