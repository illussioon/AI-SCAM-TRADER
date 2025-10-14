<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import LoadingVue from './loading.vue'
import { useTelegramStore } from './stores/telegram.js'
import { useUserStore } from './stores/user.js'

const isLoading = ref(true)

// Stores
const telegramStore = useTelegramStore()
const userStore = useUserStore()

onMounted(async () => {
  try {
    console.log('🚀 Инициализация приложения...')
    
    // 1. Инициализируем Telegram WebApp
    telegramStore.initialize()
    
    // 2. Небольшая задержка для стабилизации
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    // 3. Инициализируем пользовательские данные
    await userStore.initialize()
    
    // 4. Показываем загрузку еще минимум 2 секунды для плавности
    setTimeout(() => {
      isLoading.value = false
      console.log('✅ Приложение инициализировано')
    }, 2000)
    
  } catch (error) {
    console.error('❌ Ошибка инициализации приложения:', error)
    
    // В случае ошибки все равно скрываем загрузку через 3 секунды
    setTimeout(() => {
      isLoading.value = false
    }, 3000)
  }
})

onUnmounted(() => {
  // Очищаем ресурсы при размонтировании
  userStore.stopAutoUpdate()
  console.log('🧹 Ресурсы приложения очищены')
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
  
  /* Мобильная оптимизация */
  touch-action: manipulation; /* Отключает двойной тап для зума */
  -webkit-touch-callout: none; /* Отключает контекстное меню на iOS */
  -webkit-user-select: none; /* Отключает выделение текста на WebKit */
  -moz-user-select: none; /* Отключает выделение текста на Firefox */
  -ms-user-select: none; /* Отключает выделение текста на IE */
  user-select: none; /* Отключает выделение текста */
  -webkit-tap-highlight-color: transparent; /* Убирает подсветку при тапе на iOS */
  -webkit-overflow-scrolling: touch; /* Плавная прокрутка на iOS */
  overscroll-behavior: none; /* Предотвращает bouncing эффект */
}

/* Дополнительная оптимизация для загрузки шрифтов */
body {
  font-family: 'TTCommons', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  
  /* Мобильные оптимизации для body */
  margin: 0;
  padding: 0;
  overflow-x: hidden; /* Предотвращает горизонтальную прокрутку */
  position: fixed; /* Фиксирует body для предотвращения скролла */
  width: 100%;
  height: 100%;
  -webkit-text-size-adjust: 100%; /* Предотвращает автоматическое изменение размера текста на iOS */
  -ms-text-size-adjust: 100%; /* Предотвращает автоматическое изменение размера текста на Windows Phone */
}

/* Глобальные мобильные оптимизации */
html {
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;
  height: 100%;
  overflow: hidden;
}

/* Оптимизация для input и button элементов */
input, button, textarea, select {
  -webkit-user-select: text; /* Разрешаем выделение в полях ввода */
  user-select: text;
  -webkit-tap-highlight-color: transparent;
}

/* Разрешаем выделение там, где это нужно */
.selectable {
  -webkit-user-select: text !important;
  -moz-user-select: text !important;
  -ms-user-select: text !important;
  user-select: text !important;
}

/* Оптимизация прокрутки */
* {
  -webkit-overflow-scrolling: touch;
  box-sizing: border-box;
}

/* Предотвращение зума на iOS */
@media screen and (max-device-width: 480px) {
  html {
    -webkit-text-size-adjust: none;
  }
}
</style>
