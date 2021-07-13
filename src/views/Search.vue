<template>
  <div class="search">
    <Search placeholderValue="Find curator mails, social media &amp; websites" />
  </div>
</template>

<script>
import Search from '@/components/Search.vue'

export default {
  name: 'SearchView',
  components: {
    Search
  }
}
</script>
