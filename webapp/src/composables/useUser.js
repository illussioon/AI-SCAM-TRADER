/**
 * Композабл для работы с пользовательскими данными
 * Предоставляет удобный доступ к user store из любого компонента
 */

import { computed } from 'vue'
import { useUserStore } from '../stores/user.js'
import { storeToRefs } from 'pinia'

/**
 * Композабл для работы с пользователем
 * @returns {Object} Реактивные данные и методы пользователя
 */
export function useUser() {
  const userStore = useUserStore()
  
  // Извлекаем реактивные свойства из store
  const {
    userData,
    isLoading,
    isInitialized,
    lastUpdated,
    error,
    hasUserData,
    balance,
    stakeBalance,
    profitAll,
    partnersBalance,
    userInfo,
    xpInfo
  } = storeToRefs(userStore)
  
  // Методы из store (не нужно оборачивать в storeToRefs)
  const {
    initialize,
    fetchUserData,
    refreshUserData,
    startAutoUpdate,
    stopAutoUpdate,
    clearUserData,
    createUserIfNotExists
  } = userStore
  
  /**
   * Форматирует баланс для отображения
   * @param {string} value - Значение баланса
   * @returns {string} Отформатированный баланс
   */
  const formatBalance = (value) => {
    if (!value || value === '0.00') return '0.00'
    
    // Если это строка, парсим как число
    const numValue = typeof value === 'string' ? parseFloat(value) : value
    
    // Форматируем с двумя знаками после запятой
    return numValue.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  }
  
  /**
   * Форматированные балансы для отображения
   */
  const formattedBalances = {
    balance: computed(() => formatBalance(balance.value)),
    stakeBalance: computed(() => formatBalance(stakeBalance.value)),
    profitAll: computed(() => formatBalance(profitAll.value)),
    partnersBalance: computed(() => formatBalance(partnersBalance.value))
  }
  
  /**
   * Проверяет, загружены ли данные пользователя
   * @returns {boolean}
   */
  const isUserDataLoaded = () => {
    return hasUserData.value && !isLoading.value && !error.value
  }
  
  /**
   * Получает общий баланс пользователя
   * @returns {number}
   */
  const getTotalBalance = () => {
    if (!hasUserData.value) return 0
    
    const mainBalance = parseFloat(balance.value) || 0
    const stakeBalance = parseFloat(stakeBalance.value) || 0
    const partnersBalance = parseFloat(partnersBalance.value) || 0
    
    return mainBalance + stakeBalance + partnersBalance
  }
  
  /**
   * Получает информацию о прогрессе XP
   * @returns {Object}
   */
  const getXpProgress = () => {
    return xpInfo.value
  }
  
  /**
   * Проверяет, есть ли ошибка загрузки
   * @returns {boolean}
   */
  const hasError = () => {
    return !!error.value
  }
  
  /**
   * Получает текст ошибки
   * @returns {string|null}
   */
  const getErrorMessage = () => {
    return error.value
  }
  
  /**
   * Форматирует время последнего обновления
   * @returns {string}
   */
  const getLastUpdatedFormatted = () => {
    if (!lastUpdated.value) return 'Не обновлялось'
    
    return lastUpdated.value.toLocaleString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
      second: '2-digit'
    })
  }
  
  return {
    // Реактивные свойства
    userData,
    isLoading,
    isInitialized,
    lastUpdated,
    error,
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
    createUserIfNotExists,
    
    // Утилиты
    formatBalance,
    formattedBalances,
    isUserDataLoaded,
    getTotalBalance,
    getXpProgress,
    hasError,
    getErrorMessage,
    getLastUpdatedFormatted
  }
}

export default useUser
