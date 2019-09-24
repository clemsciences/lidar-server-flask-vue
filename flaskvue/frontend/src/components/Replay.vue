<template>

    <v-card class="mx-auto" max-width="600">

        <v-card-text>
            <v-row class="mb-4" justify="space-between">
                <v-col>
                    <v-slider
                      v-model="time"
                      label="Durée"
                    ></v-slider>

                </v-col>


            </v-row>
        </v-card-text>




    </v-card>

</template>

<script>
    export default {
        name: "Replay",
        data() {
            return {
                time: 10,
            }
        },
        computed: {
            displayMeasureAtTimeT() {
                console.log("le temps");
            }
        }
    }
</script>

<style scoped>

</style>
