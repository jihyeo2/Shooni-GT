<script setup lang="ts">
const navigation = [
  { name: 'Rent', href: '/rent' },
  { name: 'Roommate', href: '/roommate' },
  { name: 'Community', href: "https://sites.gatech.edu/shooni/" },
  { name: 'About', href: '/about' },
]
</script>

<template>
    <header>
        <nav class="bg-white px-2 sm:px-4 py-2.5 dark:bg-white-900 fixed w-full z-20 top-0 left-0 right-0 border-b border-gray-200 dark:border-gray-300" aria-label="Top">
            <div class="flex justify-between">
                <router-link to="/" class="items-center content-center md:order-first ml-1 mt-1" >
                    <img src="../assets/images/logo.png" class="h-6 sm:h-9" alt="Flowbite Logo">
                </router-link>
                <div class="flex md:order-last">
                    <div class="flex flex-col px-7 py-3 mt-4 md:flex-row md:space-x-8 px-5 md:mt-0 md:text-base md:font-medium md:border-0 md:bg-white">
                        <router-link v-for="link in navigation" :to="link.href" class="block no-underline py-2 pl-3 pr-4 text-gray-700 rounded hover:bg-orange-600 md:hover:bg-transparent md:hover:text-orange-700 md:p-0 md:dark:hover:text-orange-600 dark:text-gray-400 dark:hover:bg-orange-600 dark:hover:text-orange-600 md:dark:hover:bg-transparent dark:border-gray-700">
                            {{ link.name }}
                        </router-link>
                    </div>

                    <button type="button" class="text-white bg-orange-700 hover:bg-orange-800 focus:ring-2 
                        focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-base px-3 my-1 text-center 
                        dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800"
                       ><router-link to="/signup" class="no-underline text-white">Sign Up</router-link></button>
                </div>
            </div>
        </nav>
    </header>
</template>

<style>
.router-link-exact-active{
    color:black
}
</style>


