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
  <section class="background-image1"></section>
    <div class = "center-window1" >
        <h1 class="centered-heading2 with-image">About us</h1>
    </div>
    <div class="content-wrapper" style="margin: 80px 0;">
      <div class="content">
        <div class="text">
          <h1>Our Mission</h1>
          <p>The search for housing is complicated for college students because they have little time and money but a lot of pressure to find housing near their schools and no centralized place to search for it. We aim to simplify the search process for college students to find desirable housing by creating that centralized location -- Shooni.
          </p>
        </div>
        <div class="image-b">
        <img src="/src/assets/images/yellow.png" alt="your image">
        </div>
        <div class="image">
          <img src="/src/assets/images/au2.jpg" alt="your image">
        </div>
      </div>
    </div>
    <div class="content-wrapper" style="margin: 120px 0;">
      <div class="content2">
        <div class="image2">
          <img src="/src/assets/images/au3.jpg" alt="your image">
        </div>
        <div class="text2">
          <h2>Our Values</h2>
          <p>
            We aim to develop a rating system, a roommate search system, and an interactive map on our website.
            We want to share subleasing opportunities for students in need of short-term housing; We want to establish a user-friendly forum for students to 
            find their perfect roommates; we want students to be excited to leave the nest.
            We believe our idea will provide a more efficient and effective experience for students.
          </p>
        </div>
    </div>
  </div>

  <section>

  </section>
  <Footer></Footer>
</template>














<style>


.with-image {
    background-image: url("/src/assets/images/bird1.png");
    background-repeat: no-repeat;
    background-position: right center;
    background-size: contain;
    padding-right: 70px; 
  }


.center-window1 {
  display: flex;
  justify-content: center;
  align-items: center;
}

.centered-heading2 {
  color: rgb(19, 19, 19);
  font-size: 3.5rem;
  font-weight: bold;
  text-align: center;
  margin-top: 15vh;
}

.content-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 50px 0;
  position: relative;

}
.image-b {
  width: 700px;
  float: left;
  top:45%;
  margin-right: 52%;
  position:absolute;
  z-index: -1;
  opacity: 0.7;
}

.content {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  width: 70%;
}

.text {
  flex: 1;
  padding-right: 170px;
}

.image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image img {
  max-width: 100%;
  height: auto;
}

.text h1 {
  color: rgb(19, 19, 19);
  font-size: 2rem;
  font-weight: bold;
  text-align: center;

}


.text p {
  font-size: 1.5rem;
  text-align: justify;
  margin-top: 25px;
}


.content2 {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  width: 70%;
}

.text2 {
  flex: 1;
  padding-left: 170px;
}

.image2 {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.image2 img {
  max-width: 100%;
  height: auto;
}

.text2 h2 {
  color: rgb(19, 19, 19);
  font-size: 2rem;
  font-weight: bold;
  text-align: center;

}


.text2 p {
  font-size: 1.5rem;
  text-align: justify;
  margin-top: 25px;
}

.background-image1 {
  background-image: url('/src/assets/images/aubg1.jpg');
  background-size: cover;
  background-position: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: -1;
  opacity: 0.6;
}



</style>





