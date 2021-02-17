<template>
  <div>
    <h4>Please select sub industries for each industry</h4>
    <p>Current Industry: {{currentIndustryIndex}}</p>
    <b-row>    <b-form-group label="Please select all the Sub Industries:" v-slot="{ ariaDescribedby }">
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


    <b-row>
    <b-button  @click="back">Back</b-button>
    <b-button variant="primary" @click="next">Next</b-button>
  </b-row>
  </div>


</template>

<script>
import IndustryMixin from "@/mixins/IndustryMixin";

export default {
  name: "PartialSubIndustries",
  data(){return{
    selected:[],
    subindustries: []
  }},
  methods:{
    next(){
      this.$store.dispatch("addSubIndustries", this.selected);
      this.subindustries = []
      this.$emit("next");
    },
    back(){
      this.$router.go(-1)
    }

  },
  props:{ currentIndustryIndex: String},
  computed:{
    computedSubIndustries(){
      this.subIndustries.forEach(element => {
        if(element.section == this.currentIndustryIndex){
          this.subindustries.push({value:element.code,text:element.description})
        }
        
      });
      return this.subindustries

 

      //return this.sdgs[this.currentIndustryIndex].targets
    }
  },
  mounted(){
  },
  mixins:[IndustryMixin]
}
</script>

<style scoped>

</style>
