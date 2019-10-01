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
    axios.defaults.baseURL = "http://localhost:5000";

    export default {
        name: "Lidar",
        components: {
            Plotly,
            Replay
        },
        data: function() {
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
                    height: 600,
                    autosize: true,
                    xaxis: {
                        range: [0.75, 5.25]
                    },
                    yaxis: {range: [-8, 8]},
                    title: 'Simulation mesures LiDAR'
                }
            }
        },
        created: function() {

        },
        mounted: function(){

        },
        updated: function(){

        },
        methods: {

            setMeasuresPlotly: function() {
                let r = [];
                let theta = [];
                this.measures.forEach(function (element) {
                    theta.push(element[0]);
                    r.push(element[1]);
                });
                this.layout.title = 'Mesures LiDAR';
                this.data = [
                    {
                        r: r,
                        theta: theta,
                        mode: 'markers',
                        marker: {
                            color: "rgb(0,0,0)",
                            size: 5,
                        },
                        name: 'lidar_simulation',
                        line: {color: 'red'},
                        type: 'scatterpolar',
                    }
                ];
                console.log(this.data);

            },
            get_measures_test: function(){
                //console.log(this.measures);
                //axios.get('/test_measures').then(
                axios.get('/get_measures').then(
                (response) => {
                    //console.log(response);
                    //console.log(this);
                    this.measures = response.data.measures;
                    this.setMeasuresPlotly();
                });
                //console.log(this.measures);
            },
            get_measures() {

            },

        },
    };


</script>

<style scoped>
#lidar-view {

}
</style>
