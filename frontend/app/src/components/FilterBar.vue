<!-- Reference:  https://github.com/uiuc-apartments/uiuc-apartments.com -->
<script lang="ts">
import { defineComponent,onMounted, watch, ref } from 'vue'
import type { Filter } from '../types'
import store from '../store'


export default defineComponent({
    name: 'FilterBar',
    props: ['apartments'],
    watch: {
        apartments(val) {
            this.selectedApartments = val
        }
    },
    setup(props: any, context: any) {
    const minBedrooms = ref(store.state.filter.minBedrooms)
    const maxBedrooms = ref(store.state.filter.maxBedrooms)
    const minBathrooms = ref(store.state.filter.minBathrooms)
    const maxBathrooms = ref(store.state.filter.maxBathrooms)
    const minRent = ref(store.state.filter.minRent)
    const maxRent = ref(store.state.filter.maxRent)
    const proximity = ref(store.state.filter.proximity)
    const selectedApartments = ref(store.state.filter.selectedApartments)




    // const dateRange = ref([new Date(2023, 7, 1), new Date(2023, 8, 31)])
    const filterApartments = () => {
      const filter: Filter = {
        minBedrooms: minBedrooms.value,
        maxBedrooms: maxBedrooms.value,
        minBathrooms: minBathrooms.value,
        maxBathrooms: maxBathrooms.value,
        minRent: minRent.value,
        maxRent: maxRent.value,
        // dateRange: dateRange.value,
        proximity: proximity.value,
        selectedApartments: selectedApartments.value,
      }
      context.emit('update:filter-apartments', filter)
    }
    watch(
      [
        minBedrooms,
        maxBedrooms,
        minBathrooms,
        maxBathrooms,
        minRent,
        maxRent,
        proximity,
        selectedApartments,
        // dateRange,
      ],
      filterApartments
    )
    return {
      minBedrooms,
      maxBedrooms,
      minBathrooms,
      maxBathrooms,
    //   dateRange,
      minRent,
      maxRent,
      proximity,
      selectedApartments,
    }
  },
})
</script>

<template>
    <section class="filter-map">
        <div class="flex justify-center items-center mt-4 text-brightRed mb-1" style="font-family:avenir;font-size:14px;font-weight:bold;">
            <div class="flex flex-row space-x-6 justify-evenly">

            <!-- min to max rent -->
                <div class="flex flex-col" style="margin-left: 10px;">
                    <label for="min-rent" class="block text-sm font-medium text-gray-700" style="text-align: center;">
                    Min rent
                    </label>
                    <div class="mt-1">
                        <input
                            class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                            type="number"
                            id="min-rent"
                            v-model="minRent"
                            min="1"
                            max="10000"
                        />
                    </div>
                </div>

                <div class="flex flex-col" style="margin-left: 70px;">
                    <label for="max-rent" class="block text-sm font-medium text-gray-700" style="text-align: center;">
                    Max rent
                    </label>
                    <div class="mt-1">
                    <input
                        class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        id="max-rent"
                        v-model="maxRent"
                        min="1"
                        max="10000"
                    />
                    </div>
                </div>

            <!-- min to max bathrooms -->
                <div class="flex flex-col" style="margin-left: 70px;">
                    <label
                    for="min-bathrooms"
                    class="block text-sm font-medium text-gray-700"
                    style="text-align: center;">
                    Min baths
                    </label>
                    <div class="mt-1">
                    <input
                        class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        id="min-bathrooms"
                        v-model="minBathrooms"
                        min="1"
                        max="10"
                    />
                    </div>
                </div>

                <div class="flex flex-col" style="margin-left: 70px;">
                    <label
                    for="max-bathrooms"
                    class="block text-sm font-medium text-gray-700"
                    style="text-align: center;">
                    Max baths
                    </label>
                    <div class="mt-1">
                    <input
                        class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        id="max-bathrooms"
                        v-model="maxBathrooms"
                        min="1"
                        max="10"
                    />
                    </div>
                </div>

            <!-- min to max bedrooms -->
                <div class="flex flex-col" style="margin-left: 70px;">
                    <label
                    for="min-bedrooms"
                    class="block text-sm font-medium text-gray-700"
                    style="text-align: center;">
                    Min bedrooms
                    </label>
                    <div class="mt-1">
                    <input
                        class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        id="min-bedrooms"
                        v-model="minBedrooms"
                        min="1"
                        max="10000"/>
                    </div>
                </div>

                <div class="flex flex-col" style="margin-left: 70px;">
                    <label
                    for="max-bedrooms"
                    class="block text-sm font-medium text-gray-700"
                    style="text-align: center;">
                    Max bedrooms
                    </label>
                    <div class="mt-1">
                    <input
                        class="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
                        type="number"
                        id="max-bedrooms"
                        v-model="maxBedrooms"
                        min="1"
                        max="10000"
                    />
                    </div>
                </div>

            <!-- Proximity -->
                <div class="my-4 flex flex-col space-x-6" style="margin-top: 50px; margin-left: 70px;">
                    
                    <select id="proximity" v-model="proximity" class="mx-2 bg-white border border-gray-300 text-black text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block p-2.5">
                        <option value="On Campus">On Campus</option>
                        <option value="Off Campus">Off Campus</option>
                        <option value="No Preference">No Preference</option>
                    </select> 
                </div>
            </div>
        </div>
        </section>
</template>