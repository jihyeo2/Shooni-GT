<script lang="ts">
import Footer from '../components/Footer.vue'
import { defineComponent } from 'vue';

export default defineComponent({
  components: {
    Footer,
  },
})
</script>

<template>
    <br/>
    <br/>
    <section class="overflow-hidden bg-image-home justify-end">
        <!-- <div class="relative overflow-hidden bg-no-repeat bg-center" style="background-image: url('../assets/images/bg.png'); height: 700px;"> -->
        <!-- <div class="absolute top-0 right-0 bottom-0 left-0 w-full h-full overflow-hidden bg-fixed" style="background-color: rgba(0, 0, 0, 0.75);"> -->
            <div class = "center-window-home" style="height: 500px;">
                <div>
                    <h1 class="heading-home1">Leave the nest.</h1>
                    <h1 class="heading-home2">Find your new home</h1>
                    <h1 class="heading-home2">with us!</h1>
                    <h6 class="heading-home4">Been there. Done that, we got this.</h6>
                </div>
                <div style="display: flex; justify-content: center;">
                    <div class = 'w-fit'>
                        <div class = "button-up w-full px-5 py-2 content-center items-center text-black"> 
                            <router-link to="/rent" class="no-underline">
                                <label style="margin: center;">> I am a renter</label>
                            </router-link>
                        </div>
                        <div class = "button-down w-full px-5 py-2 content-center items-center"> 
                            <label>> I am a homeowner</label>
                        </div>
                    </div>
                    <div>
                          <img src="../assets/images/bird1.png" style="width: 300px"/>
                    </div>
                </div>
            </div>

    </section>
    
    <div class="line1"></div>
    
    <section class = "mid-info my-10 justify-center">
        <div class="mt-20">
            <img src="../assets/images/logo.png" class="h-40"/>
            <label class="text-2xl text-center" style="margin-bottom: -15px">Renting is time consuming.</label>
            <label class="text-2xl text-center mt-5">We are here to help you narrow down options, save your time and money, and find you the best appropriate residences.  </label>
        </div>

        <div class="grid-container1">
            <div class="grid-item1">
                <h1 style="font-weight: bold; text-align: center;">Explore different housing options</h1>
                <h2>Many housing resources for you to choose from fancy luxuary apartments to nearby convenient campus dorms.
                    Help you connect with real estate agents to get everything start ealier and answer your questions. 
                </h2>
            </div>
            <div class="grid-item2">
                <img src="../assets/images/gg.jpg" alt="grid-item2-Image">
            </div>
            <div class="grid-item3">
                <img src="../assets/images/emm.jpg" alt="grid-item3-Image">
            </div>
            <div class="grid-item4">
                <h1 style="font-weight: bold; text-align: center;">Visit different housing designs</h1>
                <h2>Thousands of characteristic interior designs and room features. Classical, modern, fantastic views, you can find all your preferences here</h2>
            </div>
            <div class="grid-item5">
                <h1 style="font-weight: bold; text-align: center;">Compare on and off campus housing</h1>
                <h2>You are able to compare both on-campus housing and off-campus housing toghther. Enjoy your college life while saving renting fees as well as making new friends</h2>
            </div>
            <div class="grid-item6">
                <img src="../assets/images/sss.png" alt="grid-item6-Image">
            </div>
        </div>
    </section>

    <section class="middle-image my-10 w-full px-20">
        <div class="grid-container">
            <div class="grid-1home">
            <h1 class="middle-context">Shooni Remembers YOU!</h1>
            <h2 class="middle-context2">Sign in to save your progress, get recommendations, and more!</h2>
            </div>

            <div class="grid-2home">
                <img src="../assets/images/bg1.png" class="w-full" />
            </div>
        </div>

    </section>


<div class="container-fluid h-100 my-10">
    <div class="row h-100">
        <div class="col-md-6 mx-auto my-auto container-center">
            <div class="form-container">
                <h2 class="text-2xl font-bold mb-8">Contact Us</h2>
                <form>
                    <div class="form-group pb-8">
                        <label for="name">Name:</label>
                        <input type="text" class="form-control" id="name" placeholder="Enter your name">
                    </div>
                    <div class="form-group pb-8">
                        <label for="email">Email address:</label>
                        <input type="email" class="form-control" id="email" placeholder="Enter your email">
                    </div>
                    <div class="form-group pb-8">
                        <label for="message">Message:</label>
                        <textarea class="form-control" id="message" rows="5" placeholder="Enter your message"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary btn-lg">Submit</button>
                </form>
            </div>
        </div>
    </div>
</div>
<Footer></Footer>
</template>



 

<style>
.bg-image-home{
    background-image: url("/src/assets/images/bg.png");
    height: 100vh;
    background-position: center;
    background-size: cover;
    overflow:hidden;
    position: relative;
}
/* 
.center-window-home{
    width: 50%;
    height: 60%;
    background-color: #f4d0a6;
    z-index: 10;
    margin: 0 auto;
    border-radius: 30px;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    text-align: left;
    padding: 8% 0;
}

.heading-home1 {
  font-size: 70px;
  line-height: 1.2;
  text-align: center;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-right: 60px;
  font-weight: lighter;
  margin-top: -10%;
}

.heading-home2 {
  font-size: 70px;
  line-height: 1.2;
  text-align: center;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-right: 30px;
  font-weight: lighter;
}

.heading-home4 {
  font-size: 21px;
  line-height: 1.2;
  text-align: center;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-top: 2%;
}


.button-up {
    background-color:rgb(255, 133, 89);
    border-width: 0px;
    border-radius: 10px;
    width: fit-content;
    height: fit-content;
    font-size: 20px;
    font-weight: 400;
    font-family:'Inria Serif', serif;
  }
.button-down {
    color: black;
    width: fit-content;
    border-radius: 10px;
    text-align: center;
    border: solid black;
    font-size: 20px;
    margin-left: 40px;
    font-weight: 400;
    margin-top: 10%;
    font-family:'Inria Serif', serif;
  } */

  .center-window-home{
    width: fit-content;
    height: fit-content;
    background-color: #f4d0a6;
    z-index: 10;
    margin: 0 auto;
    border-radius: 30px;
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    text-align: left;
    padding: 6% 0;
    margin-left: 10%;
}
.heading-home1 {
  font-size: 70px;
  line-height: 1.2;
  text-align: left;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-right: 60px;
  font-weight: lighter;
  margin-top: -10%;
}

.heading-home2 {
  font-size: 70px;
  line-height: 1.2;
  text-align: left;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-right: 30px;
  font-weight: lighter;
}

.heading-home4 {
  font-size: 21px;
  line-height: 1.2;
  text-align: left;
  color: black;
  font-family: 'Inria Serif', serif;
  margin-left: 40px;
  margin-top: 2%;
}
.button-up {
    color: black;
    height: fit-content;
    border-radius: 10px;
    text-align: center;
    border: solid black;
    font-size: 20px;
    margin-left: 40px;
    font-weight: bold;
    margin-top: 10%;
    font-family:'Inria Serif', serif;
  }
.button-down {
    color: black;
    height: fit-content;
    border-radius: 10px;
    text-align: center;
    border: solid black;
    font-size: 20px;
    margin-left: 40px;
    font-weight: bold;
    margin-top: 10%;
    font-family:'Inria Serif', serif;
  }

img {
    max-width: 100%;
    height: auto;
}

h1 {
    font-size: 10px;
}


.grid1 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 20px;
}

@media only screen and (max-width: 1024px) {
    .center-window-home {
        width: 60%;
        margin-left: 20%;
    }
}

@media only screen and (max-width: 768px) {
    .center-window-home {
        width: 80%;
        margin: 0 auto;
    }
}
    .heading-home1,
    .heading-home2 {
        font-size: 2.5rem;
        font-weight: bold;
    }



@media only screen and (max-width: 768px) {
  .button-up,
  .button-down {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    size: 20px;
  }
}



.mid-info h1{
    padding-top: 120px;
    text-align: center;
    font-size: 4em;
}

.mid-info h2{
    padding-top: 30px;
    text-align: center;
    font-size: 2em;
    margin-left: 10%;
    margin-right: 10%;
}

.grid-container1 {
    padding-top: 30px;
	display: grid;
	grid-template-columns: repeat(2, 1fr);
	grid-template-rows: repeat(3, auto);
	grid-gap: 0;
}

.grid-item2 img, .grid-item3 img, .grid-item6 img {
        width: 100%;
        height: 100%;
    }

.grid-item1 h1 {
	
	padding: 10%;
    margin-top: 5%;
    font-size: 2.5em;
    height: 30%;
    margin-left: 10%;
    text-align: center;
    
}

.grid-item1 h2 {
	
	padding: 5%;
    font-size: 1.7em;
    margin-left: 10%;
    text-align: center;
    margin-right: 5%;
}

.grid-item2 {
	
    width: 80%;
    height: auto;
    object-fit: cover;
}


.grid-item3 {
	
    width: 80%;
    height: auto;
    margin-left: 20%;
    object-fit: cover;
}

.grid-item4 h1 {
	
	padding: 10%;
    margin-top: 5%;
    font-size: 2.5em;
    height: 30%;
    margin-left: 10%;
    text-align: center;
    
}

.grid-item4 h2 {
	
	padding: 5%;
    font-size: 1.7em;
    margin-left: 10%;
    text-align: center;

}


.grid-item5 h1 {
	
	padding: 10%;
    margin-top: 5%;
    font-size: 2.5em;
    height: 30%;
    margin-left: 10%;
    text-align: center;
    
}

.grid-item5 h2 {
	
	padding: 5%;
    font-size: 1.7em;
    margin-left: 10%;
    text-align: center;
    margin-right: 5%;
}


.grid-item6 {
	
    width: 80%;
    height: auto;
    object-fit: cover;
}

.grid-item1,.grid-item5 {
  background-color: #f2f2f2;
  border-radius: 10px;
  color: rgb(0, 0, 0);
  margin-left:20%;
}

.grid-item4{
  background-color: #f2f2f2;
  color: rgb(0, 0, 0);
  margin-right:20%;;
}




  
  .grid-1home {
    display: inline-block;
    width: 50%; 
    vertical-align: top; 
  }
  
  .grid-2home {
    display: inline-block;
    width: 50%; 
    vertical-align: top; 
  }



  .middle-image{
    padding-top: 150px; 
    padding-bottom: 120px; 
    background-color: #e6e6e6;
  }


  .middle-context{
    text-align: center;
    margin-top: 20%;
    font-size: 38px;
    margin-left: 40px;
    font-weight: 600;
    color:#E1814B;
    padding-right: 10%;
  }


  .middle-context2{
    text-align: center;
    font-size: 26px;
    margin-left: 40px;
    color:#8b3604;
    font-weight: 500;
    padding-right: 10%;
  }

/* .container {
  max-width: 2140px;
  margin: 0 auto;
  justify-content: center;
  align-items: center;
  
} */

.form-group label {
  display: block;
}

.form-control {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 8px;
  width: 100%;
  box-sizing: border-box;
}

/* .container-center {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
} */

.form-container {
    max-width: 2140px;
    padding: 40px;
    background-color: #f5f5f5;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.btn-primary {
  background-color: rgb(219, 116, 20);
  color: #fff;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  
}


.row {
  display: flex;
}

.col-md-6 {
  flex: 0 0 50%;
  max-width: 50%;
  padding: 0 15px;
  box-sizing: border-box;
}

.line1 {
  height: 1px;
  width: 100%;
  background-color: rgb(152, 149, 149);
  position: absolute;
  z-index: 1;
  margin-bottom: 3%;
}


.line2 {
  height: 3px;
  width: 100%;
  background-color: rgb(152, 149, 149);
  margin-top: 5%;
  position: relative;
  z-index: 1;
}

.line3 {
  height: 3px;
  width: 100%;
  background-color: rgb(152, 149, 149);
  position: relative;
  z-index: 1;
}


.orange-background {
  border-top: 2px solid black;
}

button.btn-primary {
  width: 120px;
                 /* Change the value to your desired width */
}



@media only screen and (max-width: 767px) {
  .grid-container {
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    grid-gap: 10px;
  }
}



input::placeholder {
  font-size: 18px;
}

/* make the message placeholder larger */
textarea::placeholder {
  font-size: 18px;
}

</style>
