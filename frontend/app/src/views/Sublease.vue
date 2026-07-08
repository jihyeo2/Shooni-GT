<script lang="ts">
import Footer from '../components/Footer.vue'
import { defineComponent } from 'vue';
import store from '../store'

export default defineComponent({
  components: {
    Footer,
  },
  methods: {
    browseSubleases() {
      // Set before navigating so Search.vue/FilterBar read the pre-selected
      // filter at mount time, same store-driven mechanism the filter chips
      // already use -- no query-param parsing needed on the Search side.
      store.dispatch('updateFilter', { ...store.state.filter, listingTypes: ['sublease'] })
    },
  },
})
</script>

<template>
    <section class="sublease-hero">
        <h1 class="sublease-hero-heading">Subleasing? We've got you covered.</h1>
        <h3 class="sublease-hero-sub">Find a sublease, or post your own in minutes.</h3>
    </section>

    <section class="py-20 px-6 md:px-16 bg-white">
        <div class="max-w-4xl mx-auto grid md:grid-cols-2 gap-6">
            <div class="sublease-card">
                <div class="sublease-card-img" style="background-image: url('/src/assets/images/gg2.png')"></div>
                <div class="p-6">
                    <h5 class="sublease-card-title">Browse Subleases</h5>
                    <p class="sublease-card-body">See every sublease listed on Shooni, filtered and ready to compare.</p>
                    <router-link to="/search" class="btn-solid" @click="browseSubleases">Browse</router-link>
                </div>
            </div>

            <div class="sublease-card">
                <div class="sublease-card-img" style="background-image: url('/src/assets/images/room.jpg')"></div>
                <div class="p-6">
                    <h5 class="sublease-card-title">Post a Sublease</h5>
                    <p class="sublease-card-body">Subleasing your place? List it directly -- no agency, no listing fee.</p>
                    <router-link to="/sublease/new" class="btn-solid">Post</router-link>
                </div>
            </div>
        </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
.sublease-hero {
    height: 60vh;
    min-height: 340px;
    background-image: url("/src/assets/images/labg.jpg");
    background-position: center;
    background-size: cover;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 6%;
}
.sublease-hero-heading {
    font-family: 'Inria Serif', serif;
    font-weight: 700;
    font-size: 2.75rem;
    line-height: 1.3;
    color: white;
}
.sublease-hero-sub {
    font-family: 'Inria Serif', serif;
    font-weight: 500;
    font-size: 1.15rem;
    color: white;
    margin-top: 2.75rem;
}

.sublease-card {
    @apply bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden transition-transform duration-200;
}
.sublease-card:hover {
    transform: translateY(-4px);
    @apply shadow-lg;
}
.sublease-card-img {
    height: 180px;
    background-position: center;
    background-size: cover;
    position: relative;
    transition: opacity 0.3s ease-in-out;
}
.sublease-card-img:hover {
    opacity: 0.85;
}
.sublease-card-title {
    @apply text-lg font-semibold text-brightRed mb-2;
}
.sublease-card-body {
    @apply text-sm text-darkGrayishBlue mb-4;
}

@media (max-width: 768px) {
    .sublease-hero-heading { font-size: 2rem; }
}
</style>
