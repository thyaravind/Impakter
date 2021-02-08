<template>
  <div>
    <h4>Please select sub SDG targets for each SDG</h4>
    <p>Current SDG Index: {{currentSdgIndex}}</p>
    <b-row>    <b-form-group label="Please select all the SDG targets:" v-slot="{ ariaDescribedby }">
      <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="computedTargets"
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
import SdgMixin from "@/mixins/SdgMixin";

export default {
  name: "SubSDGTargets",
  data(){return{
    selected:[],
    targets:[]
  }},
  methods:{
    next(){
      this.$store.dispatch("addSdgTargets", this.selected);
      this.targets = []
      this.$emit("next");
    },
    back(){
      this.$router.go(-1)
    }

  },
  props:{ currentSdgIndex: String},
  computed:{
    computedTargets(){
      this.sdgTargets.forEach(element => {
        if(element.goal == this.currentSdgIndex){
          this.targets.push({value:element.code,text:element.title})
        }
        
      });
      return this.targets

 

      //return this.sdgs[this.currentSdgIndex].targets
    }
  },
  mounted(){
  },
  mixins:[SdgMixin]
}
</script>

<style scoped>

</style>
