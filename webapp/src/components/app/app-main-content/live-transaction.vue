<template>
    <section class="mt-5">
      <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
          <div 
            class="w-[9px] h-[9px] rounded-full shadow-[0_0_20px_4px_#5EFF0366,0_0_0_4px_rgba(144,247,5,0.1)]"
            :class="[
              isLoading ? 'bg-yellow-500 pulse' : 
              error ? 'bg-red-500' : 
              isDataStale ? 'bg-orange-500' : 
              'bg-[#90F705] waving-glow'
            ]"
          ></div>
        <h2 class="font-semibold text-xl">Live транзакции:</h2>

        </div>
        
        <!-- Кнопка обновления и статус -->
        <div class="flex items-center gap-2">
          <div v-if="lastUpdateFormatted" class="text-xs text-white/40">
            {{ lastUpdateFormatted }}
          </div>
          
          <button 
            @click="handleRefresh"
            :disabled="isLoading"
            class="p-1.5 rounded-lg bg-white/10 hover:bg-white/20 transition-colors disabled:opacity-50"
            title="Обновить транзакции"
          >
            <svg 
              class="w-4 h-4 transition-transform"
              :class="{ 'animate-spin': isLoading }"
              fill="none" 
              viewBox="0 0 24 24" 
              stroke="currentColor"
            >
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
          </button>
        </div>
      </div>
      
      <div class="mt-3 space-y-2">
        <!-- Состояние загрузки -->
        <div v-if="isLoading && transactions.length === 0" class="space-y-2">
          <div 
            v-for="i in 4" 
            :key="`skeleton-${i}`"
            class="flex items-center gap-3 rounded-xl bg-gradient-to-b from-[#1A1C20]/80 to-[#0F1013]/40 p-2 h-[52px] animate-pulse"
          >
            <div class="relative">
              <div class="w-[35px] h-[35px] rounded-full bg-white/10"></div>
              <div class="absolute -bottom-1 left-0 w-8 h-4 bg-white/10 rounded-md"></div>
            </div>
            <div class="flex-1">
              <div class="w-20 h-4 bg-white/10 rounded mb-1"></div>
              <div class="w-16 h-3 bg-white/10 rounded"></div>
            </div>
            <div class="text-right">
              <div class="w-12 h-3 bg-white/10 rounded mb-1"></div>
              <div class="w-16 h-4 bg-white/10 rounded"></div>
            </div>
          </div>
        </div>

        <!-- Ошибка загрузки -->
        <div v-else-if="error" class="flex flex-col items-center justify-center py-8 text-center">
          <div class="w-12 h-12 rounded-full bg-red-500/20 flex items-center justify-center mb-3">
            <svg class="w-6 h-6 text-red-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0l-5.898 8.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <p class="text-white/60 mb-2">Ошибка загрузки транзакций</p>
          <p class="text-sm text-white/40 mb-4">{{ error }}</p>
          <button 
            @click="handleRefresh"
            class="px-4 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg text-sm font-medium transition-colors"
          >
            Попробовать снова
          </button>
        </div>

        <!-- Пустое состояние -->
        <div v-else-if="transactions.length === 0" class="flex flex-col items-center justify-center py-8 text-center">
          <div class="w-12 h-12 rounded-full bg-white/10 flex items-center justify-center mb-3">
            <svg class="w-6 h-6 text-white/40" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
          </div>
          <p class="text-white/60 mb-2">Пока нет транзакций</p>
          <p class="text-sm text-white/40">Транзакции будут отображаться здесь в реальном времени</p>
        </div>

        <!-- Список транзакций -->
        <div 
          v-else 
          class="space-y-2 transition-opacity duration-300"
          :class="{ 'opacity-60': isLoading }"
        >
          <div 
            v-for="transaction in transactions" 
            :key="transaction.id"
            class="flex items-center gap-3 rounded-xl bg-gradient-to-b from-[#1A1C20]/80 to-[#0F1013]/40 p-2 h-[52px] hover:from-[#1A1C20] hover:to-[#0F1013] transition-all duration-200"
          >
            <div class="relative">
              <div class="w-full h-full rounded-full border-2" :style="{ borderColor: transaction.borderColor }">
                <img 
                  class="w-[35px] h-[35px] object-cover rounded-full" 
                  src="/img/avatar.webp"
                  alt="Avatar"
                >
              </div>
              <div 
                class="absolute -bottom-1 left-[0px] flex items-center gap-[2px] px-2 py-[2px] rounded-md font-bold text-[8px]"
                :class="transaction.cryptoClass"
                :style="{ backgroundColor: transaction.borderColor }"
              >
                <img 
                  v-if="transaction.cryptoIcon.startsWith('data:')" 
                  :alt="transaction.cryptoName" 
                  class="block w-[10px]" 
                  :src="transaction.cryptoIcon"
                >
                <img 
                  v-else
                  :alt="transaction.cryptoName" 
                  class="block w-[10px]" 
                  :src="transaction.cryptoIcon"
                  @error="$event.target.style.display = 'none'"
                >
                <p class="leading-none mt-[2px]">{{ transaction.cryptoName }}</p>
              </div>
            </div>
            
            <div class="flex-1">
              <div class="flex-col items-center gap-1">
                <p 
                  class="text-[18px]"
                  :class="transaction.type === 'deposit' ? 'text-[#1AE268]' : 'text-[#E41C1F]'"
                >
                  {{ transaction.typeText }}
                </p>
                <p class="text-[12px] text-white/40 -mt-1">ID: {{ transaction.id }}</p>
              </div>
            </div>
            
            <div class="text-right flex flex-col mt-1">
              <div class="text-[13px]">{{ transaction.time }}</div>
              <div 
                class="text-[18px] -mt-[2px]"
                :class="transaction.type === 'deposit' ? 'text-[#1AE268]' : 'text-[#E41B1F]'"
              >
                {{ transaction.amount }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
import { onMounted, onUnmounted } from 'vue';
import { useTransactions } from '@/composables/useTransactions';

// Используем composable для транзакций
const {
  liveTransactions: transactions,
  isLoading,
  error,
  transactionCount,
  lastUpdateFormatted,
  isDataStale,
  startAutoRefresh,
  stopAutoRefresh,
  fetchLiveTransactions
} = useTransactions();

// При монтировании компонента запускаем автообновление
onMounted(() => {
  console.log('🚀 Инициализация live транзакций...');
  
  // Запускаем автообновление каждые 10 секунд
  startAutoRefresh(10000);
});

// При размонтировании останавливаем автообновление
onUnmounted(() => {
  console.log('🛑 Останавливаем автообновление live транзакций');
  stopAutoRefresh();
});

// Ручное обновление транзакций
const handleRefresh = () => {
  fetchLiveTransactions();
};
  </script>
  
  <style scoped>
  .waving-glow {
    animation: wave-glow 2s ease-in-out infinite;
  }
  
  .pulse {
    animation: pulse 1.5s ease-in-out infinite;
  }
  
  @keyframes wave-glow {
    0%, 100% {
      box-shadow: 0 0 20px 4px #5EFF0366, 0 0 0 4px rgba(144, 247, 5, 0.1);
    }
    50% {
      box-shadow: 0 0 30px 6px #5EFF0388, 0 0 0 6px rgba(144, 247, 5, 0.2);
    }
  }
  
  @keyframes pulse {
    0%, 100% {
      opacity: 1;
      box-shadow: 0 0 20px 4px rgba(234, 179, 8, 0.4), 0 0 0 4px rgba(234, 179, 8, 0.1);
    }
    50% {
      opacity: 0.7;
      box-shadow: 0 0 30px 6px rgba(234, 179, 8, 0.6), 0 0 0 6px rgba(234, 179, 8, 0.2);
    }
  }
  
  /* Плавная анимация появления новых транзакций */
  .transaction-enter-active {
    transition: all 0.3s ease-out;
  }
  
  .transaction-enter-from {
    transform: translateX(-20px);
    opacity: 0;
  }
  
  .transaction-leave-active {
    transition: all 0.3s ease-in;
  }
  
  .transaction-leave-to {
    transform: translateX(20px);
    opacity: 0;
  }
  </style>