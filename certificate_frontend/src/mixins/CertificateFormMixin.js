export default {
    data(){
        return{
            form:{},
            scale: [
                { text: "Select One", value: null },
                { text: "High", value: 2 },
                { text: "Medium", value: 1 },
                { text: "Low", value: 0 },
              ],
        }
    },
    mounted(){
        this.form = this.$store.getters.certificateForm;
        
    }
}

