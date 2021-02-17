<template>
  <div>
    <b-alert v-if="InProgress" show variant="primary">Logging you in...</b-alert>
    <b-form-group
      label-cols="4"
      label-cols-lg="3"
      label="Please enter your Organization Unique Access Token:"
      label-for="Identifier"
      label-align-sm="left"
      description="Ex: XHKHSDAISRKLA"
    >
      <b-form-input
        id="identifier"
        v-model="identifier"
        placeholder="Unique Access Token"
        required
      ></b-form-input>
    </b-form-group>
    <b-button @click="login">LogIn</b-button>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      identifier: null,
      InProgress: false
    };
  },
  methods: {
    async login() {
      this.$store.dispatch("setOrganizationID", this.identifier);
      this.InProgress = true
      setTimeout(() => { this.$router.push({ name: "InProgress" }); }, 2000);
    },
  },
};
</script>