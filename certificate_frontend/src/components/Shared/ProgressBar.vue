<template>
  <div class="root">
     <div class="container">
          <ul class="progressbar">
            <span :class="[currentStep == 1 ? 'active': 'none']">Step 1: Basic Details </span>
            <span :class="[currentStep == 2 ? 'active': 'none']">Step 2: Sustainable Development Goals </span>
            <span :class="[currentStep == 3 ? 'active': 'none']">Step 3: Industries </span>
          </ul>
      </div>
  </div>
</template>
<script>
export default {
  props:['currentStep'],
  data () {
    return {
    }
  },
  computed: {
  classObject: function () {
    return {
      active: this.isActive && !this.error,
      'text-danger': this.error && this.error.type === 'fatal'
    }
  }
}
}
</script>

(html comment removed:  Add "scoped" attribute to limit CSS to this component only )
<style scoped>
span {
  margin-right: 70px;
}
.active{
  color:#fe6663;
  font-weight: bold;
}
.container{
  position: fixed;
  background-color: white;
  z-index: 100;
  border-radius: 25px;
  border: 1px solid #ffbab9;
}
.progressbar {
  display: inline-flex;
  margin-bottom: 0px;
  padding: 5px;
  justify-items: center;
  align-items: center;
}
.root{
    margin-bottom: 60px;
}

</style>