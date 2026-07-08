<script setup lang="ts">
import { computed } from 'vue'
import { useStore } from 'vuex'
import { signOut } from 'firebase/auth'
import { auth } from '../firebase'

const navigation = [
  { name: 'Rent', href: '/rent' },
  { name: 'Roommate', href: '/roommate' },
  { name: 'Community', href: '/community' },
  { name: 'Sublease', href: '/sublease' },
  { name: 'Reviews', href: '/review' },
  { name: 'About', href: '/about' },
]

const store = useStore()
const currentUser = computed(() => store.getters.currentUser)

function logout() {
  signOut(auth)
}
</script>

<template>
    <header>
        <nav class="fixed inset-x-0 top-0 z-20 h-16 bg-white border-b border-gray-200" aria-label="Top">
            <div class="h-full flex items-center justify-between px-6 sm:px-10">
                <router-link to="/" class="flex items-center">
                    <img src="../assets/images/logo.png" class="h-8 w-auto" alt="Shooni logo">
                </router-link>

                <div class="hidden md:flex items-center gap-8">
                    <template v-for="link in navigation" :key="link.href">
                        <a v-if="link.href.startsWith('http')" :href="link.href"
                            class="navlink no-underline text-sm font-medium text-veryDarkBlue/80 hover:text-brightRed transition-colors">
                            {{ link.name }}
                        </a>
                        <router-link v-else :to="link.href"
                            class="navlink no-underline text-sm font-medium text-veryDarkBlue/80 hover:text-brightRed transition-colors">
                            {{ link.name }}
                        </router-link>
                    </template>
                </div>

                <div class="flex items-center gap-3">
                    <template v-if="currentUser">
                        <router-link to="/dashboard" class="btn-ghost hidden sm:inline-flex items-center gap-2">
                            <font-awesome-icon icon="user" />
                            <span>{{ currentUser.displayName || currentUser.email }}</span>
                        </router-link>
                        <button type="button" @click="logout" class="btn-ghost">Log Out</button>
                    </template>
                    <template v-else>
                        <router-link to="/login" class="btn-ghost">Log In</router-link>
                        <router-link to="/signup" class="btn-solid">Sign Up</router-link>
                    </template>
                </div>
            </div>
        </nav>
    </header>
</template>

<style scoped>
.navlink.router-link-exact-active {
    @apply text-brightRed;
}
</style>
