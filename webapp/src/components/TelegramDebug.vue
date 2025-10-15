<template>
  <div class="telegram-debug p-4 bg-gray-800 rounded-lg text-white">
    <h3 class="text-lg font-bold mb-4">🔧 Telegram Debug Info</h3>
    
    <div class="space-y-3">
      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">📊 Telegram Store</h4>
        <div class="text-sm space-y-1">
          <div><strong>isInitialized:</strong> {{ telegramStore.isInitialized ? '✅' : '❌' }}</div>
          <div><strong>userId:</strong> {{ telegramStore.userId || 'не найден' }}</div>
          <div><strong>user:</strong> <pre class="text-xs">{{ JSON.stringify(telegramStore.user, null, 2) }}</pre></div>
        </div>
      </div>

      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">🌐 WebApp Data</h4>
        <div class="text-sm space-y-1">
          <div><strong>initData:</strong> {{ telegramStore.initData || 'пусто' }}</div>
          <div><strong>initDataUnsafe:</strong> <pre class="text-xs">{{ JSON.stringify(telegramStore.initDataUnsafe, null, 2) }}</pre></div>
        </div>
      </div>

      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">🔗 Реферальная ссылка</h4>
        <div class="text-sm space-y-1">
          <div><strong>Сгенерированная:</strong> {{ generatedLink }}</div>
          <div><strong>Из useReferral:</strong> {{ referralData.link || 'не сгенерирована' }}</div>
        </div>
      </div>

      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">🛠️ Различные источники ID</h4>
        <div class="text-sm space-y-1">
          <div><strong>telegramStore.userId:</strong> {{ telegramStore.userId || 'нет' }}</div>
          <div><strong>telegramStore.user?.id:</strong> {{ telegramStore.user?.id || 'нет' }}</div>
          <div><strong>telegramStore.initDataUnsafe?.user?.id:</strong> {{ telegramStore.initDataUnsafe?.user?.id || 'нет' }}</div>
          <div><strong>WebApp.initDataUnsafe?.user?.id:</strong> {{ webAppUserId }}</div>
          <div><strong>window.Telegram?.WebApp?.initDataUnsafe?.user?.id:</strong> {{ windowTelegramId }}</div>
        </div>
      </div>

      <div class="bg-green-700 p-3 rounded">
        <h4 class="font-semibold mb-2">✅ Итоговый выбранный ID</h4>
        <div class="text-lg font-mono">{{ finalTelegramId || 'НЕ НАЙДЕН' }}</div>
        <div class="text-sm mt-1">Ссылка: {{ finalLink }}</div>
      </div>
    </div>

    <div class="mt-4 flex gap-2">
      <button 
        @click="refreshData"
        class="px-3 py-1 bg-blue-600 hover:bg-blue-700 rounded text-sm"
      >
        🔄 Обновить
      </button>
      
      <button 
        @click="initializeTelegram"
        class="px-3 py-1 bg-green-600 hover:bg-green-700 rounded text-sm"
      >
        🚀 Инициализировать Telegram
      </button>
      
      <button 
        @click="copyDebugInfo"
        class="px-3 py-1 bg-purple-600 hover:bg-purple-700 rounded text-sm"
      >
        📋 Копировать Debug Info
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useTelegramStore } from '../stores/telegram.js'
import { useReferral } from '../composables/useReferral.js'
import WebApp from '@twa-dev/sdk'

const telegramStore = useTelegramStore()
const { referralData, generateReferralLinkLocal } = useReferral()

// Реактивные данные для отладки
const webAppUserId = ref(null)
const windowTelegramId = ref(null)

// Вычисляемые свойства
const finalTelegramId = computed(() => {
  return telegramStore.userId || 
         telegramStore.user?.id || 
         telegramStore.initDataUnsafe?.user?.id ||
         webAppUserId.value ||
         windowTelegramId.value ||
         null
})

const generatedLink = computed(() => {
  if (finalTelegramId.value) {
    return generateReferralLinkLocal(finalTelegramId.value)
  }
  return 'ID не найден'
})

const finalLink = computed(() => {
  return generatedLink.value !== 'ID не найден' ? generatedLink.value : 'https://t.me/RoyallAppBot?start=ref_UNKNOWN'
})

// Методы
const refreshData = () => {
  // Обновляем данные из различных источников
  try {
    webAppUserId.value = WebApp.initDataUnsafe?.user?.id || null
  } catch (e) {
    webAppUserId.value = 'ошибка: ' + e.message
  }

  try {
    windowTelegramId.value = window.Telegram?.WebApp?.initDataUnsafe?.user?.id || null
  } catch (e) {
    windowTelegramId.value = 'ошибка: ' + e.message
  }

  console.log('🔄 Debug data refreshed:', {
    telegramStore: telegramStore.userId,
    webApp: webAppUserId.value,
    window: windowTelegramId.value,
    final: finalTelegramId.value
  })
}

const initializeTelegram = () => {
  try {
    telegramStore.initialize()
    setTimeout(refreshData, 1000)
  } catch (e) {
    console.error('Ошибка инициализации Telegram:', e)
  }
}

const copyDebugInfo = async () => {
  const debugInfo = {
    telegramStore: {
      isInitialized: telegramStore.isInitialized,
      userId: telegramStore.userId,
      user: telegramStore.user,
      initData: telegramStore.initData,
      initDataUnsafe: telegramStore.initDataUnsafe
    },
    webApp: {
      userId: webAppUserId.value,
      raw: WebApp.initDataUnsafe
    },
    window: {
      telegramId: windowTelegramId.value,
      available: !!window.Telegram
    },
    final: {
      telegramId: finalTelegramId.value,
      link: finalLink.value
    }
  }

  try {
    await navigator.clipboard.writeText(JSON.stringify(debugInfo, null, 2))
    alert('Debug info скопирована в буфер обмена!')
  } catch (e) {
    console.error('Ошибка копирования:', e)
    alert('Ошибка копирования')
  }
}

// Жизненный цикл
onMounted(() => {
  refreshData()
  
  // Обновляем данные каждые 2 секунды
  setInterval(refreshData, 2000)
})
</script>

<style scoped>
pre {
  max-height: 100px;
  overflow-y: auto;
  background: rgba(0,0,0,0.3);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-top: 0.25rem;
}
</style>







