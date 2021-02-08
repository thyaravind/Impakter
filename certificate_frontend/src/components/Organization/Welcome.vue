<template>
  <div>

      <b-form-group
        label-cols="4"
        label-cols-lg="3"
        label="Please enter your Organization Unique Identifier:"
        label-for="Identifier"
        label-align-sm="left"
        description="Ex: XHKHSDAISRKLA"
      >
        <b-form-input
          id="identifier"
          v-model="identifier"
          placeholder="Unique Identifier"
          required
        ></b-form-input>
      </b-form-group>
<b-button @click="go">Go to my Certificates</b-button>
  </div>
</template>

<script>


export default {
  name: "Welcome",
  data() {
    return {
      identifier:null,
    };
  },
  methods: {
    async go() {this.$router.push({name:'OrgHome'})
      this.$store.dispatch("setOrganizationID",this.identifier)
        
    },
  },
};
</script>