/**
 * Композабл для работы со стейкингом
 * Предоставляет функциональность для инвестирования, сбора прибыли и получения статистики
 */

import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useTelegramStore } from '../stores/telegram.js'
import { useUserStore } from '../stores/user.js'
import { useApi } from './useApi.js'

export function useStake() {
  const telegramStore = useTelegramStore()
  const userStore = useUserStore()
  const api = useApi()
  
  // Используем данные из пользовательского store
  const stakeData = computed(() => userStore.stakeData)
  const isLoading = computed(() => userStore.isStakeLoading)
  const error = computed(() => userStore.stakeError)
  
  // Локальные состояния для операций
  const availableTariffs = ref([])
  const isInvesting = ref(false)
  const isCollecting = ref(false)
  
  // Интервал для обновления прибыли
  let profitUpdateInterval = null
  const PROFIT_UPDATE_INTERVAL = 10000 // 10 секунд
  
  // Вычисляемые свойства (берем из store или создаем дополнительные)
  const formattedStakeBalance = computed(() => userStore.formattedStakeBalance)
  const formattedAccumulatedProfit = computed(() => userStore.formattedAccumulatedProfit)
  
  const formattedBalance = computed(() => {
    return stakeData.value.balance.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  })
  
  const canInvest = computed(() => userStore.canInvest)
  const canCollect = computed(() => userStore.canCollect)
  const hasActiveStake = computed(() => userStore.hasActiveStake)
  
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
           telegramStore.initDataUnsafe?.user?.id
  }
  
  /**
   * Загружает статистику стейкинга (теперь через store)
   */
  const loadStakeStats = async () => {
    console.log('📊 Загрузка статистики стейкинга через store...')
    return await userStore.fetchStakeData()
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
        
        // Обновляем данные в store
        userStore.updateStakeData({
          balance: response.data.new_balance,
          stakeBalance: response.data.new_stake_balance
        })
        
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
      const errorMessage = err.message || 'Ошибка инвестирования'
      
      if (telegramStore.isInitialized) {
        telegramStore.showAlert(errorMessage)
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
        
        // Обновляем данные в store
        userStore.updateStakeData({
          balance: response.data.new_balance,
          accumulatedProfit: 0,
          totalProfit: response.data.total_profit
        })
        
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
      const errorMessage = err.message || 'Ошибка сбора прибыли'
      
      if (telegramStore.isInitialized) {
        telegramStore.showAlert(errorMessage)
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
          console.log('🔄 Автообновление прибыли стейкинга...')
          await userStore.fetchStakeData()
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
  
  // Инициализация при создании композабла (данные уже загружаются в store)
  onMounted(async () => {
    console.log('🚀 Инициализация композабла стейкинга')
    
    // Загружаем только тарифы (данные стейка уже в store)
    await loadAvailableTariffs()
    
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

