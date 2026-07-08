<!-- Reference: https://github.com/uiuc-apartments/uiuc-apartments.com -->
<script module="es2015" lang="ts">
import { defineComponent, onMounted, type Ref, ref } from 'vue'
import type { Article, Filter } from '../types'
import VirtualList from 'vue3-virtual-scroll-list'
import ArticleCard from '../components/ArticleCard.vue'
import FilterBar from '../components/FilterBar.vue'
import SearchMap from '../components/SearchMap.vue'
import Footer from '../components/Footer.vue'



function getApartments(): Promise<Article[]> {
  return fetch(import.meta.env.VITE_DATA_ENDPOINT_URL)
    .then((response) => response.json())
    .then(data => Object.values(data))
    .then(data => {
      return data.map((value) => {
        var value_str = value as string
        var elem = JSON.parse(value_str)
        elem['listing_type'] = elem['listing_type'] || 'apartment_complex'
        return elem
      })})
}

function getSubleases(): Promise<Article[]> {
  return fetch(import.meta.env.VITE_GET_SUBLEASES_ENDPOINT_URL)
    .then((response) => response.json())
    .catch(() => [])
}

function getData(): Promise<Article[]> {
  // Two independent sources merged into one list: apartment/individual-landlord
  // listings from get-apartments, and user-submitted subleases from
  // get-subleases. `id` is assigned once across the merged array (not per
  // source) since VirtualList's data-key needs uniqueness across the whole
  // rendered list.
  return Promise.all([getApartments(), getSubleases()])
    .then(([apartments, subleases]) => [...apartments, ...subleases])
    .then(data => data.map((elem, index) => ({ ...elem, id: index })))
}

export default defineComponent({
  components: {
    ArticleCard,
    SearchMap,
    FilterBar,
    VirtualList,
    Footer,
  },
  computed: {
    apartments(): Array<string> {
      return [
        ...new Set(
          this.allArticles.map((article: Article) => article.apartment)
        )
      ]
    },
    filteredArticles(): Article[] {
      return this.allArticles.filter((article) => {
        return (
          article.bedrooms >= this.filter.minBedrooms &&
          article.bedrooms <= this.filter.maxBedrooms &&
          article.bathrooms >= this.filter.minBathrooms &&
          article.bathrooms <= this.filter.maxBathrooms &&
          article.rent >= this.filter.minRent &&
          article.rent <= this.filter.maxRent &&
          (this.filter.selectedApartments.length == 0 ||
            this.filter.selectedApartments.includes(article.apartment)) &&
          (this.filter.listingTypes.length == 0 ||
            this.filter.listingTypes.includes(article.listing_type || 'apartment_complex'))
        )
      })
    },
    mapArticles(): Article[] {
      // One marker per property, not per unit: units in the same complex
      // share coordinates, so their markers overlap and Google Maps' click
      // hit-testing resolves to whichever is topmost (in practice the last
      // one rendered) rather than a predictable article. Always bind each
      // marker to the first-occurring unit for that property so a marker
      // click scrolls to a deterministic card.
      const seen = new Set<string>()
      const result: Article[] = []
      for (const article of this.filteredArticles) {
        if (!seen.has(article.apartment)) {
          seen.add(article.apartment)
          result.push(article)
        }
      }
      return result
    }
  },
  setup() {
    const allArticles: Ref<Array<Article>> = ref([])
    const selectedArticle: Ref<Article> = ref({} as Article)
    const articleCard = ArticleCard
    const filter: Ref<Filter> = ref({} as Filter)
    const highlightedApartment: Ref<string | null> = ref(null)
    onMounted(async () => {
      getData().then((data) => {
        allArticles.value = data
      })
    })
    return {
      articleCard,
      selectedArticle,
      allArticles,
      filter,
      highlightedApartment,
    }
  },
  data() {
    return {
      highlightTimeout: null as ReturnType<typeof setTimeout> | null,
    }
  },
  methods: {
    onArticleHover(article: Article) {
      this.selectedArticle = article
    },
    onMarkerClick(article: Article) {
      // Deliberately not using VirtualList's own scrollToIndex: its last-item
      // case delegates to scrollToBottom(), which retries on a timer and can
      // spin indefinitely, permanently overriding any later scroll attempt.
      // Scrolling the actual card into view sidesteps that bug entirely.
      const card = document.querySelector(`[data-article-id="${article.id}"]`) as HTMLElement | null
      card?.scrollIntoView({ behavior: 'smooth', inline: 'start', block: 'nearest' })

      // scrollIntoView is a no-op when the whole list already fits on screen,
      // which leaves no visual cue for which card(s) the clicked marker
      // corresponds to -- flash a highlight on every card for that property
      // (not just the single unit the marker is bound to) so it's obvious
      // even when nothing scrolls.
      if (this.highlightTimeout) {
        clearTimeout(this.highlightTimeout)
      }
      this.highlightedApartment = article.apartment
      this.highlightTimeout = setTimeout(() => {
        this.highlightedApartment = null
      }, 2200)
    }
  }
})
</script>

<template>
  <main class="max-w-6xl mx-auto px-4 py-6 flex flex-col gap-6">
      <div class="flex justify-end">
        <router-link to="/sublease/new" class="btn-solid">Post a Sublease</router-link>
      </div>

      <FilterBar
        v-bind:apartments="apartments"
        v-model:filter-apartments="filter"
      ></FilterBar>

      <SearchMap
        v-bind:articles="mapArticles"
        @marker-click="onMarkerClick"
      ></SearchMap>

      <VirtualList
      class="list-horizontal"
      :data-key="'id'"
      :data-sources="filteredArticles"
      :data-component="articleCard"
      :extra-props="{ highlightedApartment }"
      :estimate-size="90"
      :wrap-class="'wrapper'"
      :item-class="'list-item-horizontal'"
      :direction="'horizontal'"
      @article-hover="onArticleHover"
      />
    </main>

  <Footer></Footer>
</template>

<style>
.list-horizontal {
  width: 100%;
  min-width: 0;
  overflow-x: auto;
}

.list-horizontal .wrapper {
  display: flex;
  flex-direction: row;
}

.list-item-horizontal {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  margin: 0 10px;
}

.list-item-horizontal .title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.list-item-horizontal .description {
  font-size: 14px;
}


</style>