<template>

    <v-container id="lidar-view">
        <Plotly :data="data" :layout="layout"/>

    </v-container>

</template>

<script>
    import { Plotly } from 'vue-plotly';

    export default {

        name: "Lidar",

        components: {
            Plotly
        },

        data() {
            return {
                data: [{
                    x: [1, 2, 3, 4, 5],
                    y: [1, 6, 3, 6, 1],
                    mode: 'markers',
                    type: 'scatter',
                    name: 'bléré',
                    text: ['A-1', 'A-2', 'A-3', 'A-4', 'A-5'],
                    marker: {size: 12}
                },],
                layout: {
                    xaxis: {
                        range: [0.75, 5.25]
                    },
                    yaxis: {range: [-8, 8]},
                    title: 'Le titre'
                }
            }
        }
    };


</script>

<style scoped>

</style>
