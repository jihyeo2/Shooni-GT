import { createStore } from 'vuex'

export default createStore({
    state: {
        filter: {
            minBedrooms: 1,
            maxBedrooms: 5,
            minBathrooms: 1,
            maxBathrooms: 5,
            minRent: 0,
            maxRent: 9999,
            proximity: 'No Preference',
            selectedApartments: [],
        }
    },
    mutations: {
        UPDATE_FILTER(state, payload) {
            state.filter = payload
        }
    }, 
    actions: {
        updateFilter(context, payload) {
            context.commit('UPDATE_FILTER', payload)
        }
    },
    getters: {
        getFilter: function(state) {
            return state.filter
        }
    }

})

