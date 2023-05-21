<script module="es2015" lang="ts">
import NavBar from './components/NavBar.vue'

export default {
  components: {
    NavBar,
  }
}
</script>


<template>
  <NavBar/>
  <router-view />
</template>
