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
   * Инициализирует автоматическое обновление данных
   */
  const startAutoUpdate = (intervalMs = 30000) => {
    // Очищаем предыдущий интервал, если есть
    stopAutoUpdate()
    
    console.log(`🔄 Запуск автоматического обновления каждые ${intervalMs/1000} секунд`)
    
    updateInterval = setInterval(async () => {
      if (!isLoading.value) {
        console.log('🔄 Автоматическое обновление данных пользователя...')
        await fetchUserData()
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
        // Небольшая задержка для инициализации telegram
        await new Promise(resolve => setTimeout(resolve, 1000))
      }
      
      // Получаем начальные данные
      await fetchUserData()
      
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
    console.log('🔄 Принудительное обновление данных пользователя...')
    await fetchUserData()
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
    console.log('🧹 Данные пользователя очищены')
  }
  
  return {
    // Состояние
    userData,
    isLoading,
    isInitialized,
    lastUpdated,
    error,
    
    // Вычисляемые свойства
    hasUserData,
    balance,
    stakeBalance,
    profitAll,
    partnersBalance,
    userInfo,
    xpInfo,
    
    // Методы
    initialize,
    fetchUserData,
    refreshUserData,
    startAutoUpdate,
    stopAutoUpdate,
    clearUserData,
    createUserIfNotExists
  }
})






