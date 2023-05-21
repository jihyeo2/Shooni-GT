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
    class="relative flex items-center space-x-3 rounded-lg border border-gray-300 bg-white px-6 py-5 shadow-sm focus-within:ring-2 focus-within:ring-indigo-500 focus-within:ring-offset-2 hover:border-gray-400"
    style="width: 300px; border: solid 2px orange;"
    :key="source.link"
    @mouseover="articleHover(source)"
    @mouseleave="articleHover({} as Article)"
  >
    <div class="min-w-0 flex-1">
      <a
        :href="source.link"
        target="_blank"
        rel="noreferrer noopener"
        class="focus:outline-none no-underline"
      >
        <span class="font-bold text-gray-900 no-underline">
          <font-awesome-icon icon="dollar-sign" />
          {{ source.rent }} 
        </span>
        <p class="text-sm font-medium text-gray-900 no-underline">{{ source.apartment }}</p>
        <div class="truncate text-sm text-gray-500 no-underline">
          {{ source.address }}
          <div v-if="source.is_studio">
            <font-awesome-icon icon="bed" /> Studio
          </div>
          <div v-else>
            <font-awesome-icon icon="bed" /> {{ source.bedrooms }}
            <font-awesome-icon icon="bath" /> {{ source.bathrooms }}
          </div>
          Available: {{ source.available_date }} <br />
        </div>
      </a>
    </div>
  </div>
</template>
