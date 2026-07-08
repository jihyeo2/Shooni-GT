<template>
  <div class="max-w-4xl mx-auto px-4 py-14">
    <h1 class="text-3xl font-semibold text-veryDarkBlue text-center">Your Dashboard</h1>

    <div class="card mt-10 p-8">
      <h2 class="text-xl font-semibold text-veryDarkBlue mb-5">Profile</h2>
      <div class="mb-4">
        <label class="field-label">Display name</label>
        <input type="text" v-model="displayName" class="field-input" placeholder="Add a display name">
      </div>
      <p class="text-sm text-darkGrayishBlue mb-4">{{ email }}</p>
      <p v-if="profileError" class="text-sm text-red-600 mb-3">{{ profileError }}</p>
      <p v-if="profileSaved" class="text-sm text-green-700 mb-3">Saved!</p>
      <button type="button" class="btn-solid" :disabled="savingProfile" @click="saveProfile">Save changes</button>
    </div>

    <div class="mt-10">
      <h2 class="text-xl font-semibold text-veryDarkBlue mb-4">
        Saved listings ({{ favorites.length }})
      </h2>
      <p v-if="favorites.length === 0" class="text-darkGrayishBlue">
        You haven't saved any listings yet — look for the heart icon on a listing card.
      </p>
      <div v-else class="flex flex-wrap gap-4">
        <ArticleCard v-for="f in favorites" :key="f.id" :source="f" />
      </div>
    </div>

    <div class="mt-10">
      <h2 class="text-xl font-semibold text-veryDarkBlue mb-4">
        My subleases ({{ mySubleases.length }})
      </h2>
      <p v-if="subleasesError" class="text-sm text-red-600">{{ subleasesError }}</p>
      <p v-else-if="!subleasesLoading && mySubleases.length === 0" class="text-darkGrayishBlue">
        You haven't posted any subleases yet.
      </p>
      <div v-else class="flex flex-wrap gap-4">
        <ArticleCard v-for="s in mySubleases" :key="s.id" :source="s" deletable @delete="deleteSublease" />
      </div>
    </div>

    <div class="mt-10">
      <h2 class="text-xl font-semibold text-veryDarkBlue mb-4">
        My reviews ({{ myReviews.length }})
      </h2>
      <p v-if="reviewsError" class="text-sm text-red-600">{{ reviewsError }}</p>
      <p v-else-if="!reviewsLoading && myReviews.length === 0" class="text-darkGrayishBlue">
        You haven't submitted any reviews yet.
      </p>
      <div v-else class="flex flex-col gap-4">
        <ReviewCard v-for="r in myReviews" :key="r.id" :review="r" deletable @delete="deleteReview" />
      </div>
    </div>
  </div>

  <Footer></Footer>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { updateProfile } from 'firebase/auth';
import store from '../store';
import { auth } from '../firebase';
import ArticleCard from '../components/ArticleCard.vue';
import ReviewCard from '../components/ReviewCard.vue';
import Footer from '../components/Footer.vue';

export default defineComponent({
  components: {
    ArticleCard,
    ReviewCard,
    Footer,
  },
  data() {
    return {
      displayName: auth.currentUser?.displayName || '',
      email: auth.currentUser?.email || '',
      savingProfile: false,
      profileError: '',
      profileSaved: false,
      myReviews: [] as Array<any>,
      reviewsLoading: true,
      reviewsError: '',
      mySubleases: [] as Array<any>,
      subleasesLoading: true,
      subleasesError: '',
    };
  },
  computed: {
    favorites() {
      return store.getters.favorites;
    },
  },
  mounted() {
    store.dispatch('loadFavorites');
    this.fetchMyReviews();
    this.fetchMySubleases();
  },
  methods: {
    async saveProfile() {
      this.profileError = '';
      this.profileSaved = false;
      this.savingProfile = true;
      try {
        if (!auth.currentUser) throw new Error('Not logged in');
        await updateProfile(auth.currentUser, { displayName: this.displayName });
        // Same reasoning as SignUp.vue: updateProfile doesn't reliably re-fire
        // onAuthStateChanged right away, so push the updated user into the
        // store directly so NavBar reflects the change immediately.
        store.dispatch('setUser', auth.currentUser);
        this.profileSaved = true;
      } catch (e: any) {
        this.profileError = e.message || 'Failed to save profile.';
      } finally {
        this.savingProfile = false;
      }
    },
    async fetchMyReviews() {
      this.reviewsLoading = true;
      this.reviewsError = '';
      try {
        const idToken = await auth.currentUser?.getIdToken();
        const response = await fetch(`${import.meta.env.VITE_GET_REVIEWS_ENDPOINT_URL}?mine=true`, {
          headers: { 'Authorization': `Bearer ${idToken}` },
        });
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        this.myReviews = await response.json();
      } catch (e: any) {
        this.reviewsError = e.message || 'Failed to load your reviews.';
      } finally {
        this.reviewsLoading = false;
      }
    },
    async deleteReview(id: string) {
      if (!confirm('Delete this review?')) return;
      try {
        const idToken = await auth.currentUser?.getIdToken();
        const response = await fetch(`${import.meta.env.VITE_DELETE_REVIEW_ENDPOINT_URL}?id=${encodeURIComponent(id)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${idToken}` },
        });
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        await this.fetchMyReviews();
      } catch (e: any) {
        alert(e.message || 'Failed to delete review.');
      }
    },
    async fetchMySubleases() {
      this.subleasesLoading = true;
      this.subleasesError = '';
      try {
        const idToken = await auth.currentUser?.getIdToken();
        const response = await fetch(`${import.meta.env.VITE_GET_SUBLEASES_ENDPOINT_URL}?mine=true`, {
          headers: { 'Authorization': `Bearer ${idToken}` },
        });
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        this.mySubleases = await response.json();
      } catch (e: any) {
        this.subleasesError = e.message || 'Failed to load your subleases.';
      } finally {
        this.subleasesLoading = false;
      }
    },
    async deleteSublease(id: string) {
      if (!confirm('Delete this sublease listing?')) return;
      try {
        const idToken = await auth.currentUser?.getIdToken();
        const response = await fetch(`${import.meta.env.VITE_DELETE_SUBLEASE_ENDPOINT_URL}?id=${encodeURIComponent(id)}`, {
          method: 'DELETE',
          headers: { 'Authorization': `Bearer ${idToken}` },
        });
        if (!response.ok) {
          throw new Error(`Request failed with status ${response.status}`);
        }
        await this.fetchMySubleases();
      } catch (e: any) {
        alert(e.message || 'Failed to delete sublease.');
      }
    },
  },
});
</script>
