<template>
  <div>
    <b-jumbotron>
      <template #lead>
        {{ CurrentQuestionObj.question }}
      </template>

      <hr class="my-4" />
      <b-list-group>
        <b-list-group-item v-for="(answer, index) in answers" :key="index" @click.prevent="selectedAnswer(index)"> {{ index + 1 }}. {{ answer }}</b-list-group-item>
      </b-list-group>

      <b-button variant="primary" href="#">Submit</b-button>
      <b-button variant="success" @click="next" href="#">Next</b-button>
    </b-jumbotron>
  </div>
</template>

<script>
export default {
  props: {
    CurrentQuestionObj: Object,
  },
  data(){
      return {selectedIndex: null}

  },
  methods: {
    next: function () {
      this.$emit("next");
    },
    selectedAnswer(index){
        this.selectedIndex = index;

    }
  }

</script>

<style scoped>
.list-group {
    margin-bottom:10px;
}

.btn{
    margin: 0 10px;
}

.list-group-item:hover{
background: #EEE;
cursor: pointer;
}
</style>