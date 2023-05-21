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
        updateStore(e) {
            console.log("updateStore called!")
            const filter = store.state.filter
            filter.proximity = e.target.value
            store.dispatch('updateFilter', filter)
        }
    }
})
</script>

<template>
    <section id="f2-progress-bar">
       <div id="my-rounded-rectangle" class="f1-my-rounded-rectangle"> 
            <div class="f2-my-rounded-rectangle-yellow" style="height:20px;"></div>
            <img class="f2-flatbird" src="../assets/images/fatbird.png" style="height: 20px;">
        </div>
    </section>

    <section class="place-filter">
        <div class="w3-light-grey w3-round-large" style="margin: auto; width: 1100px; margin-top: 2%; height: 520px;">
            <br>
            <br>
            <div class="flex justify-center">
                <img src="../assets/images/Untitled_Artwork_2.gif" style="max-width: 20%;">
            </div>
            <br>
            <div class="flex justify-center text-brightRed" style="text-align:center;font-size:20px;font-weight:bold;font-family:avenir;color:black">Do you prefer on-campus or off-campus?</div>
            <div class="flex justify-center mt-4 text-brightRed" style="font-family:avenir;font-size:18px;font-weight:bold;">
                <div class="py-1.5 pr-6 pl-6">
                    <router-link to="/rent" class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">BACK</router-link>
                </div>
                <div class="pl-6 pr-6">
                    <div class="relative">
                        <input type="text" list="min" placeholder="Proximity" style="font-family:avenir;font-size:18px;color:black" 
                            @input="updateStore"
                            class="w-full border-2 border-gray-300 rounded-md px-4 py-2 pr-8 sm:text-sm placeholder-lightGrey focus:outline-none 
                            focus:ring-2 focus:ring-blue-400 focus:border-transparent">
                        <div class="select-arrow"></div>
                    </div>
                    <datalist id="min">
                        <option>On Campus</option>
                        <option>Off Campus</option>
                        <option>No Preference</option>
                    </datalist>
                </div>
                <div class="py-1.5 pr-6 pl-6">
                    <router-link 
                        to="/filter/2" 
                        class="btn btn-primary bg-brightRed text-white border-2 border-brightRed rounded-md px-3 py-1" 
                        style="font-family:avenir;font-size:18px;font-weight:bold">NEXT</router-link>
                </div>
            </div>
                <div class="flex justify-center py-5">
                    <router-link to="/filter/2" class="no-underline btn btn-secondary text-shooniYellow rounded-md px-3 py-1 mr-2" style="font-family: avenir; font-size: 14px; font-weight: bold;">
                        <u>Skip this filter</u>
                    </router-link>
                    <router-link to="/search" class="no-underline btn btn-secondary text-shooniYellow rounded-md px-3 py-1 ml-2" style="font-family: avenir; font-size: 14px; font-weight: bold;">
                        <u>Skip ALL filters</u>
                    </router-link>
                </div>

        </div>
    </section>

</template>


<style>
.f2-my-rounded-rectangle-yellow {
    display: flex;
    background-color: #f3d99edf;
    border-radius: 10px;
    width: 538px; /*  width */
    height: 20px; /*  height */
}
.f2-flatbird {
    /* display: flex; */
    margin-left: -18px;
}
</style>