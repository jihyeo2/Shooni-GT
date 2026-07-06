<script lang="ts">
import Footer from '../components/Footer.vue'
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    Footer,
  }
})
</script>

<template>
    <section class="rent-hero">
        <h1 class="rent-hero-heading">Let's build the perfect home for you!</h1>
        <h3 class="rent-hero-sub">Currently available for: Georgia Institute of Technology</h3>
        <router-link to="/filter" class="btn-solid btn-lg mt-8">Start your search</router-link>
    </section>

    <section class="py-20 px-6 md:px-16 bg-white">
        <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6">
            <div class="rent-card">
                <div class="rent-card-img" style="background-image: url('/src/assets/images/bg11.png')"></div>
                <div class="p-6">
                    <h5 class="rent-card-title">Find your Roomies</h5>
                    <p class="rent-card-body">Search your area and find the perfect roommate(s) for you!</p>
                    <router-link to="/roommate" class="btn-solid">Finder</router-link>
                </div>
            </div>

            <div class="rent-card">
                <div class="rent-card-img" style="background-image: url('/src/assets/images/bg22.png')"></div>
                <div class="p-6">
                    <h5 class="rent-card-title">Join the Community</h5>
                    <p class="rent-card-body">Chat with other students and explore the marketplace!</p>
                    <a href="https://sites.gatech.edu/shooni/" class="btn-solid">Join</a>
                </div>
            </div>

            <div class="rent-card">
                <div class="rent-card-img" style="background-image: url('/src/assets/images/bg33.png')"></div>
                <div class="p-6">
                    <h5 class="rent-card-title">Create an account</h5>
                    <p class="rent-card-body">Sign up to receive all the benefits Shooni has to offer!</p>
                    <router-link to="/signup" class="btn-solid">Create</router-link>
                </div>
            </div>
        </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
.rent-hero {
    height: 85vh;
    min-height: 420px;
    background-image: url("/src/assets/images/labg2.png");
    background-position: center;
    background-size: cover;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 0 6%;
}
.rent-hero-heading {
    font-family: 'Inria Serif', serif;
    font-weight: 700;
    font-size: 3rem;
    color: white;
}
.rent-hero-sub {
    font-family: 'Inria Serif', serif;
    font-weight: 500;
    font-size: 1.25rem;
    color: white;
    margin-top: 1rem;
}

.rent-card {
    @apply bg-white rounded-2xl border border-gray-200 shadow-sm overflow-hidden transition-transform duration-200;
}
.rent-card:hover {
    transform: translateY(-4px);
    @apply shadow-lg;
}
.rent-card-img {
    height: 160px;
    background-position: center;
    background-size: cover;
    position: relative;
    transition: opacity 0.3s ease-in-out;
}
.rent-card-img:hover {
    opacity: 0.85;
}
.rent-card-title {
    @apply text-lg font-semibold text-brightRed mb-2;
}
.rent-card-body {
    @apply text-sm text-darkGrayishBlue mb-4;
}

@media (max-width: 768px) {
    .rent-hero-heading { font-size: 2rem; }
}
</style>
