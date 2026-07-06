<!-- Reference: https://github.com/uiuc-apartments/uiuc-apartments.com -->
<script lang="ts">
import type { Article } from '../types'
export default {
  props: {
    source: {
      type: Object as () => Article,
      required: true,
    },
  },
  methods: {
    articleHover(article: Article) {
      this.$parent?.$parent?.$emit('article-hover', article)
    },
  },
  emits: ['article-hover'],
}
</script>
<template>
  <!-- apartment card with bedrooms bathrooms agency, rent, location with link to apartment using tailwind css -->

  <div
    class="listing-card"
    :key="source.link"
    :data-article-id="source.id"
    @mouseover="articleHover(source)"
    @mouseleave="articleHover({} as Article)"
  >
    <a
      :href="source.link"
      target="_blank"
      rel="noreferrer noopener"
      class="no-underline focus:outline-none"
    >
      <span class="listing-rent">
        <font-awesome-icon icon="dollar-sign" />{{ source.rent }}
      </span>
      <p class="listing-apt">{{ source.apartment }}</p>
      <p class="listing-addr">{{ source.address }}</p>
      <div class="listing-meta">
        <span v-if="source.is_studio"><font-awesome-icon icon="bed" /> Studio</span>
        <span v-else><font-awesome-icon icon="bed" /> {{ source.bedrooms }}</span>
        <span v-if="!source.is_studio"><font-awesome-icon icon="bath" /> {{ source.bathrooms }}</span>
      </div>
      <span class="listing-avail">Available {{ source.available_date }}</span>
    </a>
  </div>
</template>

<style scoped>
.listing-card {
  @apply bg-white rounded-2xl border border-gray-200 shadow-sm px-5 py-4 transition-all duration-150;
  width: 260px;
}
.listing-card:hover {
  @apply shadow-lg border-brightRedLight;
  transform: translateY(-3px);
}
.listing-rent {
  @apply text-lg font-bold text-brightRed;
  font-variant-numeric: tabular-nums;
}
.listing-apt {
  @apply text-sm font-semibold text-veryDarkBlue mt-1.5 truncate;
}
.listing-addr {
  @apply text-xs text-darkGrayishBlue truncate;
}
.listing-meta {
  @apply flex gap-3 text-xs text-darkGrayishBlue mt-2;
}
.listing-avail {
  @apply inline-block mt-3 text-[11px] font-semibold text-darkBlue bg-darkBlue/10 rounded-full px-2.5 py-1;
}
</style>
