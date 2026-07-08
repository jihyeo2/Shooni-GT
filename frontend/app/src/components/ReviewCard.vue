<template>
  <div class="review-item">
    <div class="flex items-center justify-between">
      <span class="review-stars">
        <span v-for="n in 5" :key="n" class="star" :class="{ 'star-filled': n <= review.rating }">&#9733;</span>
      </span>
      <div class="flex items-center gap-3">
        <span class="review-date">{{ formatDate(review.created) }}</span>
        <button v-if="deletable" type="button" class="review-delete-btn" aria-label="Delete review" @click="$emit('delete', review.id)">
          <font-awesome-icon icon="trash" />
        </button>
      </div>
    </div>
    <h3 class="review-title">{{ review.title }}</h3>
    <p class="review-comment">{{ review.comment }}</p>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    review: {
      type: Object as () => { id: string, title: string, comment: string, rating: number, created: string },
      required: true,
    },
    deletable: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['delete'],
  methods: {
    formatDate(iso: string) {
      if (!iso) return '';
      return new Date(iso).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
    },
  },
});
</script>

<style scoped>
.review-item {
  @apply border border-gray-200 rounded-2xl p-5;
}
.review-stars {
  font-size: 0.9rem;
}
.star {
  color: #d8d8de;
}
.star-filled {
  color: #F4774E !important;
}
.review-date {
  @apply text-xs text-darkGrayishBlue;
}
.review-delete-btn {
  @apply text-gray-300 hover:text-brightRed transition-colors duration-150;
}
.review-title {
  @apply text-base font-semibold text-veryDarkBlue mt-2;
}
.review-comment {
  @apply text-sm text-darkGrayishBlue mt-1;
}
</style>
