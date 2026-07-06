<template>
  <div class="min-h-[70vh] flex flex-col items-center justify-center text-center px-5">
    <img src="../assets/images/hammer.gif" class="max-w-[220px]">
    <h1 class="text-xl font-semibold text-brightRed mt-4">This page is currently under construction</h1>
    <p class="text-darkGrayishBlue mt-1">Come back in</p>
    <div class="mt-6">
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