<template>
  <div>
    <h4>Please select sub SDG targets for each SDG</h4>
    <p>Current SDG Index: {{currentSdgIndex}}</p>
    <b-row>    <b-form-group label="Please select all the SDG targets:" v-slot="{ ariaDescribedby }">
      <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="targets"
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
export default {
  name: "SubSDGTargets",
  data(){return{
    sdgs:[],
    selected:[]
  }},
  methods:{
    next(){
      this.$store.commit("addSdgTargets", this.selected);
      this.$emit("next");
    }

  },
  props:{ currentSdgIndex: String},
  computed:{
    targets(){
      return this.sdgs[this.currentSdgIndex].targets
    }
  },
  mounted(){
    this.sdgs = this.$store.getters.sdgs;
  }
}
</script>

<style scoped>

</style>
