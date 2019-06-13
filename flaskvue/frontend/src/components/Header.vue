<template>
    <v-toolbar dense>
        <v-toolbar-title class="headline text-uppercase">Hugin</v-toolbar-title>
        <v-toolbar-items>
            <v-label>Hugin</v-label>
        </v-toolbar-items>

        <v-spacer></v-spacer>

        <v-toolbar-items>
            <v-btn flat>Configuration</v-btn>
        </v-toolbar-items>
    </v-toolbar>
</template>

<script>
    export default {
        name: "Header",
        data: () => {return {};},
    }
</script>

<style scoped>

</style>
