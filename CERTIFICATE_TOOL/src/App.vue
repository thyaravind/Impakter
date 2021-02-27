<template>
  <div id="app">
    <b-container>
      <b-row>
        <div id="nav">
          <b-navbar toggleable="lg" type="dark" fixed="top" variant="light">
            <b-navbar-brand href=""
              ><img id="logo" src="@/assets/logo_index.png"
            /></b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
              <b-navbar-nav> </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-item ><router-link to="/wait"><span id="refresh">refresh</span></router-link></b-nav-item>
                <b-nav-item
                  ><router-link to="/organization/home">MY CERTIFICATES</router-link></b-nav-item>
                <b-nav-item href="#"><router-link to="/certificates/add">ADD CERTIFICATE</router-link></b-nav-item>
                <b-nav-item> | </b-nav-item>
                <b-nav-item>
                  <span v-if="loggedIn" @click="logout"
                    >LOGOUT</span
                  >
                  <span v-if="!loggedIn" @click="login"
                    >LOGIN</span
                  ></b-nav-item
                >
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
        </div>
      </b-row>
      <b-row>
        <div id="spacer"></div>
      </b-row>
      <b-row>
        <b-container id="router_view_container"><router-view /></b-container>
      </b-row>
      <b-row>
        <b-col>
          <br />
          <br />
          <span></span>
          <br />
          <br />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  computed: {
loggedIn: function(){ return this.$store.state.IsloggedIn} 
  },
  mounted(){
    this.$root.$on('myEvent', () => { // here you need to use the arrow function
     this.loggedIn = true;})
    
  },

  methods: {
    logout() {
      localStorage.removeItem("OrganizationID");
      localStorage.removeItem("OrganizationName");
      this.$store.dispatch("changeLoginStatus");
      this.$router.push("/prompt");
    },
    login() {
      this.$router.push("/login");
    },
  },
    created () {
            document.title = "Impakter - Certificates";
        }
};
</script>

<style lang="scss">
@import "assets/custom_vars.scss";

@import "~bootstrap/scss/bootstrap.scss";
@import "~bootstrap-vue/src/index.scss";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #010101;
}

#nav {

  border-bottom: #a1a1a1 0.5px solid;
  box-shadow: 1px 1px 5px 1px #c0c0c0;
  background: aliceblue;
  z-index:100;
}

#nav a {
  font-weight: bold;
  font-size: 14px;
  color: #222222;
}

#nav a.router-link-exact-active {
  color: #fe6663;
}

button {
  margin-left: 10px;
}

#logo {
  width: 190px;
}

#refresh {
  color: rgb(79, 167, 162);
}

.main_row {
  margin-top: 0px;
}

.buttons_row {
  justify-content: center;
}

.buttons_row * {
  margin-right: 10px;
  margin-left: 10px;
}




#checkbox-group-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}

#input-group-1 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}

#input-group-2 {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
}

#spacer {
  background-color: white;
  position: fixed;
  z-index:90;
  padding: 50px;
  width: 100%;
}

#router_view_container{
margin-top: 100px;

}

.pagination {
  margin-top: 20px;
  margin-bottom: 40px;
}


</style>
