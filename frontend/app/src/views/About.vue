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
    <section class="about-hero">
      <h1 class="about-hero-heading">About us</h1>
    </section>

    <section class="py-20 px-6 md:px-16 bg-white">
      <div class="max-w-5xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div>
          <h2 class="text-3xl font-semibold text-veryDarkBlue mb-5">Our Mission</h2>
          <p class="text-lg text-darkGrayishBlue leading-relaxed">
            The search for housing is complicated for college students because they have little time and money
            but a lot of pressure to find housing near their schools and no centralized place to search for it.
            We aim to simplify the search process for college students to find desirable housing by creating
            that centralized location — Shooni.
          </p>
        </div>
        <div class="flex justify-center">
          <img src="/src/assets/images/au2.jpg" class="about-photo" alt="Students moving into an apartment">
        </div>
      </div>
    </section>

    <section class="py-20 px-6 md:px-16 bg-veryLightGray">
      <div class="max-w-5xl mx-auto grid md:grid-cols-2 gap-12 items-center">
        <div class="order-2 md:order-1 flex justify-center">
          <img src="/src/assets/images/au3.jpg" class="about-photo" alt="Students in a shared living space">
        </div>
        <div class="order-1 md:order-2">
          <h2 class="text-3xl font-semibold text-veryDarkBlue mb-5">Our Values</h2>
          <p class="text-lg text-darkGrayishBlue leading-relaxed">
            We aim to develop a rating system, a roommate search system, and an interactive map on our website.
            We want to share subleasing opportunities for students in need of short-term housing; we want to
            establish a user-friendly forum for students to find their perfect roommates; we want students to be
            excited to leave the nest. We believe our idea will provide a more efficient and effective experience
            for students.
          </p>
        </div>
      </div>
    </section>

    <Footer></Footer>
</template>

<style scoped>
.about-hero {
  height: 320px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-image: linear-gradient(rgba(29,30,37,0.45), rgba(29,30,37,0.45)), url("/src/assets/images/aubg1.jpg");
  background-position: center;
  background-size: cover;
}
.about-hero-heading {
  font-family: 'Inria Serif', serif;
  font-size: 3rem;
  font-weight: 400;
  color: white;
}

.about-photo {
  width: 100%;
  max-width: 420px;
  border-radius: 1rem;
  object-fit: cover;
  box-shadow: 0 12px 30px rgba(72,36,82,0.15);
}

@media (max-width: 768px) {
  .about-hero-heading { font-size: 2.25rem; }
}
</style>
