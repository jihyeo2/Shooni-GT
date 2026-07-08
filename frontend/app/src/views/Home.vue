<script lang="ts">
import Footer from '../components/Footer.vue'
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    Footer,
  },
})
</script>

<template>
    <section class="hero">
      <div class="hero-copy">
        <h1 class="hero-heading">Leave the nest.<br>Find your new home<br><span class="text-brightRed">with us.</span></h1>
        <p class="hero-sub">Been there. Done that, we got this.</p>
        <div class="flex flex-wrap gap-3 mt-6">
          <router-link to="/rent" class="btn-solid btn-lg">I am a renter</router-link>
          <div class="btn-ghost btn-lg">I am a homeowner</div>
        </div>
      </div>
      <img src="../assets/images/bird1.png" class="hero-bird" alt="">
    </section>

    <section class="py-20 px-6 md:px-16 bg-white">
        <div class="max-w-3xl mx-auto text-center">
            <img src="../assets/images/logo.png" class="h-24 mx-auto mb-6"/>
            <h2 class="text-3xl font-semibold text-veryDarkBlue">Renting is time consuming.</h2>
            <p class="mt-4 text-darkGrayishBlue text-lg">
                We are here to help you narrow down options, save your time and money, and find you the best appropriate residences.
            </p>
        </div>

        <div class="max-w-6xl mx-auto grid md:grid-cols-3 gap-6 mt-14">
            <div class="feature-card">
                <img src="../assets/images/gg.jpg" alt="Apartment interior" class="feature-card-img">
                <h3 class="feature-card-title">Explore different housing options</h3>
                <p class="feature-card-body">Many housing resources for you to choose from — fancy luxury apartments to nearby convenient campus dorms. Connect with real estate agents to get everything started earlier.</p>
            </div>
            <div class="feature-card">
                <img src="../assets/images/emm.jpg" alt="Living room interior" class="feature-card-img">
                <h3 class="feature-card-title">Visit different housing designs</h3>
                <p class="feature-card-body">Thousands of characteristic interior designs and room features. Classical, modern, fantastic views — find all your preferences here.</p>
            </div>
            <div class="feature-card">
                <img src="../assets/images/sss.png" alt="Apartment building" class="feature-card-img">
                <h3 class="feature-card-title">Compare on and off campus housing</h3>
                <p class="feature-card-body">Compare on-campus and off-campus housing side by side. Enjoy college life while saving on rent and making new friends.</p>
            </div>
        </div>
    </section>

    <section class="nudge">
        <div class="max-w-6xl mx-auto grid md:grid-cols-2 gap-10 items-center px-6 md:px-16">
            <div>
                <h2 class="text-3xl font-semibold text-white">Shooni remembers you.</h2>
                <p class="mt-3 text-white/80 text-lg">Sign in to save your progress, get recommendations, and more!</p>
            </div>
            <img src="../assets/images/bg1.png" class="rounded-2xl shadow-lg" />
        </div>
    </section>

    <section class="py-20 px-6 flex justify-center bg-veryLightGray">
        <div class="card w-full max-w-md p-8">
            <h2 class="text-2xl font-semibold text-veryDarkBlue mb-6">Contact Us</h2>
            <div class="mb-4">
                <label class="field-label" for="name">Name</label>
                <input id="name" class="field-input" placeholder="Enter your name">
            </div>
            <div class="mb-4">
                <label class="field-label" for="email">Email address</label>
                <input id="email" type="email" class="field-input" placeholder="Enter your email">
            </div>
            <div class="mb-6">
                <label class="field-label" for="message">Message</label>
                <textarea id="message" rows="5" class="field-input" placeholder="Enter your message"></textarea>
            </div>
            <button type="submit" class="btn-solid btn-lg btn-block">Submit</button>
        </div>
    </section>

<Footer></Footer>
</template>

<style scoped>
.hero {
    position: relative;
    min-height: 560px;
    display: flex;
    align-items: center;
    background-image: linear-gradient(100deg, rgba(255,251,247,0.94) 0%, rgba(255,251,247,0.75) 40%, rgba(255,251,247,0.1) 65%, rgba(255,251,247,0) 80%), url("/images/bg.png");
    background-position: center;
    background-size: cover;
    padding: 0 6%;
}
.hero-copy {
    max-width: 560px;
}
.hero-heading {
    font-family: 'Inria Serif', serif;
    font-weight: 400;
    font-size: 3.25rem;
    line-height: 1.15;
    color: #1D1E25;
}
.hero-sub {
    font-family: 'Inria Serif', serif;
    font-size: 1.25rem;
    color: #1D1E25;
    margin-top: 1rem;
}
.hero-bird {
    position: absolute;
    right: 6%;
    bottom: 6%;
    width: 200px;
    filter: drop-shadow(0 18px 26px rgba(29,30,37,0.3));
}

.feature-card {
    @apply bg-white rounded-2xl border border-gray-200 overflow-hidden transition-transform duration-200;
}
.feature-card:hover {
    transform: translateY(-4px);
    @apply shadow-lg;
}
.feature-card-img {
    @apply w-full h-40 object-cover;
}
.feature-card-title {
    @apply text-lg font-semibold text-veryDarkBlue px-6 pt-5;
}
.feature-card-body {
    @apply text-sm text-darkGrayishBlue px-6 py-4;
}

.nudge {
    @apply py-20 bg-darkBlue;
}

@media (max-width: 768px) {
    .hero { min-height: 480px; padding: 0 6%; }
    .hero-heading { font-size: 2.25rem; }
    .hero-bird { width: 120px; }
}
</style>
