<script lang="ts">
import { defineComponent } from 'vue'
import store from '../store'

export default defineComponent({
    data(){
        return {
            minBedrooms: 1,
            maxBedrooms: 5,
            minBathrooms: 1,
            maxBathrooms: 5,
        }
    },
    methods: {
        updateStore() {
            const filter = store.state.filter
            filter.minBedrooms = this.minBedrooms
            filter.maxBedrooms = this.maxBedrooms
            filter.minBathrooms = this.minBathrooms
            filter.maxBathrooms = this.maxBathrooms
            store.dispatch('updateFilter', filter)
        }
    }
})
</script>

<template>
    <section class="px-6 pb-16">
        <div class="wizard-card">
            <img src="../assets/images/Untitled_Artwork.gif" class="wizard-illustration">

            <h2 class="wizard-question">Do you have a preference on bed &amp; bath configuration?</h2>

            <div class="flex flex-wrap items-end justify-center gap-8 mt-6">
                <div class="flex items-end gap-3">
                    <span class="field-label mb-2.5">Bed</span>
                    <input class="field-input w-20" type="number" v-model="minBedrooms" min="1" max="5">
                    <span class="text-xl text-darkGrayishBlue pb-2.5">–</span>
                    <input class="field-input w-20" type="number" v-model="maxBedrooms" min="1" max="5">
                </div>
                <div class="flex items-end gap-3">
                    <span class="field-label mb-2.5">Bath</span>
                    <input class="field-input w-20" type="number" v-model="minBathrooms" min="1" max="5">
                    <span class="text-xl text-darkGrayishBlue pb-2.5">–</span>
                    <input class="field-input w-20" type="number" v-model="maxBathrooms" min="1" max="5">
                </div>
            </div>

            <div class="flex justify-center gap-3 mt-8">
                <router-link to="/filter/1" class="btn-ghost">Back</router-link>
                <router-link to="/search" @click.native="updateStore" class="btn-solid">Finish</router-link>
            </div>

            <div class="flex justify-center gap-6 mt-5 text-sm">
                <router-link to="/search" class="wizard-skip">Skip this filter</router-link>
                <router-link to="/search" class="wizard-skip">Skip all filters</router-link>
            </div>
        </div>
    </section>
</template>
