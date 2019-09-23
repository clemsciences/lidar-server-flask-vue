<template>

    <v-slider
      v-model="volume"
      @end=""
      append-icon="volume_up"
      prepend-icon="volume_down"
      label="Durée"
    ></v-slider>

</template>

<script>
    export default {
        name: "Replay"
    }
</script>

<style scoped>

</style>
