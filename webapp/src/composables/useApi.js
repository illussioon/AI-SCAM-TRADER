/**
 * Composable для работы с API
 * Удобный доступ к API конфигурации в Composition API
 */

import { getCurrentInstance } from 'vue'
import { API_CONFIG, API_URLS, buildApiUrl } from '../config/api.js'

/**
 * Композабл для работы с API
 * @returns {Object} API утилиты и конфигурация
 */
export function useApi() {
  // Получаем экземпляр приложения (для Options API совместимости)
  const instance = getCurrentInstance()
  
  /**
   * Выполняет HTTP запрос к API
   * @param {string} endpoint - Путь к эндпоинту
   * @param {Object} options - Опции для fetch
   * @returns {Promise} Результат запроса
   */
  const apiRequest = async (endpoint, options = {}) => {
    const url = buildApiUrl(endpoint)
    
    const defaultOptions = {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers
      },
      ...options
    }
    
    try {
      const response = await fetch(url, defaultOptions)
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }
      
      // Пытаемся парсить JSON, если не получается - возвращаем текст
      const contentType = response.headers.get('content-type')
      if (contentType && contentType.includes('application/json')) {
        return await response.json()
      } else {
        return await response.text()
      }
    } catch (error) {
      console.error('API Request Error:', error)
      throw error
    }
  }
  
  /**
   * GET запрос
   * @param {string} endpoint - Путь к эндпоинту
   * @param {Object} options - Дополнительные опции
   */
  const get = (endpoint, options = {}) => {
    return apiRequest(endpoint, { ...options, method: 'GET' })
  }
  
  /**
   * POST запрос
   * @param {string} endpoint - Путь к эндпоинту
   * @param {Object} data - Данные для отправки
   * @param {Object} options - Дополнительные опции
   */
  const post = (endpoint, data = null, options = {}) => {
    return apiRequest(endpoint, {
      ...options,
      method: 'POST',
      body: data ? JSON.stringify(data) : null
    })
  }
  
  /**
   * PUT запрос
   * @param {string} endpoint - Путь к эндпоинту
   * @param {Object} data - Данные для отправки
   * @param {Object} options - Дополнительные опции
   */
  const put = (endpoint, data = null, options = {}) => {
    return apiRequest(endpoint, {
      ...options,
      method: 'PUT',
      body: data ? JSON.stringify(data) : null
    })
  }
  
  /**
   * DELETE запрос
   * @param {string} endpoint - Путь к эндпоинту
   * @param {Object} options - Дополнительные опции
   */
  const del = (endpoint, options = {}) => {
    return apiRequest(endpoint, { ...options, method: 'DELETE' })
  }
  
  return {
    // Конфигурация
    domain: API_CONFIG.DOMAIN,
    urls: API_URLS,
    config: API_CONFIG,
    
    // Утилиты
    buildUrl: buildApiUrl,
    
    // HTTP методы
    request: apiRequest,
    get,
    post,
    put,
    delete: del,
    
    // Быстрые методы для частых запросов
    checkStatus: () => get(API_CONFIG.ENDPOINTS.STATUS),
    getDebugFiles: () => get(API_CONFIG.ENDPOINTS.DEBUG_FILES),
    getOnline: () => get(API_CONFIG.ENDPOINTS.ONLINE),
    
    // Методы для работы с пользователями
    createUser: (userData) => post(API_CONFIG.ENDPOINTS.USER_CREATE, userData),
    getUserStats: (telegramId) => get(`${API_CONFIG.ENDPOINTS.USER_STATS}?telegram_id=${telegramId}`),
    getUserById: (telegramId) => get(`${API_CONFIG.ENDPOINTS.USER_BY_ID}/${telegramId}`),
    
    // Методы для работы с реферальной системой
    getReferralStats: (telegramId) => get(`${API_CONFIG.ENDPOINTS.REFERRAL_STATS}?telegram_id=${telegramId}`),
    getReferralLink: (telegramId) => get(`${API_CONFIG.ENDPOINTS.REFERRAL_LINK}?telegram_id=${telegramId}`),
    getReferralList: (telegramId, limit = 50, offset = 0) => get(`${API_CONFIG.ENDPOINTS.REFERRAL_LIST}?telegram_id=${telegramId}&limit=${limit}&offset=${offset}`),
    
    // Тестирование базы данных
    testDatabase: () => get(API_CONFIG.ENDPOINTS.DATABASE_TEST),
    
    // Методы для работы со стейкингом
    getStakeStats: (telegramId) => get(`/api/stake/stats?telegram_id=${telegramId}`),
    stakeInvest: (investmentData) => post('/api/stake/invest', investmentData),
    stakeCollect: (telegramId) => post(`/api/stake/collect?telegram_id=${telegramId}`),
    getAvailableTariffs: () => get('/api/stake/tariffs'),
    
    // Доступ к глобальному API (для совместимости)
    $api: instance?.appContext?.config?.globalProperties?.$api
  }
}
