import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useApi } from '../composables/useApi.js'
import { useTelegramStore } from './telegram.js'

export const useUserStore = defineStore('user', () => {
  // API композабл
  const api = useApi()
  
  // Telegram store для получения telegram_id
  const telegramStore = useTelegramStore()
  
  // Состояние пользователя
  const userData = ref(null)
  const isLoading = ref(false)
  const isInitialized = ref(false)
  const lastUpdated = ref(null)
  const error = ref(null)
  
  // Состояние стейкинга
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
  const isStakeLoading = ref(false)
  const stakeLastUpdated = ref(null)
  const stakeError = ref(null)
  
  // Состояние рефералов
  const referralData = ref({
    activePartners: 0,
    level1Partners: 0,
    level23Partners: 0,
    totalPartners: 0,
    level1Active: 0,
    level23Active: 0
  })
  const isReferralLoading = ref(false)
  const referralLastUpdated = ref(null)
  const referralError = ref(null)
  
  // Интервал для автоматического обновления
  let updateInterval = null
  
  // Вычисляемые свойства
  const hasUserData = computed(() => userData.value !== null)
  
  const balance = computed(() => userData.value?.balance || '0.00')
  const stakeBalance = computed(() => userData.value?.stake_balance || '0.00') 
  const profitAll = computed(() => userData.value?.profit_all || '0.00')
  const partnersBalance = computed(() => userData.value?.partners_balance || '0.00')
  
  const userInfo = computed(() => ({
    id: userData.value?.id || null,
    username: userData.value?.username || null,
    telegramId: userData.value?.telegram_id || null,
    ref: userData.value?.ref || null,
    createAccount: userData.value?.create_account || null
  }))
  
  const xpInfo = computed(() => {
    if (!userData.value?.xp) {
      return {
        raw: '0/100',
        current: 0,
        max: 100,
        percentage: 0,
        level: 1
      }
    }
    return userData.value.xp
  })
  
  // Вычисляемые свойства для стейкинга
  const hasActiveStake = computed(() => stakeData.value.stakeBalance > 0)
  const canInvest = computed(() => stakeData.value.balance >= stakeData.value.minAmount)
  const canCollect = computed(() => stakeData.value.accumulatedProfit > 0)
  
  // Определение доступного тарифа на основе стейкового баланса
  const availableTariff = computed(() => {
    const stakeBalance = stakeData.value.stakeBalance
    
    // Пороги для тарифов (должны совпадать с серверными)
    if (stakeBalance >= 100000) return 'USDT' // 100,000₽
    if (stakeBalance >= 10000) return 'ETH'   // 10,000₽
    return 'TON' // Базовый тариф
  })
  
  // Проверка возможности повышения тарифа
  const canUpgradeTariff = computed(() => {
    return availableTariff.value !== stakeData.value.currentTariff
  })
  
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
  
  // Методы
  /**
   * Получает данные пользователя с сервера
   */
  const fetchUserData = async () => {
    try {
      isLoading.value = true
      error.value = null
      
      // Получаем telegram_id из telegram store
      const telegramId = telegramStore.userId
      
      if (!telegramId) {
        throw new Error('Telegram ID не найден')
      }
      
      console.log(`📊 Получение данных пользователя ${telegramId}...`)
      
      const response = await api.getUserStats(telegramId)
      
      if (response.success && response.data) {
        userData.value = response.data
        lastUpdated.value = new Date()
        
        console.log('✅ Данные пользователя получены:', userData.value)
      } else {
        throw new Error(response.message || 'Не удалось получить данные пользователя')
      }
      
    } catch (err) {
      console.error('❌ Ошибка получения данных пользователя:', err)
      error.value = err.message || 'Неизвестная ошибка'
      
      // Пытаемся создать пользователя, если он не существует
      if (err.message?.includes('404') || err.message?.includes('не найден')) {
        await createUserIfNotExists()
      }
    } finally {
      isLoading.value = false
    }
  }
  
  /**
   * Создает пользователя, если он не существует
   */
  const createUserIfNotExists = async () => {
    try {
      console.log('🔄 Попытка создания пользователя...')
      
      // Создаем пользователя через telegram store
      const result = await telegramStore.createUserOnServer()
      
      if (result?.success) {
        console.log('✅ Пользователь создан, повторное получение данных...')
        // Пытаемся снова получить данные
        await fetchUserData()
      }
    } catch (err) {
      console.error('❌ Ошибка создания пользователя:', err)
      error.value = 'Не удалось создать пользователя'
    }
  }
  
  /**
   * Получает данные стейкинга с сервера
   */
  const fetchStakeData = async () => {
    try {
      isStakeLoading.value = true
      stakeError.value = null
      
      const telegramId = telegramStore.userId
      if (!telegramId) {
        throw new Error('Telegram ID не найден')
      }
      
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
        
        stakeLastUpdated.value = new Date()
        console.log('✅ Статистика стейкинга загружена:', stakeData.value)
      } else {
        throw new Error(response.message || 'Ошибка загрузки статистики стейкинга')
      }
      
    } catch (err) {
      console.error('❌ Ошибка загрузки статистики стейкинга:', err)
      stakeError.value = err.message || 'Ошибка загрузки статистики стейкинга'
      
      // Устанавливаем базовые значения при ошибке
      stakeData.value = {
        currentTariff: 'TON',
        tariffName: 'TON',
        tariffIcon: '/icon/ton.svg',
        stakeBalance: 0,
        accumulatedProfit: 0,
        dailyProfitRate: 1.7,
        minAmount: 500,
        maxAmount: 10000,
        balance: userData.value?.balance || 0,
        totalProfit: 0
      }
    } finally {
      isStakeLoading.value = false
    }
  }

  /**
   * Получает детальную статистику рефералов с сервера
   */
  const fetchReferralData = async () => {
    try {
      isReferralLoading.value = true
      referralError.value = null
      
      const telegramId = telegramStore.userId
      if (!telegramId) {
        throw new Error('Telegram ID не найден')
      }
      
      console.log('📊 Загрузка статистики рефералов для пользователя:', telegramId)
      
      const response = await api.get(`/api/referral/detailed-stats?telegram_id=${telegramId}`)
      
      if (response.success && response.data) {
        referralData.value = {
          activePartners: response.data.active_partners || 0,
          level1Partners: response.data.level1_partners || 0,
          level23Partners: response.data.level23_partners || 0,
          totalPartners: response.data.total_partners || 0,
          level1Active: response.data.level1_active || 0,
          level23Active: response.data.level23_active || 0
        }
        
        referralLastUpdated.value = new Date()
        console.log('✅ Статистика рефералов загружена:', referralData.value)
      } else {
        throw new Error(response.message || 'Ошибка загрузки статистики рефералов')
      }
      
    } catch (err) {
      console.error('❌ Ошибка загрузки статистики рефералов:', err)
      referralError.value = err.message || 'Ошибка загрузки статистики рефералов'
      
      // Устанавливаем базовые значения при ошибке
      referralData.value = {
        activePartners: 0,
        level1Partners: 0,
        level23Partners: 0,
        totalPartners: 0,
        level1Active: 0,
        level23Active: 0
      }
    } finally {
      isReferralLoading.value = false
    }
  }
  
  /**
   * Обновляет данные стейкинга после операций
   */
  const updateStakeData = (newData) => {
    if (newData) {
      const oldTariff = stakeData.value.currentTariff
      Object.assign(stakeData.value, newData)
      stakeLastUpdated.value = new Date()
      
      // Проверяем изменение тарифа
      const newTariff = availableTariff.value
      if (newTariff !== oldTariff) {
        console.log(`🎉 Тариф повышен: ${oldTariff} → ${newTariff} (стейк баланс: ${stakeData.value.stakeBalance}₽)`)
        
        // Обновляем данные стейка с сервера для получения нового тарифа
        setTimeout(() => {
          fetchStakeData()
        }, 1000)
      }
      
      console.log('🔄 Данные стейкинга обновлены:', stakeData.value)
    }
  }
  
  /**
   * Инициализирует автоматическое обновление данных
   */
  const startAutoUpdate = (intervalMs = 30000) => {
    // Очищаем предыдущий интервал, если есть
    stopAutoUpdate()
    
    console.log(`🔄 Запуск автоматического обновления каждые ${intervalMs/1000} секунд`)
    
    updateInterval = setInterval(async () => {
      if (!isLoading.value && !isStakeLoading.value && !isReferralLoading.value) {
        console.log('🔄 Автоматическое обновление данных пользователя, стейка и рефералов...')
        await Promise.all([
          fetchUserData(),
          fetchStakeData(),
          fetchReferralData()
        ])
      }
    }, intervalMs)
  }
  
  /**
   * Останавливает автоматическое обновление
   */
  const stopAutoUpdate = () => {
    if (updateInterval) {
      clearInterval(updateInterval)
      updateInterval = null
      console.log('⏹️ Автоматическое обновление остановлено')
    }
  }
  
  /**
   * Инициализирует пользовательские данные
   */
  const initialize = async () => {
    if (isInitialized.value) return
    
    try {
      console.log('🚀 Инициализация пользовательских данных...')
      
      // Ждем инициализации telegram store
      if (!telegramStore.isInitialized) {
        console.log('⏳ Ожидание инициализации Telegram...')
        // Уменьшенная задержка для инициализации telegram
        await new Promise(resolve => setTimeout(resolve, 500))
      }
      
      // Получаем начальные данные параллельно
      await Promise.all([
        fetchUserData(),
        fetchStakeData(),
        fetchReferralData()
      ])
      
      // Запускаем автообновление
      startAutoUpdate(30000) // 30 секунд
      
      isInitialized.value = true
      console.log('✅ Пользовательские данные инициализированы')
      
    } catch (err) {
      console.error('❌ Ошибка инициализации пользовательских данных:', err)
      error.value = err.message || 'Ошибка инициализации'
    }
  }
  
  /**
   * Принудительное обновление данных
   */
  const refreshUserData = async () => {
    console.log('🔄 Принудительное обновление данных пользователя, стейка и рефералов...')
    await Promise.all([
      fetchUserData(),
      fetchStakeData(),
      fetchReferralData()
    ])
  }
  
  /**
   * Очистка данных (при logout или смене пользователя)
   */
  const clearUserData = () => {
    stopAutoUpdate()
    userData.value = null
    isInitialized.value = false
    lastUpdated.value = null
    error.value = null
    
    // Очищаем данные стейкинга
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
    stakeLastUpdated.value = null
    stakeError.value = null
    
    // Очищаем данные рефералов
    referralData.value = {
      activePartners: 0,
      level1Partners: 0,
      level23Partners: 0,
      totalPartners: 0,
      level1Active: 0,
      level23Active: 0
    }
    referralLastUpdated.value = null
    referralError.value = null
    
    console.log('🧹 Данные пользователя, стейкинга и рефералов очищены')
  }
  
  return {
    // Состояние пользователя
    userData,
    isLoading,
    isInitialized,
    lastUpdated,
    error,
    
    // Состояние стейкинга
    stakeData,
    isStakeLoading,
    stakeLastUpdated,
    stakeError,
    
    // Состояние рефералов
    referralData,
    isReferralLoading,
    referralLastUpdated,
    referralError,
    
    // Вычисляемые свойства пользователя
    hasUserData,
    balance,
    stakeBalance,
    profitAll,
    partnersBalance,
    userInfo,
    xpInfo,
    
    // Вычисляемые свойства стейкинга
    hasActiveStake,
    canInvest,
    canCollect,
    availableTariff,
    canUpgradeTariff,
    formattedStakeBalance,
    formattedAccumulatedProfit,
    
    // Методы
    initialize,
    fetchUserData,
    fetchStakeData,
    fetchReferralData,
    updateStakeData,
    refreshUserData,
    startAutoUpdate,
    stopAutoUpdate,
    clearUserData,
    createUserIfNotExists
  }
})







