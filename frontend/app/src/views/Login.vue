<template>
  <div class="min-h-[80vh] flex items-center justify-center bg-veryLightGray px-4 py-16">
    <div class="auth-card">
      <img src="../assets/images/logo.png" class="h-9 mx-auto mb-5" alt="Shooni">
      <h1 class="text-xl font-semibold text-veryDarkBlue">Log in</h1>
      <p class="text-sm text-darkGrayishBlue mt-1 mb-6">Welcome back — find your place.</p>

      <form @submit.prevent="submitLogin" class="text-left">
        <div class="mb-4">
          <label for="email" class="field-label">Email address</label>
          <input type="email" id="email" name="email" v-model="email" class="field-input" required>
        </div>
        <div class="mb-2">
          <label for="pwd" class="field-label">Password</label>
          <input type="password" id="pwd" name="pwd" v-model="password" class="field-input" required>
        </div>
        <p v-if="error" class="text-sm text-red-600 mt-2">{{ error }}</p>
        <button type="submit" :disabled="submitting" class="btn-solid btn-lg btn-block mt-5">Log in</button>
      </form>

      <p class="text-sm text-darkGrayishBlue mt-5">
        Don't have an account? <router-link to="/signup" class="text-brightRed font-semibold no-underline">Sign up</router-link>
      </p>
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent } from 'vue';
import { auth } from '../firebase';
import { signInWithEmailAndPassword } from 'firebase/auth';

export default defineComponent({
  data(){
    return {
      email: '',
      password: '',
      error: '',
      submitting: false,
    }
  },
  methods: {
    async submitLogin() {
      this.error = '';
      this.submitting = true;
      try {
        await signInWithEmailAndPassword(auth, this.email, this.password);
        this.$router.push('/');
      } catch (e: any) {
        this.error = e.message || 'Failed to log in.';
      } finally {
        this.submitting = false;
      }
    }
  }
})
</script>
