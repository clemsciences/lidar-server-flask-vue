<template>
  <div id="app">
    <v-app>
      <v-content>
      <app-header></app-header>
      </v-content>

      <v-content>
        <router-view/>
      </v-content>

    </v-app>
  </div>

</template>

<script>

  import Vue from 'vue';
  import Vuetify from 'vuetify';
  import Header from '../src/components/Header.vue'
  Vue.use(Vuetify);

  export default {
    name: 'Hugin',
    el: '#app',
    components:{
      'app-header': Header,
    },


  };
</script>

<style>
  @import "styles/main.css";


</style>
