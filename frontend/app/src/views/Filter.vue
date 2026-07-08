<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  data() {
    return {
      steps: [
        { label: 'School', to: '/rent', icon: 'school.png' },
        { label: 'Price', to: '/filter', icon: 'price.png' },
        { label: 'Place', to: '/filter/1', icon: 'prox.png' },
        { label: 'Bed & Bath', to: '/filter/2', icon: 'bed.png' },
        { label: 'Finish', to: '/search', icon: 'finish.png' },
      ],
    }
  },
  computed: {
    activeIndex(): number {
      const path = this.$route.path
      if (path === '/filter/1') return 2
      if (path === '/filter/2') return 3
      if (path === '/filter' || path === '/filter/') return 1
      return 1
    },
  },
})
</script>

<template>
    <section class="pt-12 pb-6 px-6">
        <div class="max-w-2xl mx-auto flex items-start justify-between">
            <template v-for="(step, index) in steps" :key="step.label">
                <div class="flex flex-col items-center gap-2" style="width: 80px;">
                    <router-link :to="step.to" class="step-icon" :class="{ 'step-icon-active': index <= activeIndex }">
                        <img :src="`/images/${step.icon}`" class="h-5 w-5 object-contain">
                    </router-link>
                    <span class="step-label" :class="{ 'step-label-active': index <= activeIndex }">{{ step.label }}</span>
                </div>
                <div v-if="index < steps.length - 1" class="step-line" :class="{ 'step-line-active': index < activeIndex }"></div>
            </template>
        </div>
    </section>

    <router-view></router-view>
</template>

<style scoped>
.step-icon {
    @apply flex items-center justify-center h-11 w-11 rounded-full bg-gray-100 border-2 border-gray-200 transition-colors;
}
.step-icon-active {
    @apply bg-brightRedSupLight border-brightRed;
}
.step-label {
    @apply text-xs font-medium text-gray-400 text-center;
}
.step-label-active {
    @apply text-brightRed font-semibold;
}
.step-line {
    @apply flex-1 h-0.5 bg-gray-200 mt-5;
}
.step-line-active {
    @apply bg-brightRed;
}
</style>
