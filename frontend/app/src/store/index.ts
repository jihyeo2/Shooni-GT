import { createStore } from 'vuex'
import type { User } from 'firebase/auth'

// Only a plain, serializable snapshot of the user is kept in the store --
// never the live Firebase User instance. Firebase mutates that object's
// fields in place (e.g. updateProfile), and Vue's reactivity does a
// reference-equality check, so re-dispatching the same mutated object is
// indistinguishable from "nothing changed" and never triggers a re-render.
export type UserSnapshot = {
    uid: string
    email: string | null
    displayName: string | null
}

function toSnapshot(user: User | null): UserSnapshot | null {
    if (!user) return null
    return { uid: user.uid, email: user.email, displayName: user.displayName }
}

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
        },
        user: null as UserSnapshot | null,
    },
    mutations: {
        UPDATE_FILTER(state, payload) {
            state.filter = payload
        },
        SET_USER(state, user: UserSnapshot | null) {
            state.user = user
        }
    },
    actions: {
        updateFilter(context, payload) {
            context.commit('UPDATE_FILTER', payload)
        },
        setUser(context, user: User | null) {
            context.commit('SET_USER', toSnapshot(user))
        }
    },
    getters: {
        getFilter: function(state) {
            return state.filter
        },
        currentUser: function(state) {
            return state.user
        },
        isLoggedIn: function(state) {
            return state.user !== null
        }
    }

})

