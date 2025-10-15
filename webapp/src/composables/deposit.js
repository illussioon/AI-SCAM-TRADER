import { ref } from 'vue';
import axios from 'axios';
import { usePersistentNotifications } from './usePersistentNotifications';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

/**
 * Composable для работы с пополнением баланса
 */
export function useDeposit() {
  const isLoading = ref(false);
  const error = ref(null);
  const depositStatus = ref(null);
  
  // Система уведомлений
  const { addDepositNotification, addReferralBonusNotification } = usePersistentNotifications();

  /**
   * Создание запроса на пополнение баланса
   * @param {number} telegramId - ID пользователя в Telegram
   * @param {number} amount - Сумма пополнения
   * @param {string} paymentType - Тип оплаты (СБП, Карта и т.д.)
   * @param {object} paymentDetails - Детали платежа
   * @returns {Promise<object>} Результат создания запроса
   */
  const createDepositRequest = async (telegramId, amount, paymentType = 'СБП', paymentDetails = {}) => {
    isLoading.value = true;
    error.value = null;

    try {
      console.log('🚀 Создание запроса на пополнение:', {
        telegramId,
        amount,
        paymentType,
        paymentDetails,
        url: `${API_BASE_URL}/api/deposit/create`
      });

      const requestData = {
        telegram_id: parseInt(telegramId),
        amount: parseFloat(amount),
        payment_type: paymentType,
        payment_details: paymentDetails || {}
      };

      console.log('📤 Отправляем данные:', requestData);

      const response = await axios.post(`${API_BASE_URL}/api/deposit/create`, requestData, {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 10000 // 10 секунд таймаут
      });

      console.log('📥 Получен ответ:', response);

      if (response.data && response.data.success) {
        console.log('✅ Запрос на пополнение создан:', response.data);
        return response.data;
      } else {
        console.error('❌ Неуспешный ответ:', response.data);
        throw new Error(response.data?.message || 'Ошибка создания запроса');
      }
    } catch (err) {
      console.error('❌ Детальная ошибка создания запроса:', {
        message: err.message,
        response: err.response?.data,
        status: err.response?.status,
        config: err.config
      });
      
      let errorMessage = 'Неизвестная ошибка';
      
      if (err.response) {
        // Сервер ответил с ошибкой
        errorMessage = err.response.data?.detail || err.response.data?.message || `HTTP ${err.response.status}`;
      } else if (err.request) {
        // Запрос был отправлен, но ответа не получено
        errorMessage = 'Нет ответа от сервера. Проверьте подключение к интернету.';
      } else {
        // Ошибка в настройке запроса
        errorMessage = err.message;
      }
      
      error.value = errorMessage;
      throw new Error(errorMessage);
    } finally {
      isLoading.value = false;
    }
  };

  /**
   * Получение статуса запроса на пополнение
   * @param {number} requestId - ID запроса
   * @returns {Promise<object>} Статус запроса
   */
  const getDepositStatus = async (requestId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/deposit/status/${requestId}`);
      
      if (response.data.success) {
        depositStatus.value = response.data.data.status;
        return response.data.data;
      } else {
        throw new Error(response.data.message || 'Ошибка получения статуса');
      }
    } catch (err) {
      console.error('❌ Ошибка получения статуса пополнения:', err);
      error.value = err.response?.data?.detail || err.message || 'Неизвестная ошибка';
      throw err;
    }
  };

  /**
   * Проверка последнего запроса пользователя
   * @param {number} telegramId - ID пользователя в Telegram
   * @returns {Promise<object|null>} Последний запрос или null
   */
  const getLastDepositRequest = async (telegramId) => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/deposit/last/${telegramId}`);
      
      if (response.data.success) {
        return response.data.data;
      }
      return null;
    } catch (err) {
      console.error('❌ Ошибка получения последнего запроса:', err);
      return null;
    }
  };

  /**
   * Подписка на обновления статуса (для WebSocket/polling в будущем)
   * @param {number} requestId - ID запроса
   * @param {function} callback - Callback функция при изменении статуса
   */
  const subscribeToStatusUpdates = (requestId, callback) => {
    console.log('🔄 Начинаем отслеживание статуса запроса:', requestId);
    
    // Polling каждые 3 секунды
    const interval = setInterval(async () => {
      try {
        const status = await getDepositStatus(requestId);
        
        // Если статус изменился на approved или rejected, останавливаем polling
        if (status.status === 'approved' || status.status === 'rejected') {
          clearInterval(interval);
          
          console.log('🎯 Статус изменился:', status);
          
          // Создаем persistent уведомление
          addDepositNotification({
            status: status.status,
            amount: status.amount,
            bonus_amount: status.bonus_amount,
            total_amount: status.total_amount,
            payment_type: status.payment_type || 'СБП'
          });
          
          // Вызываем callback для совместимости
          if (callback) {
            callback(status);
          }
        }
      } catch (err) {
        console.error('Ошибка при проверке статуса:', err);
      }
    }, 3000);

    // Возвращаем функцию для отмены подписки
    return () => {
      console.log('⏹️ Отменяем отслеживание статуса для запроса:', requestId);
      clearInterval(interval);
    };
  };

  return {
    isLoading,
    error,
    depositStatus,
    createDepositRequest,
    getDepositStatus,
    getLastDepositRequest,
    subscribeToStatusUpdates
  };
}

