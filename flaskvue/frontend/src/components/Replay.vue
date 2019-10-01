<template>

    <v-card class="mx-auto" max-width="800" max-height="70">

        <v-card-text>
<!--            <v-row class="mb-4" justify="space-between">-->
<!--                <v-col>-->
                    <v-slider
                      height="30"
                      id="measurePicker"
                      v-model="time"
                      label="Durée"
                    ></v-slider>

<!--                </v-col>-->
<!--            </v-row>-->
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
#measurePicker {
    height: 100
}

</style>
