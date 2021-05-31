<template>
<div>
    <div id="navbar">
        <router-link to="/">Home</router-link> |
        <router-link to="/About">About</router-link> |
        <router-link to="/SignIn">Sign In</router-link> |
        <router-link to="/SignUp">Sign Up</router-link>
    </div>
    <div>
        <img alt="Vue logo" src="../assets/logo.png">
    </div>
    <div>
        <h1>
            this is the About Page of Vue
        </h1>
        <el-button type="primary" @click="ClickThis()">测试此按钮</el-button>
        
    </div>
</div>
</template>

<script>
export default{
    data() {
        return ;
    },
    methods: {
        ClickThis(){
            alert("you click this!");
        },
    },
};

</script>

<style>

</style>
