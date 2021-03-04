<template>
  <b-modal
    ref="preview-modal"
    hide-footer
    size="xl"
    :title="isSavePreview ? 'Certificate Preview' : 'Certificate Information'"
  >
    <!--<h3>variant 1: Horizontal tabs</h3>
    <b-card no-body>
      <b-tabs card>
        <b-tab title="Basic Information" active>
          <b-card-text>
            <p><b>Certificate Name:</b> {{ form.name }}</p>
            <p>Certificate Description: {{ form.description }}</p>
            <p>Priority: {{ form.priority }}</p>
            <p>Active status: {{ form.name }}</p>
          </b-card-text>
        </b-tab>
        <b-tab title="UN Sustainable Development Goals">
          <b-card-text>content</b-card-text>
        </b-tab>
        <b-tab title="Industries">
          <b-card-text>content</b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
    <hr />-->
    <!--<h3>variant 2: vertical tabs</h3>-->
    <b-card no-body v-if="!isSavePreview">
      <b-tabs pills card vertical>
        <b-tab title="Basic Information" active>
          <b-card-text>
            <p><b>Certificate Name:</b> {{ form.name }}</p>
            <p><b>Certificate Description:</b> {{ form.description }}</p>
            <p><b>Priority:</b> {{ form.priority }}</p>
            <p><b>Active status:</b> {{ form.activeStatus }}</p>
            <p><b>Goal of the certificate:</b> {{ form.goal }}</p>
            <p><b>UN SDG Engagement:</b> {{ form.sdgEngagement }}</p>
          </b-card-text>
        </b-tab>
        <b-tab title="UN Sustainable Development Goals">
          <b-card-text>
            <p v-for="(sdg, index) in form.computedSdgs" :key="index">
              {{ sdg.text }}
            </p>
          </b-card-text>
        </b-tab>
        <b-tab title="Industries">
          <b-card-text>
            <p
              v-for="(industry, index) in form.computedIndustries"
              :key="index"
            >
              {{ industry.text }}
            </p>
          </b-card-text>
        </b-tab>
      </b-tabs>
    </b-card>
    <!--<h3>variant 3: Long form</h3>-->
    <div v-if="isSavePreview">
      <b-card title="Basic Information">
        <p><b>Certificate Name:</b> {{ form.name }}</p>
        <p><b>Certificate Description:</b> {{ form.description }}</p>
        <p><b>Priority:</b> {{ form.priority }}</p>
        <p><b>Active status:</b> {{ form.activeStatus }}</p>
        <p><b>Goal of the certificate:</b> {{ form.goal }}</p>
        <p><b>UN SDG Engagement:</b> {{ form.sdgEngagement }}</p>
      </b-card>
      <br />
      <b-card title="UN Sustainable Development Goals">
        <p v-for="(sdg, index) in form.computedSdgs" :key="index">
          {{ sdg.text }}
          <!--<span v-for="(target,index) in form.sdgTargets.filter()" :key="index">{{target}}</span>-->
        </p>
      </b-card>
       <br />
      <b-card title="Industries">
        <p v-for="(industry, index) in form.computedIndustries" :key="index">
          {{ industry.text }}
        </p>
      </b-card>
    </div>
 <br />
    <b-row class="buttons_row" v-if="isSavePreview">
      <b-button @click="submit" variant="primary">Submit</b-button>
    </b-row>
    <br />
    <b-row class="buttons_row" v-if="!isSavePreview">
      <b-button @click="edit" variant="outline-danger">Edit</b-button>
      <b-button @click="deleteCert" variant="danger">Delete</b-button>
      <b-button @click="close" variant="primary"> Close</b-button>
    </b-row>
  </b-modal>
</template>

<script>
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

export default {
  name: "CertificateProfile",
  data() {
    return { form: {} };
  },
  props: {
    isSavePreview: Boolean,
  },
  methods: {
    showModal() {
      this.$store.dispatch("performComputations");
      this.form = this.$store.getters.certificateForm;
      this.$refs["preview-modal"].show();
    },
    add() {},
    submit() {
      this.$emit("submit");
    },
        edit() {
      this.$emit("edit");
    },
        delete() {
      this.$emit("delete");
    },
    close() {
      this.$refs["preview-modal"].hide();
    },
  },
  mixins: [CertificateFormMixin],
  mounted() {},
};
</script>