<template>

    <v-container id="lidar-view">
        <v-btn @click="get_measures_test"></v-btn>
        <Plotly :data="data" :layout="layout"/>
        <Replay/>

    </v-container>

</template>

<script>
    import { Plotly } from 'vue-plotly';
    import Replay from './Replay';
    import axios from 'axios';
    axios.defaults.baseURL = "http://127.0.0.1:5000";

    export default {

        name: "Lidar",

        components: {
            Plotly,
            Replay
        },

        methods: {
            get_measures_test() {
                axios.get('/test_measures').then(response =>
                    (this.data.measures = response.measure));

            },
            get_measures() {

            },

        },
        created: function() {

        },
        mounted: function(){

        },
        updated: function(){

        },

        data() {
            return {
                measures: [],
                data: [{
                    r: [1000, 1200, 1700, 750, 2400, 2000],
                    theta: [0, 0.2*180/3.14, 180/3.14, 2*180/3.14, 3*180/3.14, 5*180/3.14],
                    mode: 'lines',
                    name: 'lidar_simulation',
                    line: {color: 'red'},
                    type: 'scatterpolar',

                    // x: [1, 2, 3, 4, 5],
                    // y: [1, 6, 3, 6, 1],
                    // mode: 'markers',
                    // type: 'scatter',
                    // name: 'bléré',
                    // text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
                    // marker: {size: 12}
                },],
                layout: {
                    //width: 500,
                    height: 400,
                    autosize: true,
                    xaxis: {
                        range: [0.75, 5.25]
                    },
                    yaxis: {range: [-8, 8]},
                    title: 'Simulation mesures LiDAR'
                }
            }
        }
    };


</script>

<style scoped>
#lidar-view {

}
</style>
