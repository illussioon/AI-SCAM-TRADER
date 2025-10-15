import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import WebApp from '@twa-dev/sdk'
import { useApi } from '../composables/useApi.js'

export const useTelegramStore = defineStore('telegram', () => {
  // API композабл
  const api = useApi()
  
  // Состояние
  const isInitialized = ref(false)
  const user = ref(null)
  const initData = ref(null)
  const initDataUnsafe = ref(null)
  
  // Вычисляемые свойства
  const userPhoto = computed(() => {
    if (user.value?.photo_url) {
      return user.value.photo_url
    }
    // Возвращаем дефолтную аватарку если фото не найдено
    return '/img/avatar.webp'
  })
  
  const userId = computed(() => {
    return user.value?.id || null
  })
  
  const firstName = computed(() => {
    return user.value?.first_name || 'Пользователь'
  })
  
  const lastName = computed(() => {
    return user.value?.last_name || ''
  })
  
  const fullName = computed(() => {
    return `${firstName.value} ${lastName.value}`.trim()
  })
  
  const username = computed(() => {
    return user.value?.username || null
  })
  
  // Методы
  const initialize = () => {
    try {
      console.log('🔄 Инициализация Telegram WebApp...')
      
      // Инициализируем WebApp
      WebApp.ready()
      
      // Расширяем приложение на весь экран
      WebApp.expand()
      
      // Получаем данные пользователя
      initData.value = WebApp.initData
      initDataUnsafe.value = WebApp.initDataUnsafe
      
      if (WebApp.initDataUnsafe?.user) {
        user.value = WebApp.initDataUnsafe.user
        console.log('👤 Данные пользователя получены:', user.value)
      } else {
        console.warn('⚠️ Данные пользователя не найдены, используем тестовые данные')
        // Тестовые данные для разработки
        user.value = {
          id: 851069605,
          first_name: 'Test',
          last_name: 'User',
          username: 'testuser',
          photo_url: null
        }
      }
      
      isInitialized.value = true
      
      // Настраиваем тему
      WebApp.setHeaderColor('#000000')
      WebApp.setBackgroundColor('#000000')
      
      console.log('✅ Telegram WebApp успешно инициализирован')
      
    } catch (error) {
      console.error('❌ Ошибка инициализации Telegram WebApp:', error)
      
      // В случае ошибки используем мок данные
      user.value = {
        id: 851069605,
        first_name: 'Test',
        last_name: 'User',
        username: 'testuser',
        photo_url: null
      }
      isInitialized.value = true
    }
  }
  
  const close = () => {
    WebApp.close()
  }
  
  const showAlert = (message) => {
    WebApp.showAlert(message)
  }
  
  const showConfirm = (message, callback) => {
    WebApp.showConfirm(message, callback)
  }
  
  const hapticFeedback = (type = 'light') => {
    WebApp.HapticFeedback.impactOccurred(type)
  }
  
  // Методы для работы с главной кнопкой
  const showMainButton = (text, callback) => {
    WebApp.MainButton.setText(text)
    WebApp.MainButton.onClick(callback)
    WebApp.MainButton.show()
  }
  
  const hideMainButton = () => {
    WebApp.MainButton.hide()
  }
  
  // API методы для работы с сервером
  const sendUserDataToServer = async () => {
    try {
      console.log('📤 Отправка данных пользователя на сервер...')
      
      const userData = {
        user_id: userId.value,
        first_name: firstName.value,
        last_name: lastName.value,
        username: username.value,
        photo_url: user.value?.photo_url || null,
        init_data: initData.value,
        timestamp: Date.now()
      }
      
      // Используем API композабл для отправки данных
      const response = await api.post('/api/user', userData)
      console.log('✅ Данные пользователя отправлены:', response)
      
      return response
    } catch (error) {
      console.error('❌ Ошибка отправки данных пользователя:', error)
      throw error
    }
  }
  
  const checkApiConnection = async () => {
    try {
      console.log('🔍 Проверка соединения с API...')
      console.log('🌐 API Domain:', api.domain)
      
      const status = await api.checkStatus()
      console.log('✅ API соединение установлено:', status)
      
      return status
    } catch (error) {
      console.error('❌ Ошибка соединения с API:', error)
      throw error
    }
  }
  
  const getUserBalanceFromServer = async () => {
    try {
      if (!userId.value) {
        throw new Error('User ID не найден')
      }
      
      console.log(`💰 Получение баланса для пользователя ${userId.value}...`)
      
      const balance = await api.get(`/api/user/${userId.value}/balance`)
      console.log('✅ Баланс получен:', balance)
      
      return balance
    } catch (error) {
      console.error('❌ Ошибка получения баланса:', error)
      throw error
    }
  }

  const getUserStatsFromServer = async () => {
    try {
      if (!userId.value) {
        throw new Error('User ID не найден')
      }
      
      console.log(`📊 Получение статистики для пользователя ${userId.value}...`)
      
      const stats = await api.getUserStats(userId.value)
      console.log('✅ Статистика получена:', stats)
      
      return stats
    } catch (error) {
      console.error('❌ Ошибка получения статистики:', error)
      throw error
    }
  }

  const createUserOnServer = async () => {
    try {
      if (!userId.value || !user.value) {
        throw new Error('Данные пользователя не найдены')
      }

      console.log(`👤 Создание пользователя ${username.value || `user_${userId.value}`}...`)

      const userData = {
        username: username.value || `user_${userId.value}`,
        telegram_id: userId.value,
        ref: null // Можно передать реферальный код, если есть
      }

      const result = await api.createUser(userData)
      console.log('✅ Пользователь создан/найден:', result)
      
      return result
    } catch (error) {
      console.error('❌ Ошибка создания пользователя:', error)
      throw error
    }
  }
  
  return {
    // Состояние
    isInitialized,
    user,
    initData,
    initDataUnsafe,
    
    // Вычисляемые свойства
    userPhoto,
    userId,
    firstName,
    lastName,
    fullName,
    username,
    
    // Методы
    initialize,
    close,
    showAlert,
    showConfirm,
    hapticFeedback,
    showMainButton,
    hideMainButton,
    
    // API методы
    sendUserDataToServer,
    checkApiConnection,
    getUserBalanceFromServer,
    getUserStatsFromServer,
    createUserOnServer,
    
    // API утилиты (для прямого доступа)
    apiDomain: api.domain,
    apiUrls: api.urls
  }
})
