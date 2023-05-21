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
            console.log("updateStore called!")
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
    <section id="f3-progress-bar">
       <div id="my-rounded-rectangle" class="f1-my-rounded-rectangle"> 
            <div class="f3-my-rounded-rectangle-yellow" style="height:20px;"></div>
            <img class="f3-flatbird" src="../assets/images/fatbird.png" style="height: 20px;">
        </div>
    </section>

    <section class="bed-filter">
        <div class="w3-light-grey w3-round-large " style="margin: auto; align-items: center; width: 90%; margin-top: 2%; margin-bottom: 2%;">
            <br>
            <br>
            <div class="flex justify-center">
                <img src="../assets/images/Untitled_Artwork.gif" style="max-width: 30%;">
            </div>
            <div class="flex justify-center text-brightRed" style="text-align:center;font-size:20px;font-weight:bold;font-family:avenir;color: #000;">Do you have a preference on bed & bath configuration?</div>
            <div class="flex justify-center align-center mt-4 text-brightRed" style="font-family:avenir;font-weight:bold;width: 100%">
                <div class="py-1.5 pr-6 pl-6">
                    <router-link to="/rent" class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">BACK</router-link>
                </div>
                <div class="mr-3 flex">
                    <div class="text-l my-2" style="color:#000;"> Bed: </div>
                    <div class="px-2">
                        <div class="mt-1">
                            <input
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                type="number"
                                id="min-rent"
                                v-model="minBedrooms"
                                min="1"
                                max="5"
                                style="color:#000"
                            />
                        </div>
                    </div>
                    <div class="text-l my-2" style="font-weight:bold;color:#000"> - </div>
                    <div class="px-2">
                        <div class="mt-1">
                            <input
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                type="number"
                                id="max-rent"
                                v-model="maxBedrooms"
                                min="1"
                                max="5"
                                style="color:#000"
                            />
                        </div>
                    </div>
                </div>
                <div class="ml-3 flex">
                    <div class="text-l my-2" style="color:#000;"> Bath: </div>
                    <div class="px-2">
                        <div class="mt-1">
                            <input
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                type="number"
                                id="min-rent"
                                v-model="minBathrooms"
                                min="1"
                                max="5"
                                style="color:#000"
                            />
                        </div>
                    </div>
                    <div class="text-l my-2" style="font-weight:bold;color:#000"> - </div>
                    <div class="px-2">
                        <div class="mt-1">
                            <input
                                class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                                type="number"
                                id="max-rent"
                                v-model="maxBathrooms"
                                min="1"
                                max="5"
                                style="color:#000"
                            />
                        </div>
                    </div>
                </div>
                <div class="py-1.5 pr-6 pl-6">
                    <router-link 
                        to="/search" 
                        @click.native="updateStore"
                        class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">Finish</router-link>
                </div>
            </div>
            <div class="flex justify-center py-5">
                <router-link to="/search" class="no-underline btn btn-secondary text-shooniYellow rounded-md px-3 py-1 mr-10" style="font-family: avenir; font-size: 14px; font-weight: bold;">
                    <u>Skip this filter</u>
                </router-link>
                <router-link to="/search" class="no-underline btn btn-secondary text-shooniYellow rounded-md px-3 py-1 ml-10" style="font-family: avenir; font-size: 14px; font-weight: bold;">
                    <u>Skip ALL filters</u>
                </router-link>
            </div>
        </div>
</section>
</template>


<style>
.f3-my-rounded-rectangle-yellow {
    display: flex;
    background-color: #f3d99edf;
    border-radius: 10px;
    width: 790px; /*  width */
    height: 20px; /*  height */
}
.f3-flatbird {
    /* display: flex; */
    margin-left: -18px;
}
</style>