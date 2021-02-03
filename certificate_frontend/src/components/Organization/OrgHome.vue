<template>
  <div>
    <h2>Welcome Rain Forest Alliance</h2>
    <br />
    <b-table :fields="fields" :items="certificates">
      <template #cell(actions)="data">
        <b-button @click="copy(data.index)" variant="success">Copy</b-button>
        <b-button @click="edit(data.index)" variant="outline-danger">Edit</b-button>
        <!--<b-button>See Details</b-button>-->
      </template>
    </b-table>
    <b-button variant="outline-success"> Add Certificate
    </b-button>
  </div>
</template>


<script>
export default {
  name: "OrgHome",
  data() {
    return {
      certificates: [],
      fields: ["name", "difficulty", "relevance", "validity", "actions"],
    };
  },
  mounted() {
    this.certificates = this.$store.getters.certificates;
  },
  methods: {
    copy(index) {
      this.$store.dispatch("changeCertificate", this.certificates[index]);
      this.$router.push({ name: "formPage1" });
    },
    edit(index) {
      this.$store.dispatch("changeCertificate", this.certificates[index]);
      this.$store.dispatch("changeMode", "edit");
      this.$router.push({ name: "formPage1" });
    },
  },
};
</script>

<style scoped>
b-button {
  margin: 10px;
}

h2 {
  align-self: left;
}
</style>