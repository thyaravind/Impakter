<template>
  <div id="app">
    <b-container>
      <b-row>
        <div id="nav">
          <b-navbar toggleable="lg" type="dark" fixed="top" variant="light">
            <b-navbar-brand href="#">Impakter Index - Cerificates</b-navbar-brand
            >

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
              <b-navbar-nav>
                <b-nav-item><router-link to="/organization/home">Home</router-link></b-nav-item
                >
                <b-nav-item href="#"
                  ><router-link to="/certificates/add"
                    >Add Certificate</router-link
                  ></b-nav-item
                >
              </b-navbar-nav>

              <!-- Right aligned nav items -->
              <b-navbar-nav class="ml-auto">
                <b-nav-item><router-link to="/">LogOut</router-link></b-nav-item>
              </b-navbar-nav>
            </b-collapse>
          </b-navbar>
        </div></b-row
      >
      <b-row>
        <b-container><router-view /></b-container>
      </b-row>
    </b-container>
  </div>
</template>

<script>

export default {
  mounted:{
    //todo Login - Logout based on certirficates fetched or not

  }
}
</script>

<style lang="scss">

  @import 'assets/custom_vars.scss';

  @import '~bootstrap/scss/bootstrap.scss';
  @import '~bootstrap-vue/src/index.scss';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #010101;
}

#nav {
  margin-bottom: 90px;
  border-bottom: #a1a1a1 0.5px solid;
  box-shadow: 1px 1px 5px 1px #c0c0c0;
  background: aliceblue;
}

#nav a {
  font-weight: bold;
  color: #010101;
}

#nav a.router-link-exact-active {
  color: #fe6663;
}
</style>
