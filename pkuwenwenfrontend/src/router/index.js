import { createWebHistory, createRouter } from "vue-router"

const routes = [
    {
      path: '/',
      name: 'Home',
      component: () => import('../components/Home.vue')
    },
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
    },
    {
        path: '/SchoolIndex',
        name: 'SchoolIndex',
        component: () => import('../components/Pages/SchoolIndex.vue')
    },
    {
        path: '/:school/CourseIndex', //使用动态链接，school是院系名
        name: 'CourseIndex',
        component: () => import('../components/Pages/CourseIndex.vue')
    },
    {
        path: '/:school/:course/QuestionIndex',
        //path: '/Questions',
        name: 'QuestionIndex',
        component: () => import('../components/Pages/QuestionIndex.vue')
    },
    {
        path: '/Question/:id',
        name: 'Question',
        component: () => import('../components/Pages/Question.vue')
    },
    {
        path: '/Dashboard',
        name: 'Dashboard',
        component: () => import('../components/dashboard')
    },
    {
        path: '/ViewAnswer',
        name: 'ViewAnswer',
        component: () => import ('../components/Pages/ViewAnswer')
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

/*
router.beforeEach((to, from, next) => {
    document.title = `| PkuWenWen |`;
    const role = localStorage.getItem('ms_username');
    if (!role && to.path !== '/SignIn') {
        next('/SignIn');
    } else {
        next();
    }
})
*/

export default router
