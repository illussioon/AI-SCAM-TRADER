import { ref } from 'vue'
import { useApi } from './useApi.js'
import { useTelegramStore } from '../stores/telegram.js'

export function usePayHistory() {
  const api = useApi()
  const telegramStore = useTelegramStore()
  
  // State
  const transactions = ref([])
  const isLoading = ref(false)
  const error = ref(null)
  const totalCount = ref(0)
  const hasMore = ref(false)
  
  /**
   * Получает Telegram ID из всех возможных источников
   */
  const getTelegramId = () => {
    const id = telegramStore.userId || 
           telegramStore.user?.id || 
           telegramStore.initDataUnsafe?.user?.id
    console.log('🔍 [PAY-HISTORY] getTelegramId вернул:', id)
    return id
  }
  
  /**
   * Загрузка истории транзакций
   */
  const loadTransactions = async (limit = 20, offset = 0) => {
    console.log('🔍 [PAY-HISTORY] Начало loadTransactions')
    console.log('🔍 [PAY-HISTORY] limit:', limit, 'offset:', offset)
    
    try {
      isLoading.value = true
      error.value = null
      
      const telegramId = getTelegramId()
      
      if (!telegramId) {
        console.error('❌ [PAY-HISTORY] Telegram ID не найден!')
        error.value = 'Telegram ID не найден'
        isLoading.value = false
        return []
      }
      
      const url = `/api/money-log/history?telegram_id=${telegramId}&limit=${limit}&offset=${offset}`
      console.log(`📊 [PAY-HISTORY] Загрузка истории транзакций`)
      console.log(`🔗 [PAY-HISTORY] Полный URL:`, url)
      console.log(`🆔 [PAY-HISTORY] Telegram ID:`, telegramId)
      
      const response = await api.get(url)
      
      console.log('📥 [PAY-HISTORY] Ответ от API:', JSON.stringify(response, null, 2))
      
      if (response.success && response.data) {
        transactions.value = response.data.logs || []
        totalCount.value = response.data.total_count || 0
        hasMore.value = response.data.has_more || false
        
        console.log(`✅ [PAY-HISTORY] Загружено ${transactions.value.length} транзакций из ${totalCount.value}`)
        console.log(`📋 [PAY-HISTORY] Транзакции:`, JSON.stringify(transactions.value, null, 2))
        return transactions.value
      } else {
        console.warn('⚠️ [PAY-HISTORY] Неуспешный ответ:', response)
        transactions.value = []
        totalCount.value = 0
        hasMore.value = false
        return []
      }
      
    } catch (err) {
      console.error('❌ [PAY-HISTORY] Ошибка загрузки истории транзакций:', err)
      console.error('❌ [PAY-HISTORY] Тип ошибки:', err.constructor.name)
      console.error('❌ [PAY-HISTORY] Сообщение:', err.message)
      if (err.stack) console.error('❌ [PAY-HISTORY] Stack:', err.stack)
      error.value = err.message || 'Ошибка загрузки истории'
      transactions.value = []
      totalCount.value = 0
      hasMore.value = false
      return []
    } finally {
      isLoading.value = false
      console.log('🏁 [PAY-HISTORY] loadTransactions завершен')
      console.log('🏁 [PAY-HISTORY] Итоговое состояние: transactions.length =', transactions.value.length, 'isLoading =', isLoading.value)
    }
  }
  
  /**
   * Фильтрация транзакций по типу
   */
  const filterTransactions = (type) => {
    if (type === 'all') {
      return transactions.value
    } else if (type === 'deposit') {
      // Пополнения: dep, dep_stake, dep_ref, stake_profit
      return transactions.value.filter(t => 
        ['dep', 'dep_stake', 'dep_ref', 'stake_profit'].includes(t.action)
      )
    } else if (type === 'withdrawal') {
      // Выводы: withdraw, withdraw_stake
      return transactions.value.filter(t => 
        ['withdraw', 'withdraw_stake'].includes(t.action)
      )
    }
    return transactions.value
  }
  
  /**
   * Форматирование суммы
   */
  const formatAmount = (amount) => {
    const num = Math.abs(parseFloat(amount) || 0)
    return num.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  }
  
  /**
   * Форматирование даты
   */
  const formatDate = (dateString) => {
    if (!dateString) return ''
    
    const date = new Date(dateString)
    const now = new Date()
    const diffMs = now - date
    const diffMins = Math.floor(diffMs / 60000)
    const diffHours = Math.floor(diffMs / 3600000)
    const diffDays = Math.floor(diffMs / 86400000)
    
    if (diffMins < 1) return 'Только что'
    if (diffMins < 60) return `${diffMins} мин. назад`
    if (diffHours < 24) return `${diffHours} ч. назад`
    if (diffDays < 7) return `${diffDays} дн. назад`
    
    return date.toLocaleDateString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }
  
  return {
    // State
    transactions,
    isLoading,
    error,
    totalCount,
    hasMore,
    
    // Methods
    loadTransactions,
    filterTransactions,
    formatAmount,
    formatDate,
    getTelegramId
  }
}

export default usePayHistory

