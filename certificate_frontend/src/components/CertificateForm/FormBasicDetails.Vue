<template>
  <div>

    <b-container class="bv-example-row">
      <b-row>
        <b-col></b-col>
        <b-col cols="8">
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">

            <b-form-group label-cols="4" label-cols-lg="3" label="Name of the Certificate:" label-for="name" label-align-sm="left" description="Ex: Rain Forest Alliance">
              <b-form-input
                  id="name"
                  v-model="form.name"
                  placeholder="Name"
                  required
              ></b-form-input>
            </b-form-group>

            <b-form-group label-cols="4" label-cols-lg="3" label="Level of Difficulty:" label-for="difficulty" label-align-sm="left">
              <b-form-select
                  id="difficulty"
                  v-model="form.difficulty"
                  :options="scale"
              ></b-form-select>
            </b-form-group>

            <b-form-group label-cols="4" label-cols-lg="3" label="Relevance:" label-for="relevance" label-align-sm="left">
              <b-form-select
                  id="relevance"
                  v-model="form.relevance"
                  :options="scale"
              ></b-form-select>
            </b-form-group>



            <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }" label="How many years is the certificate valid for the stakeholder?" label-for="input-3" label-align-sm="left">
              <b-form-radio-group
                  v-model="form.validity"
                  id="checkboxes-4"
                  :aria-describedby="ariaDescribedby"
              >
                <b-form-radio value="<1">Less than a year</b-form-radio>
                <b-form-radio value="1">1 year</b-form-radio>
                <b-form-radio value="2">2 years</b-form-radio>
                <b-form-radio value="3">3 years</b-form-radio>
              </b-form-radio-group>
            </b-form-group>

            <b-form-group label-cols="4" label-cols-lg="3" label="Which regions is this certificate valid in?" label-for="relevance" label-align-sm="left">
              <b-form-select
                  id="relevance"
                  v-model="form.region"
                  :options="regions"
              ></b-form-select>
            </b-form-group>

            <multi-select :options="countries"
                          :selected-options="form.countries"
                          placeholder="select item"
                          @select="onSelect">
            </multi-select>


            <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }" label="What is the goal of the certificate?" label-for="input-3" label-align-sm="left">
              <b-form-radio-group
                  class="pt-2"
                  v-model="form.goal"
                  :options="goals"
                  id="checkboxes-4"
                  :aria-describedby="ariaDescribedby"
                  stacked
              >
              </b-form-radio-group>
            </b-form-group>

            <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }" label="Choose the option that best describes the certificate" label-for="input-3" label-align-sm="left">
              <b-form-radio-group
                  class="pt-2"
                  v-model="form.rating"
                  :options="ratings"
                  id="checkboxes-4"
                  :aria-describedby="ariaDescribedby"
                  stacked
              >
              </b-form-radio-group>
            </b-form-group>

            <b-form-group label-cols="4" label-cols-lg="3" label="Cost of the certification" label-for="relevance" label-align-sm="left">
              <b-form-textarea
                  id="textarea"
                  v-model="form.pricing"
                  placeholder="Enter the pricing details..."
                  rows="3"
                  max-rows="6"
              ></b-form-textarea>
            </b-form-group>


            <b-button type="reset" variant="danger">Reset</b-button>
            <b-button type="submit" variant="primary">Next</b-button>
          </b-form>

        </b-col>
        <b-col></b-col>
      </b-row>
    </b-container>

  </div>
</template>

<script>
import { MultiSelect } from 'vue-search-select'


export default {
  data() {
    return {
      form:{},
      scale: [
        { text: "Select One", value: null },
        "High",
        "Medium",
        "Low"
      ],
      validity: [
        { text: "Select One", value: null },
        "Less than a year",
        "1 year",
        "2 years",
          "3 years",
          "4 years",
          "5+ years",
          "other"
      ],
      regions: [
        { text: "Select One", value: null },
        "Africa",
        "Asia",
        "Europe",
        "North America",
        "South America",
        "Other"
      ],
      goals:["Building and Layout Evaluation","Chemical Management","Fibre/Fabric stewardship","Process Control","Traceability in the value chain"],
      ratings:["P1: a certificate that caters to accreditation of the broader segment of production and supply chain with a main focus on overall production","P2: a certificate that has a control on a specific function of the value chain of product","P3: none of the above"],
      show: true,
      countries:[{ value: '1', text: 'United States'},{ value: '2', text: 'United Kingdom'},{ value: '3', text: 'Germany'}],

      options: [
        { value: '1', text: 'United States' + ' - ' + '1' },
        { value: '2', text: 'United Kingdom' + ' - ' + '2' },
        { value: '3', text: 'bc' + ' - ' + '3' },
        { value: '4', text: 'cd' + ' - ' + '4' },
        { value: '5', text: 'de' + ' - ' + '5' }
      ],
      searchText: '', // If value is falsy, reset searchText & searchItem
      lastSelectItem: {}
    };
  },
  mounted(){
    this.form = this.$store.getters.certificateForm;
  },
  methods: {
    async onSubmit(event) {
      event.preventDefault();
      //alert(JSON.stringify(this.form));
      await this.$store.commit("changeCertificate", this.form);
      this.$router.push({name:'formPage2-1'})
    },
    onReset(){

    },
    onSelect (items, lastSelectItem) {
      this.form.countries = items
      this.lastSelectItem = lastSelectItem
    },
    reset () {
      this.items = [] // reset
    },
  },
  components:{MultiSelect}
};
</script>


<style>
form{
  padding: 10px;
}
button{
  padding: 10px;
}


</style>
