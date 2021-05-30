<template>
  <div id = "Home">
    <router-link to="/">Home</router-link>
    <router-link to="/About">About</router-link>
    <router-link to="/SignIn">Sign In</router-link>
    <router-link to="/SignUp">Sign Up</router-link>
    
    <img alt="Vue logo" src="../assets/logo.png">
    <!--路由器匹配到的组件被渲染到router-view这里，这正是我们想要的效果-->
    <router-view></router-view>

  </div>
</template>

<script>
export default {

}
</script>

<style>
#Home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 93px;
}
</style>
