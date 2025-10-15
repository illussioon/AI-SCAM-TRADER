<template>
    <div class="h-[300px] rounded-t-[14px] bg-[rgba(19,20,23,0.7)] mt-4 px-[8px] pt-[6px] flex flex-col">
      <div class="flex gap-x-[6px]">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'gap-2 whitespace-nowrap disabled:pointer-events-none disabled:opacity-50',
            '[&_svg]:pointer-events-none [&_svg:not([class*=\'size-\'])]:size-4 shrink-0 [&_svg]:shrink-0',
            'outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]',
            'aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive',
            'shadow-xs hover:bg-primary/90 px-4 py-2 has-[>svg]:px-3',
            'flex items-center justify-center box-border border-[0.55px] rounded-[72px]',
            'backdrop-blur-[11.0317px] text-[17.65px] font-semibold leading-[15px]',
            'transition-colors duration-300 ease-in-out',
            tab.width,
            'h-[33px]',
            activeTab === tab.id 
              ? 'border-[rgba(255,255,255,0.1)] bg-gradient-to-b from-[#B3F106] to-[#5EFF03] text-black'
              : 'border-[#2e3032] bg-[rgba(255,255,255,0.05)] text-white'
          ]"
          data-slot="button"
        >
          <p class="mt-1">{{ tab.label }}</p>
        </button>
      </div>
  
      <!-- Loading State -->
      <div v-if="isLoading" class="flex-1 flex flex-col items-center justify-center">
        <div class="animate-spin rounded-full h-8 w-8 border-b-2 border-[#5EFF03]"></div>
        <p class="text-white/50 text-xs mt-2">Загрузка...</p>
      </div>

      <!-- Transaction List -->
      <div v-else-if="filteredTransactions.length > 0" class="flex-1 pt-[14px] pb-[8px] flex flex-col gap-y-[6px] overflow-y-auto custom-scrollbar">
        <div
          v-for="transaction in filteredTransactions"
          :key="transaction.id"
          class="bg-[rgba(30,31,36,0.5)] rounded-lg p-3 border border-white/5 hover:border-white/10 transition-colors"
        >
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2.5">
              <!-- Icon -->
              <div
                :class="[
                  'w-8 h-8 rounded-full flex items-center justify-center',
                  transaction.is_positive ? 'bg-green-500/20' : 'bg-red-500/20'
                ]"
              >
                <svg
                  v-if="transaction.is_positive"
                  class="w-4 h-4 text-green-400"
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
                  class="w-4 h-4 text-red-400"
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
                <p class="text-white text-[13px] font-medium">
                  {{ transaction.action_description }}
                </p>
                <p class="text-white/40 text-[10px] mt-0.5">
                  {{ formatDate(transaction.created_at) }}
                </p>
              </div>
            </div>

            <!-- Amount -->
            <div class="text-right">
              <p
                :class="[
                  'font-semibold text-[14px]',
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
      <div v-else class="flex-1 flex flex-col items-center justify-center p-4">
        <div class="w-12 h-12 rounded-full bg-white/5 flex items-center justify-center mb-3">
          <svg
            class="w-6 h-6 text-white/30"
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
        <p class="text-white/70 text-sm mb-1">{{ getEmptyMessage() }}</p>
        <p class="text-white/50 text-xs">{{ getEmptyDescription() }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  import { usePayHistory } from '../../../composables/pay-history.js'
  
  // Используем композабл для работы с историей платежей
  const {
    transactions,
    isLoading,
    loadTransactions,
    formatAmount,
    formatDate,
    getTelegramId
  } = usePayHistory()
  
  const activeTab = ref('all')
  
  const tabs = [
    { id: 'all', label: 'Все', width: 'w-[86px]' },
    { id: 'deposits', label: 'Пополнения', width: 'w-[117px]' },
    { id: 'withdrawals', label: 'Вывод', width: 'w-[88px]' }
  ]
  
  // Отфильтрованные транзакции на основе активной вкладки
  const filteredTransactions = computed(() => {
    if (activeTab.value === 'all') {
      return transactions.value
    } else if (activeTab.value === 'deposits') {
      // Пополнения: dep, dep_stake, dep_ref, stake_profit
      return transactions.value.filter(t => 
        ['dep', 'dep_stake', 'dep_ref', 'stake_profit'].includes(t.action)
      )
    } else if (activeTab.value === 'withdrawals') {
      // Выводы: withdraw, withdraw_stake
      return transactions.value.filter(t => 
        ['withdraw', 'withdraw_stake'].includes(t.action)
      )
    }
    return transactions.value
  })
  
  // Сообщения для пустого состояния
  const getEmptyMessage = () => {
    if (activeTab.value === 'deposits') {
      return 'Пополнений не найдено'
    } else if (activeTab.value === 'withdrawals') {
      return 'Выводов не найдено'
    }
    return 'Операций не найдено'
  }
  
  const getEmptyDescription = () => {
    if (activeTab.value === 'deposits') {
      return 'У вас пока нет операций пополнения'
    } else if (activeTab.value === 'withdrawals') {
      return 'У вас пока нет операций вывода'
    }
    return 'У вас пока нет операций'
  }
  
  // Загрузка транзакций при монтировании
  onMounted(async () => {
    const telegramId = getTelegramId()
    
    if (telegramId) {
      try {
        await loadTransactions(10, 0) // Загружаем последние 10 транзакций
      } catch (err) {
        console.error('❌ Ошибка загрузки транзакций:', err)
      }
    }
  })
  </script>

  <style scoped>
  /* Кастомный скроллбар */
  .custom-scrollbar::-webkit-scrollbar {
    width: 4px;
  }
  
  .custom-scrollbar::-webkit-scrollbar-track {
    background: rgba(255, 255, 255, 0.05);
    border-radius: 2px;
  }
  
  .custom-scrollbar::-webkit-scrollbar-thumb {
    background: rgba(94, 255, 3, 0.3);
    border-radius: 2px;
  }
  
  .custom-scrollbar::-webkit-scrollbar-thumb:hover {
    background: rgba(94, 255, 3, 0.5);
  }
  </style>