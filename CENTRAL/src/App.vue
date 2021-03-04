
<template>
  <div id="demo" :class="[{ collapsed: collapsed }, { onmobile: isOnMobile }]">
    <div class="demo">
      <div class="container">
        <router-view />
      </div>
      <sidebar-menu
        :menu="menu"
        :collapsed="collapsed"
        :theme="selectedTheme"
        :show-one-child="true"
        @toggle-collapse="onToggleCollapse"
        @item-click="onItemClick"
        :width="width"
        :widthCollapsed="widthCollapsed"
        ><template v-slot:header
          ><img id="logo" src="@/assets/impakt_logo.png"
        /></template>
        <template v-slot:footer></template>
        <template v-slot:toggle-icon>min</template>
        <template v-slot:dropdown-icon="{ isOpen }">
          <span v-if="!isOpen">+</span>
          <span v-else>-</span>
        </template>
      </sidebar-menu>
      <div
        v-if="isOnMobile && !collapsed"
        class="sidebar-overlay"
        @click="collapsed = true"
      />
    </div>
  </div>
</template>

<script>
const separator = {
  template: `<hr style="border-color: rgba(0, 0, 0, 0.1); margin: 20px;">`,
};
import { SidebarMenu } from "vue-sidebar-menu";

export default {
  data() {
    return {
      menu: [
        {
          href: "/",
          title: "Dashboard",
          icon: "fa fa-user-secret",
        },
        {
          href: "/news",
          title: "News",
          icon: "fa fa-user-secret",
        },
        {
          component: separator,
        },
        {
          header: true,
          title: "Index",
          hiddenOnCollapse: true,
        },

        {
          href: "/index/certificates",
          title: "Certificates",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/index/certificates/all",
              title: "All Certificates",
            },
            {
              href: "/index/certificates/orgs",
              title: "Certificate Organizations",
            },
          ],
        },
        {
          href: "/index/companies",
          title: "Companies",
          icon: "fa fa-chart-area",
          child: [
            {
              href: "/index/companies/all",
              title: "All Companies",
            },
            {
              href: "/index/companies/orgs",
              title: "Lists",
            },
            {
              href: "/index/companies/research",
              title: "Research",
            },
          ],
        },
      ],
      width: "250px",
      widthCollapsed: "55px",
      collapsed: false,
      themes: [
        {
          name: "Dark",
          input: "",
        },
        {
          name: "Light",
          input: "white-theme",
        },
      ],
      selectedTheme: "",
      isOnMobile: false,
    };
  },
  computed: {
    loggedIn: function () {
      return this.$store.state.IsloggedIn;
    },
  },
  mounted() {
    this.$root.$on("myEvent", () => {
      // here you need to use the arrow function
      this.loggedIn = true;
    });
    this.onResize();
    window.addEventListener("resize", this.onResize);
  },

  methods: {
    logout() {
      localStorage.removeItem("OrganizationID");
      localStorage.removeItem("OrganizationName");
      this.$store.dispatch("resetState");
      this.$store.dispatch("changeLoginStatus");
      this.$router.push("/prompt");
    },
    login() {
      this.$router.push("/login");
    },

    onToggleCollapse(collapsed) {
      console.log(collapsed);
      this.collapsed = collapsed;
    },
    onItemClick(event, item, node) {
      console.log("onItemClick");
      console.log(event);
      console.log(item);
      console.log(node);
    },
    onResize() {
      if (window.innerWidth <= 767) {
        this.isOnMobile = true;
        this.collapsed = true;
      } else {
        this.isOnMobile = false;
        this.collapsed = false;
      }
    },
  },
  created() {
    document.title = "Impakter - Central";
  },
  components: { SidebarMenu },
};
</script>

<style lang="scss">
@import "assets/custom_vars.scss";

@import "~bootstrap/scss/bootstrap.scss";
@import "~bootstrap-vue/src/index.scss";
@import url("https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,600");

body,
html {
  margin: 0;
  padding: 0;
}
body {
  font-family: "Source Sans Pro", sans-serif;
  font-size: 18px;
  background-color: #f2f4f7;
  color: #262626;
}
#demo {
  padding-left: 250px;
  transition: 0.3s ease;
}
#demo.collapsed {
  padding-left: 50px;
}
#demo.onmobile {
  padding-left: 50px;
}
.sidebar-overlay {
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  background-color: #000;
  opacity: 0.5;
  z-index: 900;
}
.demo {
  padding: 50px;
}
.container {
  max-width: 900px;
}
pre {
  font-family: Consolas, monospace;
  color: #000;
  background: #fff;
  border-radius: 2px;
  padding: 15px;
  line-height: 1.5;
  overflow: auto;
}

.v-sidebar-menu {
  z-index: 101;
}

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
  z-index: 100;
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

.flex_and_start {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left !important;
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
  z-index: 90;
  padding: 50px;
  width: 100%;
}

#router_view_container {
  margin-top: 100px;
}

.pagination {
  margin-top: 20px;
  margin-bottom: 40px;
}
</style>
