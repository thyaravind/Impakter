<template>
  <b-container class="bv-example-row">
    <b-row>
      <b-col cols="6"><h3>You selected the following SDGs</h3>

        <div v-for="index in form.sdgs" :key="index"
        ><h5 :class="index===currentSdgIndex?'bold':''">{{sdgs[index].text}}</h5></div>




      </b-col>
      <b-col><SubSDGTargets @next="next" :current-sdg-index=currentSdgIndex /></b-col>
    </b-row>

    <b-card class="mt-3" header="Form result so far">
    <pre class="m-0">{{ form }}</pre>
  </b-card>
  </b-container>
</template>

<script>
import SubSDGTargets from "@/components/CertificateForm/SubSDGTargets";
import {ServicesFactory} from '@/services/ServicesFactory'
import SdgMixin from "@/mixins/SdgMixin";
import CertificateFormMixin from "@/mixins/CertificateFormMixin";

const certificateService = ServicesFactory.get("certificates")
export default {
  name: "FormSDGtargets",
  components:{SubSDGTargets},
  data(){
    return {
      currentSdgIndex:null,
      sdgIndex: 0,
    }
  },
  methods:{

    async next(){
      this.sdgIndex++;
      if(this.sdgIndex<this.form.sdgs.length){
        this.currentSdgIndex = this.form.sdgs[this.sdgIndex]
      }
      else {
      var req = this.$store.getters.payload

      if(this.form.mode == "edit"){
              await certificateService.updateCertificate(
        req
      ).then(response => (this.responseMessage = response.data.msg))

      }
      else{
        await certificateService.createCertificate(
        req
      ).then(response => (this.responseMessage = response.data.msg))

      }

      this.$store.dispatch("resetCertificate");
      this.$alert(`${this.responseMessage}`);

        }

      //else this.$router.push({name:'formPage3'})

    },
    back(){

    }
  },
  computed:{


  },
  mounted(){
    this.sdgIndex = 0;
    this.currentSdgIndex = this.form.sdgs[this.sdgIndex]
  },
  mixins:[SdgMixin,CertificateFormMixin]
}
</script>

<style scoped>

.bold{
  color:#41b883;
}
</style>
