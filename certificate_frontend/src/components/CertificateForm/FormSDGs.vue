<template>
  <div>
    <b-form-group label="Using options array:" v-slot="{ ariaDescribedby }">
      <b-form-checkbox-group
          id="checkbox-group-1"
          v-model="selected"
          :options="sdgs"
          :aria-describedby="ariaDescribedby"
          name="flavour-1"
          stacked
      ></b-form-checkbox-group>
    </b-form-group>
    <b-button variant="primary" @click="next">Next</b-button>
  </div>

</template>

<script>
export default {
  name: "FormSDGs",
  data() {
    return {
      sdgs: [{value:0,text:"SDG 1 No Poverty"},
        {value:1,text:"SDG 2 Zero Hunger"},
        {value:2,text:"SDG 3 Good Health and Well-Being"},
        {value:3,text:"SDG 4 Quality Education"},
        {value:4,text:"SDG 5 Gender Equality"},
        {value:5,text:"SDG 6 Clean Water and Sanitation"}
        ],
      selected:[]
    }
  },
  methods:{
    next(){
      this.selected.sort();
      this.$store.commit("addSdgs", this.selected);
      this.$router.push({name:'formPage2-2'})
    }
  }
}
</script>

<style scoped>

</style>
