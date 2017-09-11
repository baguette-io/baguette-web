<template>
    <nav class="nav-pagination" aria-label="pagination">
        <ul class="pagination justify-content-center">
            <li class="page-item"  :class="{ disabled: !previous }">
                <a class="page-link"  @click="$emit('page-change', limit * (currentPage - 2), limit)"tabindex="-1">Previous</a>
            </li>
            <li class="page-item" v-for="page in pages" :class="{active: page === currentPage}" >
                <a class="page-link" href="#" @click="$emit('page-change', limit * (page - 1), limit)">{{ page }}</a>
            </li>
            <li class="page-item"  :class="{ disabled: !next }">
                <a class="page-link" @click="$emit('page-change', limit * (currentPage), limit)" tabindex="-1">Next</a>
            </li>
            
        </ul>
    </nav>
</template>

<script>
export default {
  props: ['limit', 'offset', 'total'],
  data: function () {
    return {
      currentPage: 1,
      totalPages: 1,
      pages: [],
      previous: false,
      next: false
    }
  },
  methods: {
    refreshPage: function () {
      let previous = true
      let next = true
      let currentPage = 1
      let totalPages = 1
      let pages = []

      /* offset */
      if (this.offset > 0) {
        currentPage = Math.ceil(this.offset / this.limit) + 1
      } else {
        previous = false
      }

      /* total pages */
      if (this.total > 0) {
        totalPages = Math.ceil(this.total / this.limit)
      }

      /* We display at most 5 number */
      if (currentPage - 2 > 0) {
        pages.push(currentPage - 2)
      }
      if (currentPage - 1 > 0) {
        pages.push(currentPage - 1)
      }
      pages.push(currentPage)
      if (currentPage + 1 <= totalPages) {
        pages.push(currentPage + 1)
      } else {
        next = false
      }
      if (currentPage + 2 <= totalPages) {
        pages.push(currentPage + 2)
      }

      this.currentPage = currentPage
      this.totalPages = totalPages
      this.pages = pages
      this.previous = previous
      this.next = next
    }
  },
  watch: {
    offset: function () {
      this.refreshPage()
    }
  },
  mounted: function () {
    this.refreshPage()
  }
}
</script>
