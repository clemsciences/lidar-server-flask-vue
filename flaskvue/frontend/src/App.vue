<template>
  <div id="app">
    <v-app>
      <app-header/>

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
