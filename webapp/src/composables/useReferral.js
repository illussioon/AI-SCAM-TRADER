/**
 * Композабл для работы с реферальной системой
 * Предоставляет функциональность для работы с реферальными ссылками и статистикой
 */

import { ref, computed } from 'vue'
import { useTelegramStore } from '../stores/telegram.js'
import { useApi } from './useApi.js'
import WebApp from '@twa-dev/sdk'

export function useReferral() {
  const telegramStore = useTelegramStore()
  const api = useApi()
  
  // Реактивные данные
  const referralData = ref({
    link: '',
    partnersCount: 0,
    totalEarnings: 0,
    referralsList: []
  })
  
  const isLoading = ref(false)
  const error = ref(null)
  
  // Вычисляемые свойства
  const formattedEarnings = computed(() => {
    return referralData.value.totalEarnings.toLocaleString('ru-RU', {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  })
  
  const hasReferrals = computed(() => {
    return referralData.value.partnersCount > 0
  })
  
  /**
   * Генерирует реферальную ссылку локально (fallback)
   */
  const generateReferralLinkLocal = (telegramId, botUsername = 'RoyallAppBot') => {
    return `https://t.me/${botUsername}?start=ref_${telegramId}`
  }

  /**
   * Загружает данные реферальной системы
   */
  const loadReferralData = async () => {
    try {
      isLoading.value = true
      error.value = null
      
      // Пытаемся получить Telegram ID из всех возможных источников
      const telegramId = telegramStore.userId || 
                        telegramStore.user?.id || 
                        telegramStore.initDataUnsafe?.user?.id
      
      console.log('🔍 Поиск Telegram ID:')
      console.log('  - telegramStore.userId:', telegramStore.userId)
      console.log('  - telegramStore.user?.id:', telegramStore.user?.id)
      console.log('  - telegramStore.initDataUnsafe?.user?.id:', telegramStore.initDataUnsafe?.user?.id)
      console.log('  - Итоговый ID:', telegramId)
      console.log('🔍 Telegram Store полное состояние:', {
        isInitialized: telegramStore.isInitialized,
        userId: telegramStore.userId,
        user: telegramStore.user,
        initData: telegramStore.initData,
        initDataUnsafe: telegramStore.initDataUnsafe
      })
      
      if (!telegramId) {
        // Пытаемся получить ID из разных источников
        const fallbackId = telegramStore.user?.id || 
                          telegramStore.initDataUnsafe?.user?.id ||
                          123456789 // Тестовый ID для разработки
        
        console.log('⚠️ Telegram ID не найден, используем fallback:', fallbackId)
        
        // Генерируем ссылку локально
        referralData.value.link = generateReferralLinkLocal(fallbackId)
        referralData.value.partnersCount = 0
        referralData.value.totalEarnings = 0
        
        console.log('🔗 Сгенерирована fallback ссылка:', referralData.value.link)
        return
      }
      
      // Сначала генерируем ссылку локально (быстро)
      referralData.value.link = generateReferralLinkLocal(telegramId)
      console.log('🔗 Локально сгенерированная ссылка:', referralData.value.link)
      
      // Затем пытаемся загрузить данные через API
      try {
        console.log('📡 Загрузка данных через API...')
        
        // Параллельно загружаем ссылку и статистику
        const [linkResponse, statsResponse] = await Promise.all([
          api.getReferralLink(telegramId).catch(err => {
            console.warn('⚠️ Ошибка API getReferralLink:', err)
            return { success: false, error: err.message }
          }),
          api.getReferralStats(telegramId).catch(err => {
            console.warn('⚠️ Ошибка API getReferralStats:', err)
            return { success: false, error: err.message }
          })
        ])
        
        console.log('📡 API ответы:', { linkResponse, statsResponse })
        
        // Обновляем ссылку только если API вернул успешный ответ
        if (linkResponse.success && linkResponse.data?.referral_link) {
          referralData.value.link = linkResponse.data.referral_link
          console.log('✅ Ссылка обновлена из API:', referralData.value.link)
        } else {
          console.log('ℹ️ Используем локально сгенерированную ссылку')
        }
        
        // Обновляем статистику если API вернул данные
        if (statsResponse.success && statsResponse.data) {
          referralData.value.partnersCount = statsResponse.data.partners_count || 0
          referralData.value.totalEarnings = statsResponse.data.total_earnings || 0
          console.log('✅ Статистика обновлена из API:', {
            partners: referralData.value.partnersCount,
            earnings: referralData.value.totalEarnings
          })
        } else {
          console.log('ℹ️ Статистика недоступна, используем значения по умолчанию')
          referralData.value.partnersCount = 0
          referralData.value.totalEarnings = 0
        }
        
      } catch (apiError) {
        console.warn('⚠️ API недоступен, используем локальные данные:', apiError)
        // Ссылка уже сгенерирована локально, просто устанавливаем дефолтные значения
        referralData.value.partnersCount = 0
        referralData.value.totalEarnings = 0
      }
      
      console.log('✅ Финальные реферальные данные:', referralData.value)
      
    } catch (err) {
      console.error('❌ Критическая ошибка загрузки реферальных данных:', err)
      error.value = err.message || 'Ошибка загрузки данных'
      
      // В крайнем случае устанавливаем базовые значения
      if (!referralData.value.link) {
        const fallbackId = telegramStore.userId || 
                          telegramStore.user?.id || 
                          telegramStore.initDataUnsafe?.user?.id ||
                          123456789
        referralData.value.link = generateReferralLinkLocal(fallbackId)
      }
      referralData.value.partnersCount = 0
      referralData.value.totalEarnings = 0
      
    } finally {
      isLoading.value = false
    }
  }
  
  /**
   * Загружает список рефералов
   */
  const loadReferralsList = async (limit = 50, offset = 0) => {
    try {
      const telegramId = telegramStore.userId
      if (!telegramId) {
        throw new Error('Telegram ID не найден')
      }
      
      const response = await api.getReferralList(telegramId, limit, offset)
      
      if (response.success) {
        referralData.value.referralsList = response.data.referrals
        console.log('✅ Список рефералов загружен:', response.data.referrals.length)
        return response.data
      } else {
        throw new Error(response.message || 'Ошибка загрузки списка рефералов')
      }
      
    } catch (err) {
      console.error('❌ Ошибка загрузки списка рефералов:', err)
      error.value = err.message || 'Ошибка загрузки списка рефералов'
      return null
    }
  }
  
  /**
   * Поделиться реферальной ссылкой через Telegram WebApp
   */
  const shareReferralLink = () => {
    try {
      const shareText = `🚀 Присоединяйся к Royal APL!\n\n💰 Торгуй криптовалютой и зарабатывай вместе со мной!\n\n🔗 Переходи по ссылке: ${referralData.value.link}`
      
      // Используем Telegram WebApp API
      if (WebApp.isExpanded) {
        if (WebApp.openTelegramLink) {
          const shareUrl = `https://t.me/share/url?url=${encodeURIComponent(referralData.value.link)}&text=${encodeURIComponent('🚀 Присоединяйся к Royal APL! 💰 Торгуй криптовалютой и зарабатывай вместе со мной!')}`
          WebApp.openTelegramLink(shareUrl)
        } else {
          // Fallback - копируем в буфер обмена
          copyToClipboard(shareText)
          telegramStore.showAlert('Текст скопирован! Отправьте его друзьям в Telegram.')
        }
      } else {
        // Fallback для браузера
        copyToClipboard(shareText)
        alert('Текст с реферальной ссылкой скопирован в буфер обмена!')
      }
      
      console.log('📤 Поделиться реферальной ссылкой')
      
    } catch (err) {
      console.error('❌ Ошибка при отправке реферальной ссылки:', err)
      telegramStore.showAlert('Произошла ошибка при отправке ссылки')
    }
  }
  
  /**
   * Копирует реферальную ссылку в буфер обмена
   */
  const copyReferralLink = async () => {
    try {
      await copyToClipboard(referralData.value.link)
      
      // Показываем уведомление
      if (telegramStore.isInitialized) {
        telegramStore.showAlert('Реферальная ссылка скопирована!')
        telegramStore.hapticFeedback('light')
      } else {
        alert('Реферальная ссылка скопирована!')
      }
      
      console.log('📋 Реферальная ссылка скопирована')
      
    } catch (err) {
      console.error('❌ Ошибка копирования ссылки:', err)
      telegramStore.showAlert('Не удалось скопировать ссылку')
    }
  }
  
  /**
   * Отправляет индивидуальное приглашение через Telegram
   */
  const sendPersonalInvite = (contactName = '') => {
    try {
      const personalText = contactName 
        ? `Привет, ${contactName}! 🚀 Присоединяйся к Royal APL!\n\n💰 Торгуй криптовалютой и зарабатывай вместе со мной!\n\n🔗 Переходи по ссылке: ${referralData.value.link}`
        : `Привет! 🚀 Присоединяйся к Royal APL!\n\n💰 Торгуй криптовалютой и зарабатывай вместе со мной!\n\n🔗 Переходи по ссылке: ${referralData.value.link}`
      
      // Используем Telegram API для отправки сообщения
      if (WebApp.openTelegramLink) {
        const shareUrl = `https://t.me/share/url?url=${encodeURIComponent(referralData.value.link)}&text=${encodeURIComponent(personalText)}`
        WebApp.openTelegramLink(shareUrl)
      } else {
        copyToClipboard(personalText)
        telegramStore.showAlert('Личное приглашение скопировано!')
      }
      
    } catch (err) {
      console.error('❌ Ошибка отправки личного приглашения:', err)
      telegramStore.showAlert('Произошла ошибка при отправке приглашения')
    }
  }
  
  /**
   * Вспомогательная функция для копирования в буфер обмена
   */
  const copyToClipboard = async (text) => {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text)
    } else {
      // Fallback для старых браузеров
      const textArea = document.createElement('textarea')
      textArea.value = text
      textArea.style.position = 'fixed'
      textArea.style.left = '-999999px'
      textArea.style.top = '-999999px'
      document.body.appendChild(textArea)
      textArea.focus()
      textArea.select()
      document.execCommand('copy')
      textArea.remove()
    }
  }
  
  /**
   * Форматирует дату присоединения реферала
   */
  const formatJoinDate = (dateString) => {
    if (!dateString) return 'Неизвестно'
    
    try {
      const date = new Date(dateString)
      return date.toLocaleDateString('ru-RU', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric'
      })
    } catch (err) {
      return 'Неизвестно'
    }
  }
  
  /**
   * Получает статистику реферальной программы
   */
  const getReferralStats = () => {
    return {
      totalReferrals: referralData.value.partnersCount,
      totalEarnings: referralData.value.totalEarnings,
      averageEarningsPerReferral: referralData.value.partnersCount > 0 
        ? (referralData.value.totalEarnings / referralData.value.partnersCount).toFixed(2)
        : '0.00',
      hasActiveReferrals: hasReferrals.value
    }
  }
  
  /**
   * Принудительно обновляет данные
   */
  const refreshReferralData = async () => {
    console.log('🔄 Принудительное обновление реферальных данных...')
    await loadReferralData()
  }

  /**
   * Получает текущую реферальную ссылку (с обновлением при необходимости)
   */
  const getCurrentReferralLink = () => {
    if (!referralData.value.link) {
      const telegramId = telegramStore.userId || 
                        telegramStore.user?.id || 
                        telegramStore.initDataUnsafe?.user?.id ||
                        123456789
      referralData.value.link = generateReferralLinkLocal(telegramId)
    }
    return referralData.value.link
  }

  return {
    // Данные
    referralData,
    isLoading,
    error,
    
    // Вычисляемые свойства
    formattedEarnings,
    hasReferrals,
    
    // Методы загрузки данных
    loadReferralData,
    loadReferralsList,
    refreshReferralData,
    
    // Методы для работы с ссылками
    shareReferralLink,
    copyReferralLink,
    sendPersonalInvite,
    getCurrentReferralLink,
    
    // Утилиты
    formatJoinDate,
    getReferralStats,
    copyToClipboard,
    generateReferralLinkLocal
  }
}

export default useReferral
