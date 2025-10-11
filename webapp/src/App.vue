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
    <router-view v-else />
  </div>
</template>

<style scoped>
.app {
  background-color: #0b0c0d;
  min-height: 100vh;
  color: #ffffff;
}
</style>
