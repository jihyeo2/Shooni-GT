<script lang="ts">
import { defineComponent, onMounted, type Ref, ref } from 'vue'
import type { Article } from '../types'
import { GoogleMap, Marker } from 'vue3-google-map'

export default defineComponent({
    name: 'SearchMap',
    props: {
        articles: {
            type: Array<Article>
        },
    },
    components: {
        GoogleMap,
        Marker,
    },
    setup() {
        const center = { lat: 33.775618, lng: -84.396285 }
        const rand_str = import.meta.env.VITE_DATA_ENDPOINT_KEY
        return {
            center,
            rand_str
        }

    },

    
})
</script>

<template>
    <GoogleMap
      :api-key="rand_str"
      class="w-19/20 px-3"
      style="height: 400px;"
      :center="center"
      :zoom="15"
      >

        <Marker 
        v-for="(item, index) in articles" v-bind:key="index"
        :options="{ position: { lat: item['latitude'], lng: item['longitude']} }" />

        
    </GoogleMap>
</template>