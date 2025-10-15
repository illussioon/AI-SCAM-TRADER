import { ref, reactive } from 'vue';

// Глобальное состояние уведомлений
const notifications = ref([]);
let notificationId = 0;

/**
 * Composable для управления popup уведомлениями
 */
export function useNotifications() {
  
  /**
   * Добавить уведомление
   * @param {string} type - Тип уведомления: 'success', 'error', 'info', 'warning'
   * @param {string} title - Заголовок
   * @param {string} message - Сообщение
   * @param {number} duration - Длительность показа в мс (0 = бесконечно)
   * @returns {number} ID уведомления
   */
  const addNotification = (type, title, message, duration = 5000) => {
    const id = ++notificationId;
    
    const notification = reactive({
      id,
      type,
      title,
      message,
      duration,
      visible: true,
      createdAt: Date.now()
    });
    
    notifications.value.push(notification);
    
    // Автоматически удалить через duration
    if (duration > 0) {
      setTimeout(() => {
        removeNotification(id);
      }, duration);
    }
    
    return id;
  };
  
  /**
   * Удалить уведомление
   * @param {number} id - ID уведомления
   */
  const removeNotification = (id) => {
    const index = notifications.value.findIndex(n => n.id === id);
    if (index !== -1) {
      notifications.value[index].visible = false;
      
      // Удалить из массива через 300мс (время анимации)
      setTimeout(() => {
        const idx = notifications.value.findIndex(n => n.id === id);
        if (idx !== -1) {
          notifications.value.splice(idx, 1);
        }
      }, 300);
    }
  };
  
  /**
   * Показать уведомление об успехе
   * @param {string} title - Заголовок
   * @param {string} message - Сообщение
   * @param {number} duration - Длительность
   */
  const showSuccess = (title, message, duration = 5000) => {
    return addNotification('success', title, message, duration);
  };
  
  /**
   * Показать уведомление об ошибке
   * @param {string} title - Заголовок
   * @param {string} message - Сообщение
   * @param {number} duration - Длительность
   */
  const showError = (title, message, duration = 5000) => {
    return addNotification('error', title, message, duration);
  };
  
  /**
   * Показать информационное уведомление
   * @param {string} title - Заголовок
   * @param {string} message - Сообщение
   * @param {number} duration - Длительность
   */
  const showInfo = (title, message, duration = 5000) => {
    return addNotification('info', title, message, duration);
  };
  
  /**
   * Показать предупреждение
   * @param {string} title - Заголовок
   * @param {string} message - Сообщение
   * @param {number} duration - Длительность
   */
  const showWarning = (title, message, duration = 5000) => {
    return addNotification('warning', title, message, duration);
  };
  
  /**
   * Очистить все уведомления
   */
  const clearAll = () => {
    notifications.value.forEach(n => {
      n.visible = false;
    });
    
    setTimeout(() => {
      notifications.value = [];
    }, 300);
  };
  
  return {
    notifications,
    addNotification,
    removeNotification,
    showSuccess,
    showError,
    showInfo,
    showWarning,
    clearAll
  };
}

