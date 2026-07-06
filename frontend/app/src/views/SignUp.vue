<template>
  <div class="min-h-[80vh] flex items-center justify-center bg-veryLightGray px-4 py-16">
    <div class="auth-card">
      <img src="../assets/images/logo.png" class="h-9 mx-auto mb-5" alt="Shooni">
      <h1 class="text-xl font-semibold text-veryDarkBlue">Create your account</h1>
      <p class="text-sm text-darkGrayishBlue mt-1 mb-6">Save listings and write reviews.</p>

      <form @submit.prevent="submitSignUp" class="text-left">
        <div class="mb-4">
          <label for="username" class="field-label">Username</label>
          <input type="text" id="username" v-model="username" pattern="^[a-zA-Z]+(( )+[a-zA-z]+)*$" class="field-input" required>
        </div>
        <div class="mb-4">
          <label for="email" class="field-label">Email address</label>
          <input type="email" id="email" name="email" v-model="email"
            pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$" class="field-input" required>
        </div>
        <div class="mb-2">
          <label for="pwd" class="field-label">Password</label>
          <input type="password" id="pwd" name="pwd" v-model="password"
            pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}"
            title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters"
            class="field-input" required>
        </div>
        <p v-if="error" class="text-sm text-red-600 mt-2">{{ error }}</p>
        <button type="submit" id="submit" name="signup_btn" :disabled="submitting" class="btn-solid btn-lg btn-block mt-5">Sign up</button>
      </form>

      <p class="text-sm text-darkGrayishBlue mt-5">
        Already have an account? <router-link to="/login" class="text-brightRed font-semibold no-underline">Log in</router-link>
      </p>
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue';
import { auth } from '../firebase';
import { createUserWithEmailAndPassword, updateProfile } from 'firebase/auth';
import store from '../store';

export default defineComponent({
  data(){
    return {
      username: '',
      password: '',
      email: '',
      error: '',
      submitting: false,
    }
  },
  methods: {
    async submitSignUp() {
      this.error = '';
      this.submitting = true;
      try {
        const credential = await createUserWithEmailAndPassword(auth, this.email, this.password);
        await updateProfile(credential.user, { displayName: this.username });
        // updateProfile doesn't reliably re-fire onAuthStateChanged right away,
        // so push the updated user into the store directly to avoid a flash of
        // the email before the display name catches up.
        store.dispatch('setUser', credential.user);
        this.$router.push('/');
      } catch (e: any) {
        this.error = e.message || 'Failed to sign up.';
      } finally {
        this.submitting = false;
      }
    }
  }
})
</script>
