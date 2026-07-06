<script lang="ts">
import { defineComponent } from 'vue'
import store from '../store'

export default defineComponent({
    data(){
        return {
            minRent: 0,
            maxRent: 9999
        }
    },
    methods: {
        updateStore() {
            const filter = store.state.filter
            filter.minRent = this.minRent
            filter.maxRent = this.maxRent
            store.dispatch('updateFilter', filter)
        }
    }
})
</script>

<template>
    <section class="px-6 pb-16">
        <div class="wizard-card">
            <img src="../assets/images/Untitled_Artwork_1.gif" class="wizard-illustration">

            <h2 class="wizard-question">What is your desired monthly rent?</h2>

            <div class="flex items-end justify-center gap-4 mt-6">
                <div>
                    <label class="field-label text-center">Min rent</label>
                    <input class="field-input w-32" type="number" v-model="minRent" min="1" max="9999">
                </div>
                <span class="text-xl text-darkGrayishBlue pb-2.5">–</span>
                <div>
                    <label class="field-label text-center">Max rent</label>
                    <input class="field-input w-32" type="number" v-model="maxRent" min="1" max="9999">
                </div>
            </div>

            <div class="flex justify-center gap-3 mt-8">
                <router-link to="/rent" class="btn-ghost">Back</router-link>
                <router-link to="/filter/1" @click.native="updateStore" class="btn-solid">Next</router-link>
            </div>

            <div class="flex justify-center gap-6 mt-5 text-sm">
                <router-link to="/filter/1" class="wizard-skip">Skip this filter</router-link>
                <router-link to="/search" class="wizard-skip">Skip all filters</router-link>
            </div>
        </div>
    </section>
</template>

<style>
.wizard-card {
    @apply bg-white rounded-2xl border border-gray-200 shadow-sm max-w-xl mx-auto p-10 text-center;
}
.wizard-illustration {
    @apply mx-auto;
    max-width: 35%;
}
.wizard-question {
    @apply text-xl font-semibold text-veryDarkBlue mt-2;
}
.wizard-skip {
    @apply text-darkGrayishBlue hover:text-brightRed no-underline;
}
</style>
