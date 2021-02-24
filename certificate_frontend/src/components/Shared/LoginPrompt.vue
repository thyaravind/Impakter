<template>
<div>

    <p v-if="!isLoginFailed"> Please login using your Organization's Unique Identifier provided by Impakter. If you haven't received it, please contact Impakter administrator</p>
    <p v-if="isLoginFailed" class="fail">Please enter a valid organization identifier or contact Impakter admin for assistance</p>
    <b-row class="buttons_row">
    <b-button @click = "login" variant="primary"> Log me in </b-button>
    <b-button href="mailto:aravind.samala@impakter.com"> Request Access Identifier </b-button>
    </b-row>
</div>
</template>

<script>
export default {
  name: "LoginPrompt",
  data(){
    return {
      isLoginFailed: false
    }

  },
  methods:{
    login(){
      this.$router.push("/login")
    }
  },
  mounted(){
    this.isLoginFailed = this.$store.state.orgLoginFailed

  }
}
</script>

<style scoped>

.fail{
  color: red;
}
</style>