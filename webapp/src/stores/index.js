import { createPinia } from 'pinia'

export const pinia = createPinia()

// Экспортируем все stores
export { useTelegramStore } from './telegram.js'
export { useUserStore } from './user.js'

