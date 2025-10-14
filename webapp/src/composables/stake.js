/**
 * Композабл для работы со стейкингом
 * Предоставляет функциональность для инвестирования, сбора прибыли и получения статистики
 */

import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useTelegramStore } from '../stores/telegram.js'
import { useApi } from './useApi.js'

export function useStake() {
  const telegramStore = useTelegramStore()
  const api = useApi()
  
  // Реактивные данные
  const stakeData = ref({
    currentTariff: 'TON',
    tariffName: 'TON',
    tariffIcon: '/icon/ton.svg',
    stakeBalance: 0,
    accumulatedProfit: 0,
    dailyProfitRate: 1.7,
    minAmount: 500,
    maxAmount: 10000,
    balance: 0,
    totalProfit: 0
  })
  
  const availableTariffs = ref([])
  const isLoading = ref(false)
  const error = ref(null)
  const isInvesting = ref(false)
  const isCollecting = ref(false)
  
  // Интервал для обновления прибыли
  let profitUpdateInterval = null
  const PROFIT_UPDATE_INTERVAL = 10000 // 10 секунд
  
  // Вычисляемые свойства
  const formattedStakeBalance = computed(() => {
    return stakeData.value.stakeBalance.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  })
  
  const formattedAccumulatedProfit = computed(() => {
    return stakeData.value.accumulatedProfit.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 6
    })
  })
  
  const formattedBalance = computed(() => {
    return stakeData.value.balance.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  })
  
  const canInvest = computed(() => {
    return stakeData.value.balance >= stakeData.value.minAmount
  })
  
  const canCollect = computed(() => {
    return stakeData.value.accumulatedProfit > 0
  })
  
  const hasActiveStake = computed(() => {
    return stakeData.value.stakeBalance > 0
  })
  
  const profitPercentage = computed(() => {
    if (stakeData.value.stakeBalance <= 0) return 0
    return ((stakeData.value.accumulatedProfit / stakeData.value.stakeBalance) * 100).toFixed(4)
  })
  
  /**
   * Получает Telegram ID из всех возможных источников
   */
  const getTelegramId = () => {
    return telegramStore.userId || 
           telegramStore.user?.id || 
           telegramStore.initDataUnsafe?.user?.id ||
           123456789 // Fallback для разработки
  }
  
  /**
   * Загружает статистику стейкинга
   */
  const loadStakeStats = async () => {
    try {
      isLoading.value = true
      error.value = null
      
      const telegramId = getTelegramId()
      console.log('📊 Загрузка статистики стейкинга для пользователя:', telegramId)
      
      const response = await api.get(`/api/stake/stats?telegram_id=${telegramId}`)
      
      if (response.success && response.data) {
        stakeData.value = {
          currentTariff: response.data.current_tariff,
          tariffName: response.data.tariff_name,
          tariffIcon: response.data.tariff_icon,
          stakeBalance: response.data.stake_balance,
          accumulatedProfit: response.data.accumulated_profit,
          dailyProfitRate: response.data.daily_profit_rate,
          minAmount: response.data.min_amount,
          maxAmount: response.data.max_amount,
          balance: response.data.balance,
          totalProfit: response.data.total_profit
        }
        
        console.log('✅ Статистика стейкинга загружена:', stakeData.value)
      } else {
        throw new Error(response.message || 'Ошибка загрузки статистики')
      }
      
    } catch (err) {
      console.error('❌ Ошибка загрузки статистики стейкинга:', err)
      error.value = err.message || 'Ошибка загрузки статистики'
      
      // Устанавливаем базовые значения
      stakeData.value = {
        currentTariff: 'TON',
        tariffName: 'TON',
        tariffIcon: '/icon/ton.svg',
        stakeBalance: 0,
        accumulatedProfit: 0,
        dailyProfitRate: 1.7,
        minAmount: 500,
        maxAmount: 10000,
        balance: 0,
        totalProfit: 0
      }
    } finally {
      isLoading.value = false
    }
  }
  
  /**
   * Загружает список доступных тарифов
   */
  const loadAvailableTariffs = async () => {
    try {
      console.log('📋 Загрузка списка тарифов...')
      
      const response = await api.get('/api/stake/tariffs')
      
      if (response.success && response.data) {
        availableTariffs.value = response.data.tariffs
        console.log('✅ Тарифы загружены:', availableTariffs.value)
      } else {
        throw new Error(response.message || 'Ошибка загрузки тарифов')
      }
      
    } catch (err) {
      console.error('❌ Ошибка загрузки тарифов:', err)
      // Устанавливаем базовые тарифы
      availableTariffs.value = [
        {
          code: 'TON',
          name: 'TON',
          icon: '/icon/ton.svg',
          min_amount: 500,
          max_amount: 10000,
          daily_profit: 1.7,
          balance_threshold: 0
        }
      ]
    }
  }
  
  /**
   * Инвестирует средства в стейкинг
   */
  const investInStake = async (amount) => {
    try {
      isInvesting.value = true
      error.value = null
      
      const telegramId = getTelegramId()
      const numAmount = parseFloat(amount)
      
      if (isNaN(numAmount) || numAmount <= 0) {
        throw new Error('Некорректная сумма инвестиции')
      }
      
      if (numAmount < stakeData.value.minAmount) {
        throw new Error(`Минимальная сумма инвестиции: ${stakeData.value.minAmount}`)
      }
      
      if (numAmount > stakeData.value.maxAmount) {
        throw new Error(`Максимальная сумма инвестиции: ${stakeData.value.maxAmount}`)
      }
      
      if (numAmount > stakeData.value.balance) {
        throw new Error('Недостаточно средств на балансе')
      }
      
      console.log('💰 Инвестирование в стейкинг:', { telegramId, amount: numAmount })
      
      const response = await api.post('/api/stake/invest', {
        telegram_id: telegramId,
        amount: numAmount
      })
      
      if (response.success) {
        console.log('✅ Инвестиция успешно создана:', response.data)
        
        // Обновляем локальные данные
        stakeData.value.balance = response.data.new_balance
        stakeData.value.stakeBalance = response.data.new_stake_balance
        
        // Показываем уведомление
        if (telegramStore.isInitialized) {
          telegramStore.showAlert(`Успешно инвестировано ${numAmount} ₽`)
          telegramStore.hapticFeedback('success')
        }
        
        return response.data
      } else {
        throw new Error(response.message || 'Ошибка инвестирования')
      }
      
    } catch (err) {
      console.error('❌ Ошибка инвестирования:', err)
      error.value = err.message || 'Ошибка инвестирования'
      
      if (telegramStore.isInitialized) {
        telegramStore.showAlert(error.value)
      }
      
      throw err
    } finally {
      isInvesting.value = false
    }
  }
  
  /**
   * Собирает накопленную прибыль
   */
  const collectProfit = async () => {
    try {
      isCollecting.value = true
      error.value = null
      
      const telegramId = getTelegramId()
      
      if (stakeData.value.accumulatedProfit <= 0) {
        throw new Error('Нет прибыли для сбора')
      }
      
      console.log('🏦 Сбор прибыли со стейкинга для пользователя:', telegramId)
      
      const response = await api.post(`/api/stake/collect?telegram_id=${telegramId}`)
      
      if (response.success) {
        console.log('✅ Прибыль успешно собрана:', response.data)
        
        const collectedAmount = response.data.collected_amount
        
        // Обновляем локальные данные
        stakeData.value.balance = response.data.new_balance
        stakeData.value.accumulatedProfit = 0
        stakeData.value.totalProfit = response.data.total_profit
        
        // Показываем уведомление
        if (telegramStore.isInitialized) {
          telegramStore.showAlert(`Собрано ${collectedAmount.toFixed(6)} ₽ прибыли`)
          telegramStore.hapticFeedback('success')
        }
        
        return response.data
      } else {
        throw new Error(response.message || 'Ошибка сбора прибыли')
      }
      
    } catch (err) {
      console.error('❌ Ошибка сбора прибыли:', err)
      error.value = err.message || 'Ошибка сбора прибыли'
      
      if (telegramStore.isInitialized) {
        telegramStore.showAlert(error.value)
      }
      
      throw err
    } finally {
      isCollecting.value = false
    }
  }
  
  /**
   * Принудительно обновляет статистику
   */
  const refreshStakeData = async () => {
    console.log('🔄 Принудительное обновление данных стейкинга...')
    await loadStakeStats()
  }
  
  /**
   * Запускает периодическое обновление прибыли
   */
  const startProfitUpdates = () => {
    if (profitUpdateInterval) {
      clearInterval(profitUpdateInterval)
    }
    
    console.log('⏰ Запуск периодического обновления прибыли')
    
    profitUpdateInterval = setInterval(async () => {
      if (hasActiveStake.value && !isLoading.value) {
        try {
          await loadStakeStats()
        } catch (err) {
          console.warn('⚠️ Ошибка автообновления прибыли:', err)
        }
      }
    }, PROFIT_UPDATE_INTERVAL)
  }
  
  /**
   * Останавливает периодическое обновление прибыли
   */
  const stopProfitUpdates = () => {
    if (profitUpdateInterval) {
      console.log('⏹️ Остановка периодического обновления прибыли')
      clearInterval(profitUpdateInterval)
      profitUpdateInterval = null
    }
  }
  
  /**
   * Получает информацию о тарифе по коду
   */
  const getTariffInfo = (tariffCode) => {
    return availableTariffs.value.find(t => t.code === tariffCode) || availableTariffs.value[0]
  }
  
  /**
   * Форматирует сумму для отображения
   */
  const formatAmount = (amount, decimals = 2) => {
    return parseFloat(amount).toLocaleString('ru-RU', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    })
  }
  
  /**
   * Рассчитывает потенциальную дневную прибыль
   */
  const calculateDailyProfit = (amount) => {
    const numAmount = parseFloat(amount)
    if (isNaN(numAmount) || numAmount <= 0) return 0
    
    return (numAmount * stakeData.value.dailyProfitRate / 100).toFixed(6)
  }
  
  // Инициализация при создании композабла
  onMounted(async () => {
    console.log('🚀 Инициализация композабла стейкинга')
    
    // Загружаем начальные данные
    await Promise.all([
      loadStakeStats(),
      loadAvailableTariffs()
    ])
    
    // Запускаем периодическое обновление если есть активный стейк
    if (hasActiveStake.value) {
      startProfitUpdates()
    }
  })
  
  // Очистка при размонтировании
  onUnmounted(() => {
    stopProfitUpdates()
  })
  
  return {
    // Данные
    stakeData,
    availableTariffs,
    isLoading,
    error,
    isInvesting,
    isCollecting,
    
    // Вычисляемые свойства
    formattedStakeBalance,
    formattedAccumulatedProfit,
    formattedBalance,
    canInvest,
    canCollect,
    hasActiveStake,
    profitPercentage,
    
    // Методы загрузки данных
    loadStakeStats,
    loadAvailableTariffs,
    refreshStakeData,
    
    // Основные методы
    investInStake,
    collectProfit,
    
    // Управление обновлениями
    startProfitUpdates,
    stopProfitUpdates,
    
    // Утилиты
    getTariffInfo,
    formatAmount,
    calculateDailyProfit,
    getTelegramId
  }
}

export default useStake
