/**
 * API Configuration
 * Централизованная конфигурация для API эндпоинтов
 */

// Определяем базовый URL для API
const getApiDomain = () => {
  // В продакшене можно будет изменить на внешний домен
  const isDevelopment = import.meta.env.DEV || window.location.hostname === 'localhost'
  
  if (isDevelopment) {
    // Для разработки используем localhost
    return 'http://127.0.0.1:8000'
  } else {
    // Для продакшена можно указать реальный домен
    return window.location.origin
  }
}

// Экспортируем конфигурацию API
export const API_CONFIG = {
  // Базовый домен API
  DOMAIN: getApiDomain(),
  
  // Основные эндпоинты
  ENDPOINTS: {
    STATUS: '/api/status',
    DEBUG_FILES: '/debug/files',
    ONLINE: '/api/online',
    // Пользователи
    USER_CREATE: '/api/user/create',
    USER_STATS: '/api/stats/my',
    USER_BY_ID: '/api/user',
    // Реферальная система
    REFERRAL_STATS: '/api/referral/stats',
    REFERRAL_LINK: '/api/referral/link',
    REFERRAL_LIST: '/api/referral/list',
    // Тестирование БД
    DATABASE_TEST: '/api/database/test',
    // Другие эндпоинты
    USER: '/api/user',
    WALLET: '/api/wallet',
    TRANSACTIONS: '/api/transactions'
  }
}

// Утилита для построения полного URL
export const buildApiUrl = (endpoint) => {
  return `${API_CONFIG.DOMAIN}${endpoint}`
}

// Готовые URL для частого использования
export const API_URLS = {
  STATUS: buildApiUrl(API_CONFIG.ENDPOINTS.STATUS),
  DEBUG_FILES: buildApiUrl(API_CONFIG.ENDPOINTS.DEBUG_FILES),
  ONLINE: buildApiUrl(API_CONFIG.ENDPOINTS.ONLINE),
  // Пользователи
  USER_CREATE: buildApiUrl(API_CONFIG.ENDPOINTS.USER_CREATE),
  USER_STATS: buildApiUrl(API_CONFIG.ENDPOINTS.USER_STATS),
  USER_BY_ID: buildApiUrl(API_CONFIG.ENDPOINTS.USER_BY_ID),
  // Реферальная система
  REFERRAL_STATS: buildApiUrl(API_CONFIG.ENDPOINTS.REFERRAL_STATS),
  REFERRAL_LINK: buildApiUrl(API_CONFIG.ENDPOINTS.REFERRAL_LINK),
  REFERRAL_LIST: buildApiUrl(API_CONFIG.ENDPOINTS.REFERRAL_LIST),
  // Тестирование
  DATABASE_TEST: buildApiUrl(API_CONFIG.ENDPOINTS.DATABASE_TEST),
  // Другие
  USER: buildApiUrl(API_CONFIG.ENDPOINTS.USER),
  WALLET: buildApiUrl(API_CONFIG.ENDPOINTS.WALLET),
  TRANSACTIONS: buildApiUrl(API_CONFIG.ENDPOINTS.TRANSACTIONS)
}

// Экспорт для обратной совместимости
export default API_CONFIG
