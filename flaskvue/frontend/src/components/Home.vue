/* eslint-disable */
<template>

  <v-container fluid>
<!--&lt;!&ndash;    <Config></Config>&ndash;&gt;-->
<!--    <v-label>Bonjour</v-label>-->
<!--    <p>Home page</p>-->
<!--    <p>Random number from backend: {{ randomNumber }}</p>-->
<!--    <button @click="getRandom">New random number</button>-->

    <Lidar></Lidar>
    <v-footer class="pa-3 footer">
        <v-spacer></v-spacer>
        <div><a href="https://github.com/clemsciences/lidar-server-flask-vue.git">Venez contribuer ici</a></div>
      </v-footer>
  </v-container>
</template>

<script>
  import axios from 'axios'
  import Config from "./Config";
  import Lidar from "./Lidar";


export default {
  components: {Lidar, Config},
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min);
      max = Math.floor(max);
      return Math.floor(Math.random() * (max - min + 1)) + min
    },

  getRandomFromBackend () {
    const path = `http://localhost:5000/api/random`;
    axios.get(path)
    .then(response => {
      this.randomNumber = response.data.randomNumber
    })
    .catch(error => {
      console.log(error)
    })
  },

    getRandom () {
      this.randomNumber = this.getRandomInt(1, 100)
    }
  },
  created () {
    this.getRandom()
  }
};
</script>

<style scoped>
    .footer {
        position: absolute;
        bottom: 0;
        width: 100%;
        background-color: antiquewhitete;
}

</style>
