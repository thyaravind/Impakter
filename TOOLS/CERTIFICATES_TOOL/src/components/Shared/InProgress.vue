<template>
<div>
    <b-alert v-if="InProgress" show variant="primary">Refreshing Certificates...</b-alert>
</div>
</template>

<script>
export default {
  name: "InProgress",
  data(){
      return {
          InProgress: true
      }

  },
  async mounted(){
      await this.$store.dispatch("fetchOrganization");
      await this.$store.dispatch("fetchCertificates");
      await this.$store.dispatch("changeLoginStatus");
    setTimeout(() => { this.$router.push({ name: "OrgHome" }); }, 2000);
  },
  methods:{
    login(){
      
    }
  }
}
</script>

<style scoped>

</style>