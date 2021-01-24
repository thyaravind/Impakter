<template>
  <div>
    <b-form-group label="Please select all the SDGs:" v-slot="{ ariaDescribedby }">
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
export default {
  name: "FormSDGs",
  data() {
    return {
      form:{},
      sdgs: [],
      selected:[]
    }
  },
  methods:{
    next(){
      this.selected.sort();
      this.$store.commit("addSdgs", this.selected);
      this.$router.push({name:'formPage2-2'})
    },
    back(){

    }
  },
  mounted(){
    this.form = this.$store.getters.certificateForm;
    this.sdgs = this.$store.getters.sdgs;
  }
}
</script>

<style scoped>

</style>
