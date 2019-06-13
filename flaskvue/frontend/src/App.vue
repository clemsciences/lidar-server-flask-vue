<template>
  <v-app>
    <app-header></app-header>
    <p>Oui ?</p>
    <p>Bizarre</p>

    <v-content>
      <router-view/>
    </v-content>

  </v-app>

</template>

<script>

  import Vue from 'vue';
  import Vuetify from 'vuetify';
  import Header from '../src/components/Header.vue'
  Vue.use(Vuetify);

  export default {
    name: 'Hugin',
    components:{
      'app-header': Header,
    },


  };
</script>

<style>
  @import "styles/main.css";
</style>
