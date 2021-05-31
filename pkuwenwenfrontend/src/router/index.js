import { createWebHistory, createRouter } from "vue-router"

const routes = [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/Home.vue')
    },
    /*
    {
        path: '/Home',
        name: 'HomePage',
        component: () => import('../components/Home.vue')
    },
    */
    {
        path: '/SignUp',
        name: 'SignUp',
        component: () => import('../components/Pages/SignUp.vue')
    },
    
    {
        path: '/SignIn',
        name: 'SignIn',
        component: () => import('../components/Pages/SignIn.vue')
    },

    {
        path: '/About',
        name: 'About',
        component: () => import('../components/About.vue')
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router