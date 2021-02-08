<template>
  <div>
    <b-row>
      <b-col></b-col>
      <b-col cols="8">
          <b-form @submit="onSubmit" @reset="onReset">
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Name of the Certificate:"
              label-for="name"
              label-align-sm="left"
              description="Ex: Rain Forest Alliance"
            >
              <b-form-input
                id="name"
                v-model="form.name"
                placeholder="Name"
                required
              ></b-form-input>
            </b-form-group>
            <br />

            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Description of the Certification"
              label-for="description"
              label-align-sm="left"
            >
              <b-form-textarea
                id="description"
                v-model="form.description"
                placeholder="Please describe what this certificate is all about..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>
            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Please upload the certificate logo"
              label-for="description"
              label-align-sm="left"
            >
              <input type="file" /><b-button>Upload!</b-button>
            </b-form-group>
            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Priority level:"
              label-for="difficulty"
              label-align-sm="left"
            >
              <b-form-select
                id="difficulty"
                v-model="form.difficulty"
                :options="scale"
              ></b-form-select>
            </b-form-group>
            <br />
                        <b-button type="reset" variant="danger">Reset</b-button>
            <b-button type="submit" variant="primary">Proceed to SDGs</b-button>
          
          </b-form>
           </b-col>
      <b-col></b-col>
    </b-row>
  </div>
</template>

<script>
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

export default {
  data() {
    return {};
  },
    methods: {
    async onSubmit(event) {
      event.preventDefault();
      //alert(JSON.stringify(this.form));
      if(this.form.sdgEngagement == "5"){
        this.form.sdgEngagement = this.sdgEngagementOther
      }
      if(this.form.rating == "P3"){
        this.form.rating = this.ratingOther
      }
      
      await this.$store.dispatch("changeCertificate", this.form);
      this.$router.push({ name: "formPage2-1" });
    },
    onReset() {
      this.$store.dispatch("resetCertificate");
    },
    },
  mixins: [CertificateFormMixin],
};
</script>

<style scoped>
button {
  margin-left: 10px;
}
</style>