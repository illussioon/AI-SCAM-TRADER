<script setup>
import { ref, onMounted } from 'vue'
import LoadingVue from './loading.vue'

const isLoading = ref(true)

onMounted(() => {
  // Показываем loading при каждом обновлении страницы
  setTimeout(() => {
    isLoading.value = false
  }, 3000) // 3 секунды загрузки
})
</script>

<template>
  <div class="app">
    <LoadingVue v-if="isLoading" />
    <div v-else class="main-content">
      <h1>You did it!</h1>
      <p>
        Visit <a class="" href="https://vuejs.org/" target="_blank" rel="noopener">vuejs.org</a> to read the
        documentation
      </p>
    </div>
  </div>
</template>

<style scoped>
.app {
  background-color: #0b0c0d;
  min-height: 100vh;
  color: #ffffff;
}

.main-content {
  padding: 2rem;
}

.main-content a {
  color: #4ade80;
  text-decoration: none;
}

.main-content a:hover {
  text-decoration: underline;
}
</style>
