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
            console.log("updateStore called!")
            const filter = store.state.filter
            filter.minRent = this.minRent
            filter.maxRent = this.maxRent
            store.dispatch('updateFilter', filter)
        }
    }
})
</script>

<template>
    <section id="f1-progress-bar">
       <div id="my-rounded-rectangle" class="f1-my-rounded-rectangle"> 
            <div class="f1-my-rounded-rectangle-yellow" style="height:20px;"></div>
            <img class="f1-flatbird" src="../assets/images/fatbird.png" style="height: 20px;">
        </div>
    </section>

    <section class="price-filter" style="margin-bottom: 2%;">
        <div class="w3-light-grey w3-round-large" style="margin:auto; width: 1100px; height: 520px; margin-top: 2%;">

            <div class="flex justify-center">
                <img src="../assets/images/Untitled_Artwork_1.gif" style="max-width: 30%;">
            </div>
            
            <div class="flex justify-center text-brightRed" style="text-align:center;font-size:20px;font-weight:bold;font-family:avenir;color:black">What is your desired monthly rent?</div>
            <div class="flex justify-center mt-4 text-brightRed" style="font-family:avenir;font-size:18px;font-weight:bold;">
                <div class="py-1.5 pr-6 pl-6">
                    <router-link to="/rent" class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">BACK</router-link>
                </div>
                <div class="pl-6 pr-6">
                    <div class="mt-1">
                        <input
                            class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                            type="number"
                            id="min-rent"
                            v-model="minRent"
                            min="1"
                            max="9999"
                            style="color:#000"
                        />
                    </div>
                </div>
                <div style="font-size:24px;font-family:avenir;font-weight:bold;color:black"> - </div>
                <div class="pl-6 pr-6">
                    <div class="mt-1">
                        <input
                            class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                            type="number"
                            id="max-rent"
                            v-model="maxRent"
                            min="1"
                            max="9999"
                            style="color:#000"
                        />
                    </div>
                </div>
                <div class="py-1.5 pr-6 pl-6">
                    <router-link 
                        to="/filter/1" 
                        @click.native="updateStore"
                        class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">NEXT</router-link>
                </div>
            </div>
            <div class="flex justify-center py-5">
                <a class="btn btn-secondary text-shooniYellow rounded-md px-3 py-1 mr-10" 
                    style="font-family: avenir; font-size: 14px; font-weight: bold; background-color: None;">
                    <u><router-link to="/filter/1" class="no-underline">Skip this filter</router-link></u>
                </a>
                <router-link to="/search" class="no-underline btn btn-secondary text-shooniYellow rounded-md px-3 py-1 ml-10" 
                    style="font-family: avenir; font-size: 14px; font-weight: bold;">
                    <u>Skip ALL filters</u>
                </router-link>
            </div>
        </div>
    </section>
</template>


<style>
.f1-my-rounded-rectangle-yellow {
    display: flex;
    background-color: #f3d99edf;
    border-radius: 10px;
    width: 305px; /*  width */
    height: 20px; /*  height */
}
.f1-flatbird {
    /* display: flex; */
    margin-left: -18px;
}
</style>