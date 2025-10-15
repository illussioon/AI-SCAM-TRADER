<template>
  <div class="user-data-demo p-4 bg-gray-800 rounded-lg">
    <h3 class="text-xl font-bold mb-4">🚀 User Store Demo</h3>
    
    <!-- Статус загрузки -->
    <div class="mb-4">
      <div class="flex items-center gap-2 mb-2">
        <div 
          :class="[
            'w-3 h-3 rounded-full',
            isLoading ? 'bg-yellow-500 animate-pulse' : 
            hasUserData ? 'bg-green-500' : 'bg-red-500'
          ]"
        ></div>
        <span class="text-sm font-medium">
          {{ isLoading ? 'Загрузка...' : hasUserData ? 'Данные загружены' : 'Ошибка загрузки' }}
        </span>
      </div>
      
      <div v-if="error" class="text-red-400 text-sm">
        ❌ {{ error }}
      </div>
    </div>

    <!-- Данные пользователя -->
    <div v-if="hasUserData" class="space-y-3">
      <!-- Основная информация -->
      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">👤 Информация о пользователе</h4>
        <div class="grid grid-cols-2 gap-2 text-sm">
          <div>ID: {{ userInfo.id || 'N/A' }}</div>
          <div>Username: {{ userInfo.username || 'N/A' }}</div>
          <div>Telegram ID: {{ userInfo.telegramId || 'N/A' }}</div>
          <div>Ref: {{ userInfo.ref || 'Нет' }}</div>
        </div>
      </div>

      <!-- Балансы -->
      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">💰 Балансы</h4>
        <div class="grid grid-cols-2 gap-2 text-sm">
          <div>Основной: {{ formattedBalances.balance }}</div>
          <div>Стейкинг: {{ formattedBalances.stakeBalance }}</div>
          <div>Прибыль: {{ formattedBalances.profitAll }}</div>
          <div>Партнерский: {{ formattedBalances.partnersBalance }}</div>
        </div>
        <div class="mt-2 text-lg font-bold text-green-400">
          Общий баланс: {{ formatBalance(getTotalBalance()) }}
        </div>
      </div>

      <!-- XP и уровень -->
      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">⭐ Опыт и уровень</h4>
        <div class="space-y-2">
          <div class="flex justify-between text-sm">
            <span>Уровень {{ xpInfo.level }}</span>
            <span>{{ xpInfo.current }}/{{ xpInfo.max }} XP</span>
          </div>
          <div class="w-full bg-gray-600 rounded-full h-2">
            <div 
              class="bg-green-500 h-2 rounded-full transition-all duration-300"
              :style="`width: ${xpInfo.percentage}%`"
            ></div>
          </div>
          <div class="text-xs text-gray-400">
            Raw XP: {{ xpInfo.raw }}
          </div>
        </div>
      </div>

      <!-- Время обновления -->
      <div class="bg-gray-700 p-3 rounded">
        <h4 class="font-semibold mb-2">🕒 Статус обновления</h4>
        <div class="text-sm space-y-1">
          <div>Последнее обновление: {{ getLastUpdatedFormatted() }}</div>
          <div class="text-gray-400">Автообновление каждые 30 секунд</div>
        </div>
      </div>
    </div>

    <!-- Кнопки управления -->
    <div class="mt-4 flex gap-2">
      <button 
        @click="handleRefresh"
        :disabled="isLoading"
        class="px-4 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 disabled:cursor-not-allowed rounded text-sm font-medium transition-colors"
      >
        {{ isLoading ? 'Загрузка...' : '🔄 Обновить' }}
      </button>
      
      <button 
        @click="showRawData = !showRawData"
        class="px-4 py-2 bg-gray-600 hover:bg-gray-700 rounded text-sm font-medium transition-colors"
      >
        {{ showRawData ? '👁️ Скрыть данные' : '👁️ Показать данные' }}
      </button>
    </div>

    <!-- Сырые данные (для отладки) -->
    <div v-if="showRawData && userData" class="mt-4">
      <h4 class="font-semibold mb-2">🔍 Сырые данные (JSON)</h4>
      <pre class="bg-black p-3 rounded text-xs overflow-auto max-h-64 text-green-400">{{ JSON.stringify(userData, null, 2) }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useUser } from '../composables/useUser.js'

// Используем user store
const {
  userData,
  isLoading,
  hasUserData,
  error,
  userInfo,
  balance,
  stakeBalance,
  profitAll,
  partnersBalance,
  xpInfo,
  formattedBalances,
  formatBalance,
  getTotalBalance,
  getLastUpdatedFormatted,
  refreshUserData
} = useUser()

// Локальное состояние компонента
const showRawData = ref(false)

// Методы
const handleRefresh = () => {
  refreshUserData()
}
</script>

<style scoped>
.user-data-demo {
  font-family: 'TTCommons', monospace;
}

pre {
  font-family: 'Courier New', monospace;
}
</style>







