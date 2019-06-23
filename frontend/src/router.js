import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';
import Login from './views/Login.vue';
import UserDetails from './views/UserDetails.vue';

Vue.use(Router);

const router = new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Login,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
    // {
    //   path: '/login',
    //   name: 'login',
    //   component: Login,
    // },
    {
      path: '/details',
      name: 'details',
      component: UserDetails,
    }
  ],
});

router.beforeEach((to, from, next) => {
  if (!localStorage.currentUserId && to.name != 'home' && to.name != 'login') {
    next('/login');
  }
  next();
});

export default router;
