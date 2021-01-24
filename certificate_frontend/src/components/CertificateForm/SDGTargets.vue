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

export default {
  name: "FormSDGtargets",
  components:{SubSDGTargets},
  data(){
    return {
      form:{},
      sdgs:[],
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

    },
    back(){

    }
  },
  computed:{


  },
  mounted(){
    this.form = this.$store.getters.certificateForm;
    this.sdgIndex = 0;
    this.currentSdgIndex = this.form.sdgs[this.sdgIndex]
    this.sdgs = this.$store.getters.sdgs;
  }
}
</script>

<style scoped>

.bold{
  color:#41b883;
}
</style>
