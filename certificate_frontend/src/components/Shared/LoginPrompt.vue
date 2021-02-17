<template>
<div>
    <p> Please login first</p>
    <b-button @click = "login"> Login </b-button>
</div>
</template>

<script>
export default {
  name: "LoginPrompt",
  methods:{
    login(){
      this.$router.push("/login")
    }
  }
}
</script>

<style scoped>

</style>