<template> 
  <div class="signup-form" style="padding-top: 1%;">
    <div class="container-signup">
      <form class="form2" style="margin: auto; height: 30%;">
        <img class="logo-form" src="../assets/images/logo.png" width="200">

        <div class="group">
        <label for="username">Username:</label>
        <input type="text" v-model="username" pattern="^[a-zA-Z]+(( )+[a-zA-z]+)*$" required>
        </div>
        <div class="group">
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email"
          pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$">
        </div>
        <div class="group">
        <label for="password">Password:</label>
        <input type="password" id="pwd" name="pwd" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" 
          title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters">
        </div>
        <br>
        <div class="group">
          <button type="submit" id="submit" name="signup_btn" 
  class="btn btn-primary btn-user btn-block text-white bg-orange-700 hover:bg-orange-800 focus:ring-2 
        focus:outline-none focus:ring-orange-300 font-medium rounded-lg text-base px-3 my-1 text-center 
        dark:bg-orange-600 dark:hover:bg-orange-700 dark:focus:ring-orange-800"> Sign Up </button>
        </div>
      </form>
    </div> <!-- This is close of container -->
    <form class="form3" style="margin:auto; margin-top: 10px">
      <p style="text-align: center;">Already have account? <a href="#">Click here</a></p>
    </form>
  </div> 
</template>


<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data(){
    return {
      username: '',
      password: '',
      email: '',
    }
  }
})
</script>

<style>

label{
  display: block;
  margin: 20px 0 10px;
}
input {
  font-size: 25px;
  border: 2px double rgb(255 112 39);
  border-radius: 4px;
}
.form2 {
  display: center;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  padding: 20px;
  width: 500px;
  height: 600px;
  box-shadow: 0 0 10px rgba(173, 173, 173, 0.292);
  margin-bottom: 10px;
  }
.form3 {
  display: center;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  padding: 20px;
  width: 500px;
  box-shadow: 0 0 10px rgba(173, 173, 173, 0.292);
  }
.signup-form {
    padding-top: 1%;
    margin-top: 35px;
    position: absolute;
    display: center;
    align-items: center;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
.signup-form input {
  margin: 4px 0;
  width: 100%;
  max-width: 400px;
}
img {
    max-width: 100%;
    margin: auto;
  }
button {
  width: 100px;
  height: 40px;
}
.group {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
a {
  color: blue;
  text-decoration: underline;
}
a:hover {
  color: red;
}
</style>


