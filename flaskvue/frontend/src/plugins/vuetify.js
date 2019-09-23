import Vue from 'vue';

import Vuetify, {
    VApp,
    VContainer,
    VLayout,
    VBtn,
    VTextField,
    VFlex,
    VIcon,
    VDataTable,
    VSlider
} from "vuetify/lib";

import 'vuetify/dist/vuetify.min.css';



Vue.use(Vuetify, {
    components: {
        VApp,
        VContainer,
        VLayout,
        VBtn,
        VTextField,
        VFlex,
        VIcon,
        VDataTable,
        VSlider,
    },
    theme: {
    primary: '#3A84FF',
    secondary: '#424242',
    accent: '#82B1FF',
    error: '#FF5252',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FFC107',
  },
  iconfont: 'md',
});
//
// import 'vuetify/src/stylus/app.styl'
//
// Vue.use(Vuetify, {
//   iconfont: 'md',
// })
