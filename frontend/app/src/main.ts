import { createApp } from 'vue'
import './index.css'
import App from './App.vue'
import router from './router'
import store from './store'
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
  } from '@fortawesome/free-solid-svg-icons'



library.add(faBath, faBed, faHome, faSignHanging, faLocationPin, faDollarSign, faChevronDown)

const app = createApp(App)

app.use(router).use(store).component('font-awesome-icon', FontAwesomeIcon).mount('#app')