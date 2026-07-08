<!-- Reference: https://github.com/uiuc-apartments/uiuc-apartments.com -->
<script lang="ts">
import type { Article } from '../types'
import store from '../store'
export default {
  props: {
    source: {
      type: Object as () => Article,
      required: true,
    },
    highlightedApartment: {
      type: String as () => string | null,
      default: null,
    },
    deletable: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    isFavorited(): boolean {
      return store.getters.isFavorited(this.source)
    },
    isHighlighted(): boolean {
      return this.highlightedApartment !== null && this.highlightedApartment === this.source.apartment
    },
    listingTypeBadge(): { label: string, className: string } {
      if (this.source.listing_type === 'individual_landlord') {
        return { label: 'Individual Landlord', className: 'badge-landlord' }
      }
      if (this.source.listing_type === 'sublease') {
        return { label: 'Sublease', className: 'badge-sublease' }
      }
      return { label: 'Apartment Complex', className: 'badge-complex' }
    },
  },
  methods: {
    articleHover(article: Article) {
      this.$parent?.$parent?.$emit('article-hover', article)
    },
    toggleFavorite() {
      if (!store.getters.isLoggedIn) {
        alert('Please log in to save listings.')
        this.$router.push('/login')
        return
      }
      store.dispatch('toggleFavorite', this.source)
    },
  },
  emits: ['article-hover', 'delete'],
}
</script>
<template>
  <!-- apartment card with bedrooms bathrooms agency, rent, location with link to apartment using tailwind css -->

  <div
    class="listing-card"
    :class="{ 'is-highlighted': isHighlighted }"
    :key="source.link"
    :data-article-id="source.id"
    @mouseover="articleHover(source)"
    @mouseleave="articleHover({} as Article)"
  >
    <button
      v-if="deletable"
      type="button"
      class="favorite-btn delete-btn"
      aria-label="Delete listing"
      @click.stop="$emit('delete', source.id)"
    >
      <font-awesome-icon icon="trash" />
    </button>
    <button
      v-else
      type="button"
      class="favorite-btn"
      :class="{ 'is-favorited': isFavorited }"
      :aria-label="isFavorited ? 'Remove from saved listings' : 'Save listing'"
      @click.stop="toggleFavorite"
    >
      <font-awesome-icon icon="heart" />
    </button>
    <a
      :href="source.link"
      target="_blank"
      rel="noreferrer noopener"
      class="no-underline focus:outline-none"
    >
      <span class="listing-type-badge" :class="listingTypeBadge.className">
        {{ listingTypeBadge.label }}
      </span>
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
  @apply bg-white rounded-2xl border border-gray-200 shadow-sm px-5 py-4 transition-all duration-150 relative;
  width: 260px;
}
.listing-card:hover {
  @apply shadow-lg border-brightRedLight;
  transform: translateY(-3px);
}
.listing-card.is-highlighted {
  @apply shadow-lg border-brightRed;
  box-shadow: 0 0 0 3px rgba(244, 119, 78, 0.35), 0 8px 24px rgba(244, 119, 78, 0.18);
}
.favorite-btn {
  @apply absolute top-3 right-3 w-8 h-8 rounded-full bg-white shadow-sm border border-gray-200 flex items-center justify-center text-gray-300 transition-colors duration-150;
  z-index: 1;
}
.favorite-btn:hover {
  @apply text-brightRedLight;
}
.favorite-btn.is-favorited {
  @apply text-brightRed border-brightRedLight;
}
.delete-btn:hover {
  @apply text-brightRed border-brightRedLight;
}
.listing-type-badge {
  @apply block w-fit text-[10px] font-semibold uppercase tracking-wide rounded-full px-2.5 py-1 mb-1.5;
}
.badge-landlord {
  @apply bg-shooniYellow/20 text-darkBlue;
}
.badge-sublease {
  @apply bg-brightRed/10 text-brightRed;
}
.badge-complex {
  @apply bg-gray-100 text-darkGrayishBlue;
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
