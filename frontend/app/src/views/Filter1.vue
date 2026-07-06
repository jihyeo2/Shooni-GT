<script lang="ts">
import { defineComponent } from 'vue'
import store from '../store'

export default defineComponent({
    data(){
        return {
            proximity: 'No Preference'
        }
    },
    methods: {
        updateStore(e: Event) {
            const filter = store.state.filter
            filter.proximity = (e.target as HTMLSelectElement).value
            store.dispatch('updateFilter', filter)
        }
    }
})
</script>

<template>
    <section class="px-6 pb-16">
        <div class="wizard-card">
            <img src="../assets/images/Untitled_Artwork_2.gif" class="wizard-illustration">

            <h2 class="wizard-question">Do you prefer on-campus or off-campus?</h2>

            <div class="flex justify-center mt-6">
                <select v-model="proximity" @change="updateStore" class="field-input w-64 text-center">
                    <option>On Campus</option>
                    <option>Off Campus</option>
                    <option>No Preference</option>
                </select>
            </div>

            <div class="flex justify-center gap-3 mt-8">
                <router-link to="/filter" class="btn-ghost">Back</router-link>
                <router-link to="/filter/2" class="btn-solid">Next</router-link>
            </div>

            <div class="flex justify-center gap-6 mt-5 text-sm">
                <router-link to="/filter/2" class="wizard-skip">Skip this filter</router-link>
                <router-link to="/search" class="wizard-skip">Skip all filters</router-link>
            </div>
        </div>
    </section>
</template>
