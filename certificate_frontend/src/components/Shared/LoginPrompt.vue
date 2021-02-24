<template>
<div>

    <p v-if="!isLoginFailed"> Please login first</p>
    <p v-if="isLoginFailed">Please enter a valid Org ID</p>
    <b-button @click = "login"> Login </b-button>
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

</style>