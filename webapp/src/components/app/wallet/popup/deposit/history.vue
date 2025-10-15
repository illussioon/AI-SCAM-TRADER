<template>
  <div
    data-state="active"
    data-orientation="horizontal"
    role="tabpanel"
    aria-labelledby="radix-r11-trigger-history"
    id="radix-r11-content-history"
    tabindex="0"
    data-slot="tabs-content"
    class="flex-1 outline-none"
  >
    <!-- Loading State -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center p-8">
      <div class="animate-spin rounded-full h-10 w-10 border-b-2 border-[#5EFF03]"></div>
      <p class="text-white/70 mt-4">Загрузка...</p>
    </div>

    <!-- Transaction List -->
    <div v-else-if="filteredTransactions.length > 0" class="px-5 space-y-3 pb-24 mt-4">
      <div
        v-for="transaction in filteredTransactions"
        :key="transaction.id"
        class="bg-[#1E1F24] rounded-xl p-4 border border-white/10"
      >
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <!-- Icon -->
            <div
              :class="[
                'w-10 h-10 rounded-full flex items-center justify-center',
                transaction.is_positive
                  ? 'bg-green-500/20'
                  : 'bg-red-500/20'
              ]"
            >
              <svg
                v-if="transaction.is_positive"
                class="w-5 h-5 text-green-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 4v16m8-8H4"
                />
              </svg>
              <svg
                v-else
                class="w-5 h-5 text-red-400"
                fill="none"
                stroke="currentColor"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M20 12H4"
                />
              </svg>
            </div>

            <!-- Info -->
            <div>
              <p class="text-white font-medium text-[15px]">
                {{ transaction.action_description }}
              </p>
              <p class="text-white/50 text-[12px] mt-0.5">
                {{ formatDate(transaction.created_at) }}
              </p>
            </div>
          </div>

          <!-- Amount -->
          <div class="text-right">
            <p
              :class="[
                'font-semibold text-[16px]',
                transaction.is_positive ? 'text-green-400' : 'text-red-400'
              ]"
            >
              {{ transaction.is_positive ? '+' : '' }}{{ formatAmount(transaction.amount) }} ₽
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Empty State -->
    <div v-else class="flex flex-col items-center justify-center p-8 mt-8">
      <div class="w-16 h-16 rounded-full bg-white/5 flex items-center justify-center mb-4">
        <svg
          class="w-8 h-8 text-white/30"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
          />
        </svg>
      </div>
      <p class="text-white/70 text-lg mb-2">История пуста</p>
      <p class="text-white/50 text-sm text-center">
        {{ getEmptyMessage() }}
      </p>
    </div>

    <!-- Spacing -->
    <div class="h-20 mt-2"></div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { usePayHistory } from '../../../../../composables/pay-history.js'
import { useTelegramStore } from '../../../../../stores/telegram.js'
import { useUserStore } from '../../../../../stores/user.js'

console.log('📄 [HISTORY.VUE] Скрипт инициализирован')

// Получаем stores для проверки
const telegramStore = useTelegramStore()
const userStore = useUserStore()

// Используем композабл для работы с историей платежей
const {
  transactions,
  isLoading,
  error,
  loadTransactions,
  formatAmount,
  formatDate,
  getTelegramId
} = usePayHistory()

console.log('📄 [HISTORY.VUE] Композабл usePayHistory инициализирован')
console.log('📄 [HISTORY.VUE] transactions:', transactions)
console.log('📄 [HISTORY.VUE] isLoading:', isLoading)
console.log('📄 [HISTORY.VUE] telegramStore.userId:', telegramStore.userId)

// Отфильтрованные транзакции - только пополнения и выводы основного баланса
const filteredTransactions = computed(() => {
  // Фильтруем только операции с основным балансом:
  // - dep: пополнение баланса
  // - dep_ref: реферальный бонус
  // - stake_profit: прибыль со стейка (собранная на баланс)
  // - withdraw: вывод с основного баланса
  const filtered = transactions.value.filter(t => 
    ['dep', 'dep_ref', 'stake_profit', 'withdraw'].includes(t.action)
  )
  console.log(`📊 Отфильтровано транзакций основного баланса:`, filtered.length)
  return filtered
})

// Сообщение для пустого состояния
const getEmptyMessage = () => {
  return 'У вас пока нет операций с основным балансом'
}

// Загрузка при монтировании компонента
onMounted(() => {
  console.log('=' .repeat(50))
  console.log('🚀 [HISTORY] ✨✨✨ onMounted ВЫЗВАН ✨✨✨')
  console.log('🚀 [HISTORY] Компонент истории транзакций смонтирован')
  console.log('🚀 [HISTORY] transactions.value:', transactions.value)
  console.log('🚀 [HISTORY] isLoading.value:', isLoading.value)
  console.log('🚀 [HISTORY] error.value:', error.value)
  console.log('🚀 [HISTORY] telegramStore.isInitialized:', telegramStore.isInitialized)
  console.log('🚀 [HISTORY] telegramStore.userId:', telegramStore.userId)
  console.log('🚀 [HISTORY] userStore.isInitialized:', userStore.isInitialized)
  console.log('=' .repeat(50))
  
  // Простая задержка перед загрузкой
  setTimeout(async () => {
    console.log('⏰ [HISTORY] Таймаут завершен, начинаем загрузку...')
    
    const telegramId = getTelegramId()
    console.log('🆔 [HISTORY] Telegram ID получен:', telegramId)
    
    if (!telegramId) {
      console.error('❌ [HISTORY] Telegram ID не найден!')
      error.value = 'Telegram ID не найден'
      return
    }
    
    try {
      console.log('📞 [HISTORY] Вызов loadTransactions(20, 0)...')
      const result = await loadTransactions(20, 0)
      console.log('✅ [HISTORY] loadTransactions вернул:', result)
      console.log('📋 [HISTORY] Всего транзакций загружено:', transactions.value.length)
      console.log('📊 [HISTORY] transactions.value после загрузки:', transactions.value)
    } catch (err) {
      console.error('❌ [HISTORY] Ошибка в onMounted:', err)
    }
    
    console.log('=' .repeat(50))
  }, 1000)
})
</script>