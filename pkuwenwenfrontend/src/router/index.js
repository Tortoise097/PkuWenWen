import { createWebHistory, createRouter } from "vue-router";
import Home from '../components/Home.vue'
import SignUp from '../components/Pages/SignUp.vue'
import SignIn from '../components/Pages/SignIn.vue'
import About from '../components/About.vue'

const routes = [
    {
      path: '/',
      name: 'defaultPage',
      component: Home,
    },
    {
        path: '/Home',
        name: 'HomePage',
        component: Home,
    },
    {
        path: '/SignUp',
        name: 'SignUp',
        component: SignUp,
    },
    
    {
        path: '/SignIn',
        name: 'SignIn',
        component: SignIn,
    },

    {
        path: '/About',
        name: 'About',
        component: About,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});
  
export default router;