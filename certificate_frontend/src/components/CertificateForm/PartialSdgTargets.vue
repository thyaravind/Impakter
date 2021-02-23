<template>
  <div>
    <div>
      <b>Please select applicable SDG targets for each SDG</b>
    </div>
    <br />
    <div id="scroll">
      <!--<p>Current SDG Index: {{ currentSdgIndex }}</p>-->
      <b-row>
        <b-form-group
          v-slot="{ ariaDescribedby }"
        >
          <b-form-checkbox-group
            id="checkbox-group-1"
            v-model="selected"
            :options="computedTargets"
            :aria-describedby="ariaDescribedby"
            name="flavour-1"
            stacked
          ></b-form-checkbox-group>
        </b-form-group>
      </b-row>

      <b-row class="buttons_row">
        <b-button @click="back">Back</b-button>
        <b-button variant="primary" @click="next">Next</b-button>
      </b-row>
    </div>
  </div>
</template>

<script>
import SdgMixin from "@/mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

export default {
  name: "PartialSdgTargets",
  data() {
    return {
      selected: [],
      targets: [],
    };
  },
  methods: {
    next() {
      this.$store.dispatch("addSdgTargets", this.selected);
      this.targets = [];
      this.$emit("next");
      window.scrollTo(0, 0);
    },
    back() {
      this.$store.dispatch("resetComputed");
      this.$router.go(-1);
    },
  },
  props: { currentSdgIndex: String },
  computed: {
    computedTargets() {
      this.sdgTargets.forEach((element) => {
        if (element.goal == this.currentSdgIndex) {
          this.targets.push({ value: element.code, text: element.title });
        }
      });
      return this.targets;

      //return this.sdgs[this.currentSdgIndex].targets
    },
  },
  mounted() {
    this.selected = this.form.sdgTargets;
  },
  mixins: [SdgMixin,CertificateFormMixin],
};
</script>

<style scoped>
#checkbox-group-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}
.position-fixed {
  margin-bottom: 20px;
  background-color: rgb(255, 255, 255);
  z-index: 80;
}

#scroll{
  margin-top: 0px;

}
</style>
