<template>
  <div>
    <h1>Sub SDG Targets</h1>
    <p>Current SDG: {{currentSdgIndex}}</p>
  </div>

</template>

<script>
export default {
  name: "SubSDGTargets",
  data(){return{
    targets:[{},{},{}]
  }},
  methods:{},
  props:{ currentSdgIndex: String},

}
</script>

<style scoped>

</style>
