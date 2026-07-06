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
        <div class="card flex flex-wrap items-end gap-6 px-6 py-5">
            <div>
                <label for="min-rent" class="field-label">Min rent</label>
                <input class="field-input w-28" type="number" id="min-rent" v-model="minRent" min="1" max="10000" />
            </div>
            <div>
                <label for="max-rent" class="field-label">Max rent</label>
                <input class="field-input w-28" type="number" id="max-rent" v-model="maxRent" min="1" max="10000" />
            </div>
            <div>
                <label for="min-bathrooms" class="field-label">Min baths</label>
                <input class="field-input w-24" type="number" id="min-bathrooms" v-model="minBathrooms" min="1" max="10" />
            </div>
            <div>
                <label for="max-bathrooms" class="field-label">Max baths</label>
                <input class="field-input w-24" type="number" id="max-bathrooms" v-model="maxBathrooms" min="1" max="10" />
            </div>
            <div>
                <label for="min-bedrooms" class="field-label">Min bedrooms</label>
                <input class="field-input w-24" type="number" id="min-bedrooms" v-model="minBedrooms" min="1" max="10000" />
            </div>
            <div>
                <label for="max-bedrooms" class="field-label">Max bedrooms</label>
                <input class="field-input w-24" type="number" id="max-bedrooms" v-model="maxBedrooms" min="1" max="10000" />
            </div>
            <div class="flex-1 min-w-[140px]">
                <label for="proximity" class="field-label">Proximity</label>
                <select id="proximity" v-model="proximity" class="field-input">
                    <option value="On Campus">On Campus</option>
                    <option value="Off Campus">Off Campus</option>
                    <option value="No Preference">No Preference</option>
                </select>
            </div>
        </div>
    </section>
</template>