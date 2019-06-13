import Vue from 'vue';
import Router from 'vue-router';
import 'vuetify/dist/vuetify.min.css'
import About from '../components/About.vue';
import Home from '../components/Home.vue';
import NotFound from '../components/NotFound.vue';
const routerOptions = [

];

const routes = routerOptions.map((route) => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`),
  };
});

Vue.use(Router);

export default new Router({
  routes: [
  { path: '/', component: Home , name: 'home'},
  { path: '/about', component: About, name: 'about' },
  { path: '*', component: NotFound, name: 'notfound' },
  ],
});
/* eslint-disable */
