export default {
    data(){
        return{
            permitNavigation: false
        }

    },
    beforeRouteLeave(to,from,next){
        if (this.permitNavigation) {
          next()
        } else {
          const answer = window.confirm('Do you really want to leave? you have unsaved changes!')
          if(answer){
            next()
          }
          else {
            next(false)
          }
          
        }
        }
}