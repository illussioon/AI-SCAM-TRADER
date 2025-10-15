<template>
    <div class="flex flex-col w-full">
      <!-- Header Section -->
      <div class="w-full h-[52px] bg-[#1A1B20] border-b border-[#141517] rounded-t-[10px] flex items-center pl-2">
        <img 
          alt="TON" 
          class="h-[24px] w-[24px] ml-[6px] rounded-full object-cover" 
          loading="eager" 
          decoding="async" 
          draggable="false" 
          :src="iconUrl"
        >
        <div class="flex flex-col ml-[6px] -space-y-2 mt-2">
          <p class="text-[13px] opacity-50 text-gray-400">Ваш тариф:</p>
          <p class="text-[19px] font-medium text-white">{{ planName }}</p>
        </div>
      </div>
  
      <!-- Profitability Section -->
      <div class="w-full h-[52px] bg-[#1A1B20] rounded-b-[10px] flex items-center pl-4">
        <svg 
          viewBox="0 0 24 24" 
          xmlns="http://www.w3.org/2000/svg" 
          width="24" 
          height="24" 
          fill="none" 
          class="h-[23px] w-[23px] scale-125"
        >
          <rect 
            width="24" 
            height="24" 
            x="0" 
            y="0" 
            fill="rgb(255,255,255)" 
            fill-opacity="0"
          />
          <path 
            d="M12 16C11.45 16 10.9793 15.8043 10.588 15.413C10.1967 15.0217 10.0007 14.5507 10 14C9.99933 13.4493 10.1953 12.9787 10.588 12.588C10.9807 12.1973 11.4513 12.0013 12 12C12.5487 11.9987 13.0197 12.1947 13.413 12.588C13.8063 12.9813 14.002 13.452 14 14C13.998 14.548 13.8023 15.019 13.413 15.413C13.0237 15.807 12.5527 16.0027 12 16ZM7.375 7L16.625 7L17.9 4.45C18.0667 4.11667 18.054 3.79167 17.862 3.475C17.67 3.15833 17.3827 3 17 3L7 3C6.61667 3 6.32933 3.15833 6.138 3.475C5.94667 3.79167 5.934 4.11667 6.1 4.45L7.375 7ZM8.4 21L15.6 21C17.1 21 18.375 20.4793 19.425 19.438C20.475 18.3967 21 17.1173 21 15.6C21 14.9667 20.8917 14.35 20.675 13.75C20.4583 13.15 20.15 12.6083 19.75 12.125L17.15 9L6.85 9L4.25 12.125C3.85 12.6083 3.54167 13.15 3.325 13.75C3.10833 14.35 3 14.9667 3 15.6C3 17.1167 3.521 18.396 4.563 19.438C5.605 20.48 6.884 21.0007 8.4 21Z" 
            fill="rgb(158,165,173)" 
            fill-rule="nonzero"
          />
        </svg>
        <div class="flex flex-col ml-2 -space-y-2 mt-2">
          <p class="text-[13px] opacity-50 text-gray-400">Доходность</p>
          <p class="text-[19px] font-medium text-white">+ {{ profitability }}% за 24 часа</p>
        </div>
      </div>
  
      <!-- Input Section -->
      <div class="mt-3">
        <div class="flex justify-between items-center mb-2">
          <p class="text-[16px] text-[#747474]">Минимальная сумма {{ formatAmount(minAmount) }} ₽</p>
          <p class="text-[14px] text-[#747474]">Доступно: {{ formatAmount(availableBalance) }} ₽</p>
        </div>
        <input 
          v-model="amount"
          class="file:text-foreground placeholder:gray-400 text-white selection:bg-primary selection:text-primary-foreground dark:bg-[#27282A] border-input flex h-[47px] w-full min-w-0 placeholder:font-normal rounded-[17px] bg-transparent px-3 pt-1 text-[17px] font-semibold transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive placeholder:text-[20px]" 
          placeholder="Введите сумму" 
          inputmode="numeric" 
          type="text"
          :class="{ 'border-red-500': amountError }"
        >
        <p v-if="amountError" class="text-red-400 text-[14px] mt-1">{{ amountError }}</p>
        <p v-if="numericAmount > 0" class="text-[#747474] text-[14px] mt-1">
          Прибыль в день: ~{{ formatAmount((numericAmount * profitability / 100)) }} ₽ (+{{ profitability }}%)
        </p>
      </div>
    </div>
  
    <!-- Footer Button -->
    <div class="flex flex-col gap-2 mb-[200px] mt-5">
      <button 
        class="inline-flex items-center justify-center gap-2 whitespace-nowrap transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive box-border border border-white/30 rounded-[10px] backdrop-blur-[181.9px] bg-gradient-to-b from-[#B3F106] to-[#5EFF03] px-4 py-2 has-[>svg]:px-3 w-full mx-auto h-[48px] text-[18px] font-semibold text-black"
        :disabled="isButtonDisabled || isInvesting"
        @click="handleInvest"
      >
        <div v-if="isInvesting" class="animate-spin rounded-full h-5 w-5 border-b-2 border-black"></div>
        <span v-else>Инвестировать</span>
      </button>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, watch, onMounted } from 'vue'
  import useStake from '../../../../composables/stake.js'
  
  // Получаем доступ к стейк композаблу
  const { 
    stakeData, 
    isInvesting, 
    investInStake, 
    loadStakeStats,
    formatAmount,
    error 
  } = useStake()
  
  // Эмиты для взаимодействия с родительским компонентом
  const emit = defineEmits(['invested', 'close'])
  
  // Reactive data
  const amount = ref('')
  
  // Computed properties для данных из стейка
  const iconUrl = computed(() => stakeData.value.tariffIcon || '/icon/ton.svg')
  const planName = computed(() => stakeData.value.tariffName || 'TON')
  const profitability = computed(() => stakeData.value.dailyProfitRate || '0')
  const minAmount = computed(() => stakeData.value.minAmount || 100)
  const maxAmount = computed(() => stakeData.value.maxAmount || 10000)
  const availableBalance = computed(() => stakeData.value.balance || 0)
  
  // Computed properties для валидации
  const numericAmount = computed(() => {
    const num = parseFloat(amount.value)
    return isNaN(num) ? 0 : num
  })
  
  const isButtonDisabled = computed(() => {
    return !amount.value || 
           numericAmount.value < minAmount.value || 
           numericAmount.value > maxAmount.value ||
           numericAmount.value > availableBalance.value ||
           isInvesting.value
  })
  
  const amountError = computed(() => {
    if (!amount.value) return ''
    
    if (numericAmount.value < minAmount.value) {
      return `Минимальная сумма: ${formatAmount(minAmount.value)} ₽`
    }
    
    if (numericAmount.value > maxAmount.value) {
      return `Максимальная сумма: ${formatAmount(maxAmount.value)} ₽`
    }
    
    if (numericAmount.value > availableBalance.value) {
      return `Недостаточно средств. Доступно: ${formatAmount(availableBalance.value)} ₽`
    }
    
    return ''
  })
  
  // Methods
  const handleInvest = async () => {
    if (isButtonDisabled.value) return
    
    try {
      console.log('🚀 Начало инвестирования:', numericAmount.value)
      
      const result = await investInStake(numericAmount.value)
      
      console.log('✅ Инвестирование успешно завершено:', result)
      
      // Уведомляем родительский компонент об успешном инвестировании
      emit('invested', {
        amount: numericAmount.value,
        result: result
      })
      
      // Закрываем попап
      emit('close')
      
      // Очищаем поле ввода
      amount.value = ''
      
    } catch (err) {
      console.error('❌ Ошибка инвестирования:', err)
      // Ошибка уже обрабатывается в композабле
    }
  }
  
  // Инициализация при монтировании
  onMounted(async () => {
    console.log('🔄 Инициализация popup-content-stake...')
    await loadStakeStats()
  })
  
  // Автоматическое форматирование ввода
  watch(amount, (newValue) => {
    // Удаляем все символы кроме цифр и точки
    const cleaned = newValue.replace(/[^\d.]/g, '')
    
    // Проверяем на корректность десятичного числа
    const parts = cleaned.split('.')
    if (parts.length > 2) {
      // Больше одной точки - оставляем только первую
      amount.value = parts[0] + '.' + parts.slice(1).join('')
    } else if (cleaned !== newValue) {
      amount.value = cleaned
    }
  })
  </script>
  
  <style scoped>
  /* Дополнительные стили, если нужны */
  </style>