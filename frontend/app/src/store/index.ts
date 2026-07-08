import { createStore } from 'vuex'
import type { User } from 'firebase/auth'
import type { Article } from '../types'
import { auth } from '../firebase'

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

async function authHeader(): Promise<Record<string, string>> {
    const idToken = await auth.currentUser?.getIdToken()
    return idToken ? { 'Authorization': `Bearer ${idToken}` } : {}
}

// A listing's `link` alone isn't a unique identity: several complexes list
// all their units under one floorplans page URL with no per-unit anchor, so
// multiple distinct units can share the exact same link. Mirrors the same
// composite used server-side (backend_favorites/main.py's _favorite_key) so
// the frontend's "is this favorited" check lines up with what the backend
// actually stored a favorite doc under.
function favoriteKey(article: Pick<Article, 'link' | 'bedrooms' | 'bathrooms' | 'rent' | 'is_studio' | 'available_date'>): string {
    return [article.link, article.bedrooms, article.bathrooms, article.rent, article.is_studio, article.available_date].join('|')
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
            listingTypes: [],
        },
        user: null as UserSnapshot | null,
        favorites: [] as Article[],
    },
    mutations: {
        UPDATE_FILTER(state, payload) {
            state.filter = payload
        },
        SET_USER(state, user: UserSnapshot | null) {
            state.user = user
        },
        SET_FAVORITES(state, favorites: Article[]) {
            state.favorites = favorites
        }
    },
    actions: {
        updateFilter(context, payload) {
            context.commit('UPDATE_FILTER', payload)
        },
        setUser(context, user: User | null) {
            const previousUid = context.state.user?.uid ?? null
            context.commit('SET_USER', toSnapshot(user))

            if (!user) {
                context.commit('SET_FAVORITES', [])
            } else if (user.uid !== previousUid) {
                context.dispatch('loadFavorites')
            }
        },
        async loadFavorites(context) {
            try {
                const response = await fetch(import.meta.env.VITE_GET_FAVORITES_ENDPOINT_URL, {
                    headers: await authHeader(),
                })
                if (!response.ok) throw new Error(`Request failed with status ${response.status}`)
                const favorites = await response.json()
                context.commit('SET_FAVORITES', favorites.map((f: any, index: number) => ({ ...f, id: index })))
            } catch (e) {
                console.error('Failed to load favorites', e)
            }
        },
        async toggleFavorite(context, article: Article) {
            try {
                const response = await fetch(import.meta.env.VITE_TOGGLE_FAVORITE_ENDPOINT_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        ...(await authHeader()),
                    },
                    body: JSON.stringify({
                        link: article.link,
                        article: {
                            address: article.address,
                            apartment: article.apartment,
                            available_date: article.available_date,
                            bathrooms: article.bathrooms,
                            bedrooms: article.bedrooms,
                            is_studio: article.is_studio,
                            rent: article.rent,
                            latitude: article.latitude,
                            longitude: article.longitude,
                        },
                    }),
                })
                if (!response.ok) throw new Error(`Request failed with status ${response.status}`)
                await context.dispatch('loadFavorites')
            } catch (e) {
                console.error('Failed to toggle favorite', e)
            }
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
        },
        favorites: function(state) {
            return state.favorites
        },
        isFavorited: function(state) {
            return (article: Article) => state.favorites.some(f => favoriteKey(f) === favoriteKey(article))
        }
    }

})
