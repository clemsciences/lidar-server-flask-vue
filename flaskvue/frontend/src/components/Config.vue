<template>
    <v-container class="config">
        <v-layout row>
            <v-flex xs4 pa-3 class="Config">
                <v-card>
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
                            <v-checkbox v-model="extendedKalmanFilter" label="Filtrage de Kalman étendu"></v-checkbox>
                            <v-text-field v-model="targetNumbers" type="number" min="0" max="2" label="Nombre de cibles"></v-text-field>

                        </form>
                    </div>
                </v-card>


            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
    import axios from 'axios';

    import VueSocketIO from 'vue-socket.io'
    export default {
        name: "Config",
        data: function() {
            return {
                ipAddress: '',
                port: '',
                connected: false,
                n_rafraichissement: 1,
                extendedKalmanFilter: false,
                targetNumbers: 0
            };
        },
        methods: {
            applyConfig: function(){
                console.log("config applied");
                return {


                };
            }
        },
        computed: {
            }

    }
</script>

<style scoped>

.config    {
  position: absolute;
  top: 48px;
  left: 0;
  /*z-index: 10000;*/
  height: calc(100% - 48px);
  /*box-shadow: 0 10px 10px rgba(0,0,0,0.4);*/
}

</style>
