<template>
 <div>
    <div id="app">
        <router-link to="/">Home</router-link> |
        <router-link to="/About">About</router-link> |
        <router-link to="/SignIn">Sign In</router-link> |
        <router-link to="/SignUp">Sign Up</router-link>
    </div>
    <div>
        <img alt="Vue logo" src="./assets/logo.png">
    </div>
    <div>
        <router-view></router-view>
    </div>
  </div>
</template>

<style>

#app {
  padding: 30px;
  text-align: center;
}
</style>
