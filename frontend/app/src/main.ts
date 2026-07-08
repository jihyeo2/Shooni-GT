import { createApp } from 'vue'
import './index.css'
import App from './App.vue'
import router from './router'
import store from './store'
import { auth } from './firebase'
import { onAuthStateChanged } from 'firebase/auth'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome"
import {
    faBath,
    faBed,
    faHome,
    faSignHanging,
    faLocationPin,
    faDollarSign,
    faChevronDown,
    faHeart,
    faUser,
    faTrash,
  } from '@fortawesome/free-solid-svg-icons'



library.add(faBath, faBed, faHome, faSignHanging, faLocationPin, faDollarSign, faChevronDown, faHeart, faUser, faTrash)

const app = createApp(App)

app.use(router).use(store).component('font-awesome-icon', FontAwesomeIcon).mount('#app')

// Persists login across page reloads and keeps the store in sync with Firebase Auth.
onAuthStateChanged(auth, (user) => {
    store.dispatch('setUser', user)
})