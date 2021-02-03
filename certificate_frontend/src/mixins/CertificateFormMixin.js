export default {
    data(){
        return{
            form:{}
        }
    },
    mounted(){
        this.form = this.$store.getters.certificateForm;
    }
}

