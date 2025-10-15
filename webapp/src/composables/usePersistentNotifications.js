import { ref, reactive, computed, watch } from 'vue';

// Ключ для localStorage
const STORAGE_KEY = 'app_notifications';

// Глобальное состояние уведомлений
const notifications = ref([]);
const isInitialized = ref(false);

// Инициализация из localStorage
const initializeFromStorage = () => {
  if (isInitialized.value) return;
  
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) {
      const parsed = JSON.parse(stored);
      if (Array.isArray(parsed)) {
        notifications.value = parsed.filter(n => !n.isRead); // Показываем только непрочитанные
        console.log('📱 Загружено уведомлений из localStorage:', notifications.value.length);
      }
    }
  } catch (error) {
    console.error('❌ Ошибка загрузки уведомлений из localStorage:', error);
    notifications.value = [];
  }
  
  isInitialized.value = true;
};

// Сохранение в localStorage
const saveToStorage = () => {
  try {
    const allNotifications = [...notifications.value];
    localStorage.setItem(STORAGE_KEY, JSON.stringify(allNotifications));
    console.log('💾 Уведомления сохранены в localStorage:', allNotifications.length);
  } catch (error) {
    console.error('❌ Ошибка сохранения уведомлений в localStorage:', error);
  }
};

// Слежение за изменениями для автосохранения
watch(notifications, saveToStorage, { deep: true });

/**
 * Composable для работы с persistent уведомлениями
 */
export function usePersistentNotifications() {
  // Инициализация при первом использовании
  if (!isInitialized.value) {
    initializeFromStorage();
  }

  // Вычисляемые свойства
  const pendingNotifications = computed(() => 
    notifications.value.filter(n => !n.isRead)
  );

  const unreadCount = computed(() => pendingNotifications.value.length);

  /**
   * Создание нового уведомления
   * @param {Object} notification - объект уведомления
   * @param {string} notification.title - заголовок
   * @param {string} notification.message - сообщение  
   * @param {'success'|'error'|'info'|'warning'} notification.type - тип
   * @param {Object} [notification.details] - дополнительные детали
   * @param {boolean} [notification.persistent=true] - сохранять в localStorage
   * @param {boolean} [notification.autoClose] - автозакрытие
   */
  const addNotification = (notification) => {
    const newNotification = {
      id: `notification_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
      title: notification.title || 'Уведомление',
      message: notification.message || '',
      type: notification.type || 'info',
      details: notification.details || null,
      persistent: notification.persistent !== false, // По умолчанию true
      autoClose: notification.autoClose,
      timestamp: Date.now(),
      isRead: false,
      createdAt: new Date().toISOString()
    };

    console.log('🔔 Добавляем новое уведомление:', newNotification);
    
    // Добавляем в начало массива (новые уведомления сверху)
    notifications.value.unshift(newNotification);
    
    // Ограничиваем количество уведомлений (макс 20)
    if (notifications.value.length > 20) {
      notifications.value = notifications.value.slice(0, 20);
    }

    return newNotification.id;
  };

  /**
   * Пометить уведомление как прочитанное
   * @param {string} notificationId - ID уведомления
   */
  const markAsRead = (notificationId) => {
    const notification = notifications.value.find(n => n.id === notificationId);
    if (notification) {
      notification.isRead = true;
      notification.readAt = new Date().toISOString();
      console.log('✅ Уведомление помечено как прочитанное:', notificationId);
    }
  };

  /**
   * Получить текущее (первое непрочитанное) уведомление
   */
  const getCurrentNotification = () => {
    return pendingNotifications.value[0] || null;
  };

  /**
   * Удалить уведомление
   * @param {string} notificationId - ID уведомления
   */
  const removeNotification = (notificationId) => {
    const index = notifications.value.findIndex(n => n.id === notificationId);
    if (index !== -1) {
      notifications.value.splice(index, 1);
      console.log('🗑️ Уведомление удалено:', notificationId);
    }
  };

  /**
   * Очистить все уведомления
   */
  const clearAllNotifications = () => {
    notifications.value.forEach(n => n.isRead = true);
    console.log('🧹 Все уведомления помечены как прочитанные');
  };

  /**
   * Удалить все прочитанные уведомления
   */
  const removeReadNotifications = () => {
    const before = notifications.value.length;
    notifications.value = notifications.value.filter(n => !n.isRead);
    const after = notifications.value.length;
    console.log(`🗑️ Удалено прочитанных уведомлений: ${before - after}`);
  };

  /**
   * Добавить уведомление о пополнении баланса
   * @param {Object} data - данные о пополнении
   */
  const addDepositNotification = (data) => {
    const { status, amount, bonus_amount, total_amount, payment_type } = data;
    
    if (status === 'approved') {
      return addNotification({
        type: 'success',
        title: '✅ Пополнение подтверждено!',
        message: `Ваш баланс успешно пополнен через ${payment_type}`,
        details: {
          amount: amount,
          bonus: bonus_amount,
          total: total_amount
        },
        autoClose: false, // Не закрываем автоматически для важных уведомлений
        persistent: true
      });
    } else if (status === 'rejected') {
      return addNotification({
        type: 'error', 
        title: '❌ Пополнение отклонено',
        message: `Пополнение через ${payment_type} было отклонено администратором. Обратитесь в поддержку.`,
        details: {
          amount: amount
        },
        autoClose: false,
        persistent: true
      });
    }
  };

  /**
   * Добавить уведомление о реферальном бонусе
   * @param {Object} data - данные о бонусе
   */
  const addReferralBonusNotification = (data) => {
    const { amount, referral_username } = data;
    
    return addNotification({
      type: 'success',
      title: '💰 Реферальный бонус!',
      message: `Получен бонус от пополнения реферала @${referral_username}`,
      details: {
        bonus: amount,
        total: amount
      },
      autoClose: false,
      persistent: true
    });
  };

  /**
   * Проверить и обработать уведомления от API
   * Вызывается при загрузке приложения и периодически
   */
  const checkPendingNotifications = async () => {
    try {
      // Здесь можно добавить проверку API на новые уведомления
      // Например, проверить статус последних транзакций
      console.log('🔍 Проверка новых уведомлений...');
    } catch (error) {
      console.error('❌ Ошибка проверки уведомлений:', error);
    }
  };

  /**
   * Получить статистику уведомлений
   */
  const getNotificationStats = () => {
    const total = notifications.value.length;
    const unread = pendingNotifications.value.length;
    const read = total - unread;
    
    const byType = {
      success: notifications.value.filter(n => n.type === 'success').length,
      error: notifications.value.filter(n => n.type === 'error').length,
      info: notifications.value.filter(n => n.type === 'info').length,
      warning: notifications.value.filter(n => n.type === 'warning').length
    };

    return {
      total,
      unread,
      read,
      byType
    };
  };

  return {
    // Состояние
    notifications: notifications,
    pendingNotifications,
    unreadCount,
    
    // Методы
    addNotification,
    markAsRead,
    getCurrentNotification,
    removeNotification,
    clearAllNotifications,
    removeReadNotifications,
    
    // Специальные методы для приложения
    addDepositNotification,
    addReferralBonusNotification,
    checkPendingNotifications,
    
    // Утилиты
    getNotificationStats
  };
}
