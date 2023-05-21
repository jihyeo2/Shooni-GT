<template>
  <br/>
  <br/>
  <div class="app">
    <div class="flex justify-center">
                <img src="../assets/images/hammer.gif" style="max-width: 25%; margin-top: 10px;">
    </div>
    <div class="flex justify-center text-brightRed" style="text-align:center;font-size:20px;font-weight:bold;font-family:avenir">This site is currently under construction</div>
    <div class="flex justify-center text-brightRed" style="text-align:center;font-size:20px;font-weight:bold;font-family:avenir">Come back in</div>
    <div class="center">
      <Countdown />
    </div>
  </div>
</template>

<script>
import Countdown from "../components/Countdown.vue";
export default {
  name: "CountdownTimer",
  components: {
    Countdown,
  },
};
</script>

<style>
.app {
  text-align: center;
}
.flex-container {
  display: flex;
  justify-content: center;
  margin-top: 100px;
}
.center {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10vh;
}
</style>