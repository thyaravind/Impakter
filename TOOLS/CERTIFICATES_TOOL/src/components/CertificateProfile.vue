<template>
  <b-modal
    ref="preview-modal"
    hide-footer
    size="xl"
    :title="savePreview ? 'Certificate Preview' : 'Certificate Information'"
  >
  <h3>variant 1: Horizontal tabs</h3>
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
    <hr />
    <h3>variant 2: vertical tabs</h3>
    <b-card no-body>
      <b-tabs pills card vertical>
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
    <hr />
    <h3>variant 3: Long form</h3>
    <div>
    <b-card title="Basic Information">
      <p><b>Certificate Name:</b> {{ form.name }}</p>
      <p>Certificate Description: {{ form.description }}</p>
      <p>Priority: {{ form.priority }}</p>
      <p>Active status: {{ form.name }}</p>
    </b-card>
    <br />
    <b-card title="UN Sustainable Development Goals">
      <p v-for="(sdg, index) in form.computedSdgs" :key="index">
        {{ sdg.text }}
        <!--<span v-for="(target,index) in form.sdgTargets.filter()" :key="index">{{target}}</span>-->
      </p>
    </b-card>
    <b-card title="Industries"> </b-card>
    </div>

    <b-card>
      {{ form }}
    </b-card>
    <b-row class="buttons_row" v-if="savePreview">
      <b-button @click="add" variant="primary"> Add more details</b-button>
      <b-button @click="add" variant="primary">
        Add another Certificate</b-button
      >
    </b-row>
    <br />
    <b-row class="buttons_row" v-if="!savePreview">
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
    savePreview: Boolean,
  },
  methods: {
    showModal() {
      this.$store.dispatch("performComputations");
      this.form = this.$store.getters.certificateForm;
      this.$refs["preview-modal"].show();
    },
    add() {},
    close() {
      this.$refs["preview-modal"].hide();
    },
  },
  mixins: [CertificateFormMixin],
  mounted() {},
};
</script>