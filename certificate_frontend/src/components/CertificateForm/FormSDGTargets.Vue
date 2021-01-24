<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="6"><h4>You selected the following SDGs</h4>


        <b-card class="mt-3" header="Form Data Result">
          <pre class="m-0">{{ form }}</pre>
        </b-card>
      </b-col>
      <b-col><SubSDGTargets :current-sdg-index=currentSdgIndex /></b-col>
    </b-row>
    <b-row>
      <b-button variant="primary" @click="next">Next</b-button>
    </b-row>
  </b-container>
</template>

<script>
import SubSDGTargets from "@/components/CertificateForm/SubSDGTargets";

export default {
  name: "FormSDGtargets",
  components:{SubSDGTargets},
  data(){
    return {
      form:{},
      currentSdgIndex:null,
      sdgIndex: 0,
    }
  },
  methods:{

    next(){
      this.sdgIndex++;
      if(this.sdgIndex<this.form.sdgs.length){
        this.currentSdgIndex = this.form.sdgs[this.sdgIndex]
      }
      else this.$router.push({name:'formPage3'})

    }
  },
  computed:{


  },
  mounted(){
    this.form = this.$store.getters.certificateForm;
    this.sdgIndex = 0;
    this.currentSdgIndex = this.form.sdgs[this.sdgIndex]
  }
}
</script>

<style scoped>

</style>
