<template>
  <div>
    <b-container>
      <b-row class="main_row">
        <b-col></b-col>
        <b-col cols="8">
          <b-form @submit="onSubmit" @reset="onReset">
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Name of the Organization:"
              label-for="name"
              label-align-sm="left"
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
              label="Website link:"
              label-for="website"
              label-align-sm="left"
            >
              <b-form-input
                id="website"
                v-model="form.website"
                placeholder="www.rainforest.com"
                required
              ></b-form-input>
            </b-form-group>
            <br />

            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Description of the Organization"
              label-for="description"
              label-align-sm="left"
              id="desc"
            >
              <b-form-textarea
                id="description"
                v-model="form.description"
                placeholder="Please describe what this Organization is all about..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>
            <b-tooltip
              target="desc__BV_label_"
              triggers="hover"
              variant="secondary"
              placement="lefttop"
            >
              Please describe the Organizaiton in around 500 words approx.
            </b-tooltip>
            <br />

            <b-row class="buttons_row">
              <b-button type="reset" variant="danger">Reset</b-button>
              <b-button type="submit" variant="primary">Submit</b-button>
            </b-row>
          </b-form>
        </b-col>
        <b-col></b-col>
      </b-row>
    <b-modal ref="proceed-modal" hide-footer>
      <p>Status Message:</p>
      <b-alert v-if="InProgress" show variant="primary"
        >Adding/Updating Organization...</b-alert
      >
      <b-alert v-if="ProgressCompleted" show variant="success">{{
        this.responseMessage
      }}</b-alert>
      <b-alert v-if="ProgressFailed" show variant="danger">{{
        this.responseMessage
      }}</b-alert>
      <b-row class="buttons_row">
        <b-button @click="addNew" variant="primary">
          Add another Organization</b-button
        >
      </b-row>
      <br />

      <div class="flex_and_center">-Or-</div>
      <b-button id="bottom_button" to="/wait">Go to Organizations</b-button>
    </b-modal>
    </b-container>
  </div>
</template>

<script>
import FormGuardMixin from "@/mixins/FormGuardMixin";
import SubmitMixin from "@/mixins/SubmitMixin";
import { ServicesFactory } from "@/services/ServicesFactory";
const organizationService = ServicesFactory.get("organizations");

export default {
  name: "OrgForm",
  data() {
    return {
      form: null,
    };
  },
  methods: {
    onReset() {
      this.$store.dispatch("resetOrganization");
    },
       async onSubmit(){
        var mode = this.$store.getters.mode;
        var req = this.$store.getters.organization;
        this.InProgress = true;
        this.$refs["proceed-modal"].show();
        if (mode == "edit") {
          //this.$alert("updating the Organization");
          await organizationService.updateOrganization(req).then((response) => {
            this.responseMessage = response.data.msg;
            this.responseStatus = response.data.status;
          });
        } else {
          await organizationService.createOrganization(req).then((response) => {
            this.responseMessage = response.data.msg;
            this.responseStatus = response.data.status;
          });
        }

        //this.$store.dispatch("resetOrganization");
        this.InProgress = false;
        if (this.responseStatus == 1) {
          this.ProgressCompleted = true;
        } else this.ProgressFailed = true;


    },
    addNew(){
      this.onReset()
      this.$refs["proceed-modal"].hide();
    }
  },
  mixins: [FormGuardMixin, SubmitMixin],
  components: {},
  mounted() {
    this.form = this.$store.getters.organization;
  },
};
</script>

<style scoped>
#rating {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}

#rating {
  margin-bottom: 10px !important;
}
</style>