<template>
  <div class="max-w-2xl mx-auto px-4 py-14">
    <div class="text-center">
      <h1 class="text-3xl font-semibold text-veryDarkBlue">Post a Sublease</h1>
      <p class="text-darkGrayishBlue mt-1">List your place directly — no agency, no listing fee.</p>
    </div>

    <div class="card mt-10 p-8">
      <form @submit.prevent="submit">
        <div class="mb-4">
          <label for="title" class="field-label">Listing title</label>
          <input type="text" id="title" v-model="title" class="field-input" placeholder="e.g. Sunny 1BR near campus, fall semester" required>
        </div>
        <div class="mb-4">
          <label for="address" class="field-label">Address</label>
          <input type="text" id="address" v-model="address" class="field-input" placeholder="Street address, Atlanta, GA" required>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 mb-4">
          <div>
            <label for="rent" class="field-label">Rent</label>
            <input type="number" id="rent" v-model.number="rent" class="field-input" min="1" required>
          </div>
          <div>
            <label for="bedrooms" class="field-label">Bedrooms</label>
            <input type="number" id="bedrooms" v-model.number="bedrooms" class="field-input" min="0" required>
          </div>
          <div>
            <label for="bathrooms" class="field-label">Bathrooms</label>
            <input type="number" id="bathrooms" v-model.number="bathrooms" class="field-input" min="1" required>
          </div>
          <div class="flex items-end pb-2.5">
            <label class="flex items-center gap-2 text-sm text-darkGrayishBlue">
              <input type="checkbox" v-model="isStudio">
              Studio
            </label>
          </div>
        </div>
        <div class="mb-4">
          <label for="available-date" class="field-label">Available from</label>
          <input type="text" id="available-date" v-model="availableDate" class="field-input" placeholder="e.g. 2024-08-01" required>
        </div>
        <div class="mb-2">
          <label for="contact-email" class="field-label">Contact email</label>
          <input type="email" id="contact-email" v-model="contactEmail" class="field-input" required>
        </div>
        <p v-if="submitError" class="text-sm text-red-600 mt-2">{{ submitError }}</p>
        <button type="submit" :disabled="submitting" class="btn-solid btn-lg btn-block mt-5">Post sublease</button>
      </form>
    </div>
  </div>

  <Footer></Footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { auth } from '../firebase';
import Footer from '../components/Footer.vue';

export default defineComponent({
  components: {
    Footer,
  },
  data() {
    return {
      title: '',
      address: '',
      rent: null as number | null,
      bedrooms: null as number | null,
      bathrooms: null as number | null,
      isStudio: false,
      availableDate: '',
      contactEmail: auth.currentUser?.email || '',
      submitting: false,
      submitError: '',
    };
  },
  methods: {
    async submit() {
      this.submitError = '';
      this.submitting = true;
      try {
        const idToken = await auth.currentUser?.getIdToken();
        const response = await fetch(import.meta.env.VITE_SUBMIT_SUBLEASE_ENDPOINT_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${idToken}`,
          },
          body: JSON.stringify({
            title: this.title,
            address: this.address,
            rent: this.rent,
            bedrooms: this.bedrooms,
            bathrooms: this.bathrooms,
            is_studio: this.isStudio,
            available_date: this.availableDate,
            contact_email: this.contactEmail,
          }),
        });

        if (!response.ok) {
          const body = await response.json().catch(() => ({}));
          throw new Error(body.error || `Request failed with status ${response.status}`);
        }

        alert('Sublease posted, thank you!');
        this.$router.push('/search');
      } catch (e: any) {
        this.submitError = e.message || 'Failed to post sublease.';
      } finally {
        this.submitting = false;
      }
    },
  },
});
</script>
