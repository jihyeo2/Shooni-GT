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
    <section class="overflow-hidden bg-image">
            <div class = "center-window" >
                <h1 class="centered-heading">Let's build the perfect home for you!</h1>
                <!-- Will use again when we can serve multiple schools -->
                <!-- <h2 class="centered-text">Type in your school name below and Shooni will start building!</h2>
                <div class="search-bar flex items-center justify-center">
                    <input type="text" class="inline-block w-5/12 px-28 py-3 mr-14 pl-[30px] pr-[30px] border-2 border-white bg-white text-black font-medium text-md leading-snug uppercase rounded-2xl shadow-md focus:outline-none focus:ring-0 transition duration-150 ease-in-out" placeholder="Example: Georgia Institute of Technology" style="font-size: 1.5em">
                    <div class="inline-block px-5 w-1/8 py-3 border-2 text-orange-800 border-transparent bg-white font-medium text-2xl leading-snug uppercase rounded-2xl focus:outline-none focus:ring-0 transition duration-150 ease-in-out font-weight: 900" data-mdb-ripple="true" data-mdb-ripple-color="light" style="font-size: 1.5em; position: relative; display: flex; justify-content: center; align-items: center; cursor: pointer;">
                        <router-link to="/filter" class="no-underline">ENTER</router-link>
                    </div>
                </div> -->
                <h3 class="centered-text">Currently available for: Georgia Institute of Technology</h3>
                <div class="search-bar flex items-center justify-center">
                    <div class="inline-block px-5 w-1/8 py-3 border-2 text-black hover:text-orange-800 border-transparent bg-white font-medium text-xl leading-snug rounded-2xl focus:outline-none focus:ring-0 transition duration-150 ease-in-out font-weight: 900">
                        <router-link to="/filter" class="no-underline text-black">Start your search</router-link>
                    </div>
                </div>
            </div>
    </section>

        <section class="mb-32 text-gray-800 text-center">
            <div class="container my-24 px-6 mx-auto">
            <div class="grid lg:grid-cols-3 gap-6 xl:gap-x-12">
                <div class="mb-6 lg:mb-0">
                <div class="relative block bg-white rounded-lg shadow-lg">
                    <div class="flex">
                    <div
                        class="relative overflow-hidden bg-no-repeat bg-cover relative overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
                        data-mdb-ripple="true" data-mdb-ripple-color="light">
                        <img src="../assets/images/bg11.png" class="w-fit" />
                        <a href="#!">
                        <div
                            class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
                            style="background-color: rgba(251, 251, 251, 0.15)"></div>
                        </a>
                    </div>
                    </div>
                    <div class="p-6">
                    <h5 class="font-bold text-lg mb-3 text-orange-600" style=" font-size:130%;" >Find your Roomies</h5>
                   
                    <p class="mb-4 pb-2">
                        Search your area and find the perfect roomate(s) for you!
                    </p>
                    <a data-mdb-ripple="true" data-mdb-ripple-color="light"
                        class="inline-block px-6 py-2.5 font-weight: 900 bg-orange-500 text-white font-medium text-ls leading-tight uppercase rounded-full shadow-md hover:bg-orange-600 hover:shadow-lg focus:bg-orange-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-orange-600 active:shadow-lg transition duration-150 ease-in-out opacity-85"><router-link to="/roommate" class="no-underline text-white">Finder</router-link>
                        </a>
                    </div>
                </div>
                </div>

                <div class="mb-6 lg:mb-0">
                <div class="relative block bg-white rounded-lg shadow-lg">
                    <div class="flex">
                    <div
                        class="relative overflow-hidden bg-no-repeat bg-cover relative overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
                        data-mdb-ripple="true" data-mdb-ripple-color="light">
                        <img src="../assets/images/bg22.png" class="w-full" />
                        <a href="#!">
                        <div
                            class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
                            style="background-color: rgba(251, 251, 251, 0.15)"></div>
                        </a>
                    </div>
                    </div>
                    <div class="p-6">
                    <h5 class="font-bold text-lg mb-3 text-orange-600 " style="; font-size:130%;" >Join the Community</h5>
        
                    <p class="mb-4 pb-2">
                        Chat with other students and explore the marketplace!
                    </p>
                    <a href="https://sites.gatech.edu/shooni/" data-mdb-ripple="true" data-mdb-ripple-color="light"
                        class="inline-block px-6 py-2.5 bg-orange-500 font-weight: 900 text-white font-medium text-ls leading-tight uppercase rounded-full shadow-md hover:bg-orange-600 hover:shadow-lg focus:bg-orange-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-orange-600 active:shadow-lg transition duration-150 ease-in-out opacity-85">Join
                    </a>
                    </div>
                </div>
                </div>

                <div class="mb-0">
                <div class="relative block bg-white rounded-lg shadow-lg">
                    <div class="flex">
                    <div
                        class="relative overflow-hidden bg-no-repeat bg-cover relative overflow-hidden bg-no-repeat bg-cover shadow-lg rounded-lg mx-4 -mt-4"
                        data-mdb-ripple="true" data-mdb-ripple-color="light">
                        <img src="../assets/images/bg33.png" class="w-full" />
                        <a href="#!">
                        <div
                            class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed opacity-0 hover:opacity-100 transition duration-300 ease-in-out"
                            style="background-color: rgba(251, 251, 251, 0.15)"></div>
                        </a>
                    </div>
                    </div>
                    <div class="p-6">
                    <h5 class="font-bold text-lg mb-3 text-orange-600" style=" font-size:130%;" >Create an account</h5>
                  
                    <p class="mb-4 pb-2">
                        Sign up to receive all the benefits Shooni has to offer!
                    </p>
                    <a data-mdb-ripple="true" data-mdb-ripple-color="light"
                        class="inline-block px-6 py-2.5 bg-orange-500 font-weight: 900 text-white font-medium text-ls leading-tight uppercase rounded-full shadow-md hover:bg-orange-600 hover:shadow-lg focus:bg-orange-600 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-orange-600 active:shadow-lg transition duration-150 ease-in-out opacity-85"><router-link to="/signup" class="no-underline text-white">Create</router-link>
                        </a>
                    </div>
                </div>
                </div>
            </div>
        </div>
    </section>
    <Footer></Footer>
</template>

 



<style>
.centered-heading{
    font-size: 50px;
    text-align: center;
    padding-top: 13%;
    color: rgb(255, 255, 255);
    font-style: Bold;
    font-weight: 700;
}
.centered-text{
    font-size: 20px;
    text-align: center;
    color: white;
    font-style: bold;
    font-weight: 500;
    padding-top: 2%;
    overflow: hidden;
}
.info{
    padding-top: 20px;
    
}
.search-bar{
    text-align: center;
    padding-top: 3.5rem;
}
.search-bar input::placeholder {
    width: 100%;
    margin: 0px;
    text-align: center;
}

.bg-image{
    background-image: url("/src/assets/images/labg2.png");
    height: 85vh;
    background-position: center;
    background-size: cover;
}




</style>
