<template>
  <div>
    <b-container class="bv-example-row">
      <b-row>
        <b-col></b-col>
        <b-col cols="8">
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Relevance:"
              label-for="relevance"
              label-align-sm="left"
            >
              <b-form-select
                id="relevance"
                v-model="form.relevance"
                :options="scale"
              ></b-form-select>
            </b-form-group>
            <br />
            <b-form-group
              id="input-group-4"
              v-slot="{ ariaDescribedby }"
              label="How many years is the certificate valid for the stakeholder?"
              label-for="validity"
              label-align-sm="left"
            >
              <b-form-radio-group
                v-model="form.validity"
                id="validity"
                :aria-describedby="ariaDescribedby"
              >
                <b-form-radio value="<1">Less than a year</b-form-radio>
                <b-form-radio value="1">1 year</b-form-radio>
                <b-form-radio value="2">2 years</b-form-radio>
                <b-form-radio value="3">3 years</b-form-radio>
                <b-form-radio value="4">4 years</b-form-radio>
                <b-form-radio value="5+">5+ years</b-form-radio>
              </b-form-radio-group>
            </b-form-group>
            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Which regions is this certificate valid in?"
              label-for="relevance"
              label-align-sm="left"
            >
              <b-form-select
                id="relevance"
                v-model="form.region"
                :options="regions"
              ></b-form-select>
            </b-form-group>
            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Select all countires that this certificate valid in?"
              label-for="relevance"
              label-align-sm="left"
            >
              <multi-select
                :options="countries"
                :selected-options="form.countries"
                placeholder="select item"
                @select="onSelect"
              >
              </multi-select>
            </b-form-group>
            <br />
            <b-form-group
              id="input-group-4"
              v-slot="{ ariaDescribedby }"
              label="What is the goal of the certificate?"
              label-for="goal"
              label-align-sm="left"
            >
              <b-form-radio-group
                class="pt-2"
                v-model="form.goal"
                :options="goals"
                id="goal"
                :aria-describedby="ariaDescribedby"
                stacked
              >
              </b-form-radio-group>
            </b-form-group>
            <br />
            <b-form-group
              id="input-group-4"
              v-slot="{ ariaDescribedby }"
              label="Choose the option that best describes the certificate"
              label-for="rating"
              label-align-sm="left"
            >
              <b-form-radio-group
                class="pt-2"
                v-model="form.rating"
                :options="ratings"
                id="rating"
                :aria-describedby="ariaDescribedby"
                stacked
              >
              </b-form-radio-group>
            </b-form-group>
                        <b-form-group
              label-align-sm="left"
              description="As you selected other, please specify"
              v-if="form.rating == 'P3'"
            >
              <b-form-input
                id="name"
                v-model="form.ratingOther"
                placeholder="Other"
                required
              ></b-form-input>
            </b-form-group>


            <br />
            <b-form-group
              label-cols="4"
              label-cols-lg="3"
              label="Cost of the certification"
              label-for="relevance"
              label-align-sm="left"
            >
              <b-form-textarea
                id="textarea"
                v-model="form.pricing"
                placeholder="Enter the pricing details..."
                rows="3"
                max-rows="6"
              ></b-form-textarea>
            </b-form-group>

            <br />


            <b-button type="reset" variant="danger">Reset</b-button>
            <b-button type="submit" variant="primary">Proceed to SDGs</b-button>
          </b-form>
        </b-col>
        <b-col> </b-col>
      </b-row>
      <b-card class="mt-3" header="Form result so far">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </b-container>
  </div>
</template>

<script>
import { MultiSelect } from "vue-search-select";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

export default {
  data() {
    return {
      validity: [
        { text: "Select One", value: null },
        "Less than a year",
        "1 year",
        "2 years",
        "3 years",
        "4 years",
        "5+ years",
        "other",
      ],
      regions: [
        { text: "Select One", value: null },
        "Africa",
        "Asia",
        "Europe",
        "North America",
        "South America",
        "Other",
      ],
      goals: [
        "Building and Layout Evaluation",
        "Chemical Management",
        "Fibre/Fabric stewardship",
        "Process Control",
        "Traceability in the value chain",
      ],
      ratings: [
        {
          value: "P1",
          text:
            "A certificate that caters to accreditation of the broader segment of production and supply chain with a main focus on overall production",
        },
        {
          value: "P2",
          text:
            "A certificate that has a control on a specific function of the value chain of product",
        },
        { value: "P3", text: "Other" },
      ],
      show: true,
      countries: [
        { value: "1", text: "United States" },
        { value: "2", text: "United Kingdom" },
        { value: "3", text: "Germany" },
        { value: "4", text: "India" },
        { value: "5", text: "Chile" },
        { value: "6", text: "Italy" },
      ],
      searchText: "", // If value is falsy, reset searchText & searchItem
      lastSelectItem: {},

      ratingOther: null
    };
  },
  mounted() {
    
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
    onSelect(items, lastSelectItem) {
      this.form.countries = items;
      this.lastSelectItem = lastSelectItem;
    },
    reset() {
      this.items = []; // reset
    },
  },
  components: { MultiSelect },
  mixins: [CertificateFormMixin],
};
</script>


<style>
form {
  padding: 10px;
}
button {
  margin-left: 10px;
}

.label {
  font-weight: bold;
}
</style>
