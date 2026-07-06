<!-- Reference: https://github.com/uiuc-apartments/uiuc-apartments.com -->
<script module="es2015" lang="ts">
import { defineComponent, onMounted, type Ref, ref } from 'vue'
import type { Article, Filter } from '../types'
import VirtualList from 'vue3-virtual-scroll-list'
import ArticleCard from '../components/ArticleCard.vue'
import FilterBar from '../components/FilterBar.vue'
import SearchMap from '../components/SearchMap.vue'
import Footer from '../components/Footer.vue'



function getData(): Promise<Article[]> {
  return fetch(import.meta.env.VITE_DATA_ENDPOINT_URL)
    .then((response) => response.json())
    .then(data => Object.values(data))
    .then(data => {
      return data.map((value, index) => {
        var value_str = value as string
        var elem = JSON.parse(value_str)
        elem['id'] = index
        return elem
      })})
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
            this.filter.selectedApartments.includes(article.apartment))
        )
      })
    }
  },
  setup() {
    const allArticles: Ref<Array<Article>> = ref([])
    const selectedArticle: Ref<Article> = ref({} as Article)
    const articleCard = ArticleCard
    const filter: Ref<Filter> = ref({} as Filter)
    onMounted(async () => {
      getData().then((data) => {
        allArticles.value = data
      })
    })
    return {
      articleCard,
      selectedArticle,
      allArticles,
      filter
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
    }
  }
})
</script>

<template>
  <main class="max-w-6xl mx-auto px-4 py-6 flex flex-col gap-6">
      <FilterBar
        v-bind:apartments="apartments"
        v-model:filter-apartments="filter"
      ></FilterBar>

      <SearchMap
        v-bind:articles="filteredArticles"
        @marker-click="onMarkerClick"
      ></SearchMap>

      <VirtualList
      class="list-horizontal"
      :data-key="'id'"
      :data-sources="filteredArticles"
      :data-component="articleCard"
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