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

<style>
/* Глобальные шрифты TTCommons для всего приложения */
@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Regular-ClstCj-k.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Medium-DHgsE3TE.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TT Commons DemiBold-BR2O6jYH.otf') format('opentype');
  font-weight: 600;
  font-style: normal;
  font-display: swap;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Bold-DVcClD20.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}

/* Применяем шрифт ко всему приложению */
* {
  font-family: 'TTCommons', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

/* Основные стили приложения */
.app {
  background-color: #0b0c0d;
  min-height: 100vh;
  color: #ffffff;
  font-family: 'TTCommons', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
}

/* Дополнительная оптимизация для загрузки шрифтов */
body {
  font-family: 'TTCommons', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
