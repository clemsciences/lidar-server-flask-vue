<template>
    <v-container class="config full-height" xs4 pa-3>
        <v-navigation-drawer permanent absolute app>
        <v-layout row>
            <v-flex  class="Config">
                <v-card class="barre_verticale">
                    <div class="header">
                        <h3>Config</h3>
                    </div>
                    <div class="input-group">
                        <h4>Connexion au LiDAR</h4>
                        <form @submit.prevent="applyConfig">
                            <v-text-field type="text" v-model="ipAddress" label="Adresse IP" id="adresse-ip"></v-text-field>
                            <v-text-field type="number" v-model="port" label="Port" id="port"></v-text-field>
                            <p>
                                <v-btn type="submit">Se connecter</v-btn>
                                <span>
                                    <v-chip label v-if="connected">LiDAR connecté</v-chip>
                                    <v-chip label v-else>LiDAR déconnecté</v-chip>
                                </span>
                            </p>
                        </form>
                    </div>
                    <p>Nombre de rafraichissement par seconde : {{ n_rafraichissement }}</p>

                    <div class="input-group">
                        <h4>Filtrage statistique</h4>
                        <form @submit.prevent="applyConfig">
                            <v-radio-group>
                                <v-radio v-model="kalmanFilter" label="Filtrage de Kalman" value="kalman"></v-radio>
                                <v-radio v-model="extendedKalmanFilter" label="Filtrage de Kalman étendu" value="kalman-extended"></v-radio>
                            </v-radio-group>
<!--                            <v-input type="radio" id="kalman" v-model="picked">-->

                            <v-text-field v-model="targetNumbers" type="number" min="0" max="2" label="Nombre de cibles"></v-text-field>

                        </form>
                    </div>
                </v-card>


            </v-flex>
        </v-layout>
        </v-navigation-drawer>
    </v-container>
</template>

<script>
    import axios from 'axios';

    import VueSocketIO from 'vue-socket.io'
    export default {
        name: "Config",
        data() {
            return {
                ipAddress: '',
                port: '',
                connected: false,
                n_rafraichissement: 1,
                kalmanFilter: false,
                extendedKalmanFilter: false,
                targetNumbers: 0,
                lidarSocket: null
            };
        },
        methods: {
            applyConfig: function(){
                console.log("config applied");
                console.log(this.connected);
                console.log(this.ipAddress);

                this.$emit("ipAddress", {
                    "ipAddress": this.ipAddress,
                    "port": this.port
                });
                this.lidarSocket = new VueSocketIO({
                    debug: true,
                    connection: this.ipAddress+":"+this.port, // CORS block origin Access to XMLHttpRequest at '' from origin 'http://localhost:8081' has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource.

                });

                return {
                };
            },
            checkIPAddress(ipAddress){

            },
            checkPort(port){

            },


        },
        computed: {
            }

    }
</script>

<style scoped>
.barre_verticale{
    padding-left: 30px;
    margin-left: 10px;
}
.config    {
  position: absolute;
  top: 48px;
  left: 0;
  /*z-index: 10000;*/
  /*height: calc(100% - 48px);*/
  height: 100%;
  /*box-shadow: 0 10px 10px rgba(0,0,0,0.4);*/
}

</style>
