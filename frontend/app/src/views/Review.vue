<template>
  <div class="max-w-3xl mx-auto px-4 py-14">
    <div class="flex flex-col items-center text-center">
      <img src="../assets/images/room.jpg" class="review-photo" />
      <h1 class="text-3xl font-semibold text-veryDarkBlue mt-6">Modera Atlanta</h1>
      <p class="text-darkGrayishBlue mt-1">A spacious and modern apartment with stunning city views</p>
    </div>

    <div class="card mt-10 p-8">
      <h2 class="text-center text-sm font-semibold text-darkGrayishBlue uppercase tracking-wide">Leave a review to help others find the right place</h2>
      <h3 class="text-center text-xl font-semibold text-veryDarkBlue mt-1">Overall rating</h3>
      <div class="flex justify-center gap-1 mt-3 text-4xl">
        <span class="star" v-for="n in 5" :key="n" @click="setRating(n)" :class="{ 'star-filled': n <= rating }">&#9733;</span>
      </div>

      <div class="rating-grid mt-8">
        <div class="rating-row">
          <span class="rating-label">Safety</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'safety'+n" @click="setSafetyRating(n)" :class="{ 'star-filled': n <= safetyRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Location</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'location'+n" @click="setLocationRating(n)" :class="{ 'star-filled': n <= locationRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Facilities</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'facilities'+n" @click="setFacilitiesRating(n)" :class="{ 'star-filled': n <= facilitiesRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Quietness</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'quietness'+n" @click="setQuietnessRating(n)" :class="{ 'star-filled': n <= quietnessRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Pets</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'pets'+n" @click="setPetsRating(n)" :class="{ 'star-filled': n <= petsRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Value</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'value'+n" @click="setValueRating(n)" :class="{ 'star-filled': n <= valueRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Parking</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'parking'+n" @click="setParkingRating(n)" :class="{ 'star-filled': n <= parkingRating }">&#9733;</span></span>
        </div>
        <div class="rating-row">
          <span class="rating-label">Communication</span>
          <span class="stars-sm"><span class="star" v-for="n in 5" :key="'communication'+n" @click="setCommunicationRating(n)" :class="{ 'star-filled': n <= communicationRating }">&#9733;</span></span>
        </div>
      </div>

      <form class="mt-8" @submit.prevent>
        <div class="mb-4">
          <label for="name" class="field-label">Title</label>
          <input type="text" id="name" name="name" v-model="title" class="field-input" required>
        </div>
        <div class="mb-2">
          <label for="comment" class="field-label">Comments</label>
          <textarea id="comment" name="comment" rows="4" v-model="comment" class="field-input" required></textarea>
        </div>
        <p v-if="submitError" class="text-sm text-red-600 mt-2">{{ submitError }}</p>
        <button type="button" @click="submitRating" :disabled="submitting" class="btn-solid btn-lg mt-5">Submit review</button>
      </form>
    </div>
  </div>

  <Footer></Footer>
</template>

<style scoped>
.review-photo {
  width: 220px;
  height: 220px;
  object-fit: cover;
  border-radius: 1rem;
  box-shadow: 0 8px 24px rgba(72,36,82,0.12);
}
.rating-grid {
  @apply grid grid-cols-1 sm:grid-cols-2 gap-x-10 gap-y-1;
}
.rating-row {
  @apply flex items-center justify-between border-b border-gray-100 py-2.5;
}
.rating-label {
  @apply text-sm font-semibold text-veryDarkBlue;
}
.stars-sm {
  font-size: 1.1rem;
}
.star {
  color: #d8d8de;
  cursor: pointer;
  transition: color 0.15s ease;
}
.star-filled {
  color: #F4774E !important;
}
</style>

<script lang="ts">
import { defineComponent } from 'vue';
import store from '../store';
import { auth } from '../firebase';
import Footer from '../components/Footer.vue';

export default defineComponent({
components: {
  Footer,
},
data() {
  return {
    apartment: 0,
    rating: 0,
    safetyRating: 0,
    facilitiesRating: 0,
    petsRating: 0,
    parkingRating: 0,
    locationRating: 0,
    quietnessRating: 0,
    valueRating: 0,
    communicationRating: 0,
    title: '',
    comment: '',
    submitting: false,
    submitError: '',
  };
},
methods: {
  setRating(value: number) {
    this.rating = value;
  },
  setSafetyRating(value: number) {
    this.safetyRating = value;
  },
  setFacilitiesRating(value: number) {
    this.facilitiesRating = value;
  },
  setPetsRating(value: number) {
    this.petsRating = value;
  },
  setParkingRating(value: number) {
    this.parkingRating = value;
  },
  setLocationRating(value: number) {
    this.locationRating = value;
  },
  setQuietnessRating(value: number) {
    this.quietnessRating = value;
  },
  setValueRating(value: number) {
    this.valueRating = value;
  },
  setCommunicationRating(value: number) {
    this.communicationRating = value;
  },
  async submitRating() {
    this.submitError = '';

    if (!store.getters.isLoggedIn) {
      alert('Please log in to submit a review.');
      this.$router.push('/login');
      return;
    }

    if (this.rating === 0 || this.safetyRating === 0 || this.facilitiesRating === 0 || this.petsRating === 0
          || this.parkingRating === 0 || this.locationRating === 0 || this.quietnessRating === 0 || this.valueRating === 0
          || this.communicationRating === 0) {
      alert('Please rate all sections first');
      return;
    }

    this.submitting = true;
    try {
      const idToken = await auth.currentUser?.getIdToken();
      const response = await fetch(import.meta.env.VITE_REVIEW_ENDPOINT_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${idToken}`,
        },
        body: JSON.stringify({
          title: this.title,
          comment: this.comment,
          rating: this.rating,
          safetyRating: this.safetyRating,
          facilitiesRating: this.facilitiesRating,
          petsRating: this.petsRating,
          parkingRating: this.parkingRating,
          locationRating: this.locationRating,
          quietnessRating: this.quietnessRating,
          valueRating: this.valueRating,
          communicationRating: this.communicationRating,
        }),
      });

      if (!response.ok) {
        const body = await response.json().catch(() => ({}));
        throw new Error(body.error || `Request failed with status ${response.status}`);
      }

      alert('Review submitted, thank you!');
    } catch (e: any) {
      this.submitError = e.message || 'Failed to submit review.';
    } finally {
      this.submitting = false;
    }
  },
},
});
</script>
