<template>
    <v-flex>
        <v-toolbar dense color="primary">
            <v-toolbar-side-icon @click="openConfig"></v-toolbar-side-icon>
            <v-toolbar-title class="headline text-uppercase">Hugin</v-toolbar-title>
            <v-spacer/>
            <v-toolbar-items>
                <v-btn flat>Configuration</v-btn>
            </v-toolbar-items>
        </v-toolbar>
        <config v-if="isConfigButtonClicked"/>
    </v-flex>
</template>

<script>
    import Config from './Config.vue';

    export default {
        name: "Header",
        components:{
            "config": Config
        },
        data: () => {
            return {
                isConfigButtonClicked: false,
            };
            },
        methods:
            {
                openConfig: function(){
                    this.isConfigButtonClicked = !this.isConfigButtonClicked;
                }
            },

    }
</script>

<style scoped>

</style>
