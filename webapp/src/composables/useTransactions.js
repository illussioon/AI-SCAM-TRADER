import { ref, computed, onMounted, onUnmounted } from 'vue';
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000';

// Глобальное состояние для live транзакций
const liveTransactions = ref([]);
const isLoading = ref(false);
const error = ref(null);
const lastUpdateTime = ref(null);

// Интервал для автообновления
let refreshInterval = null;

/**
 * Composable для работы с live транзакциями
 */
export function useTransactions() {
  
  /**
   * Получение последних транзакций с сервера
   * @param {number} limit - Количество транзакций для получения
   */
  const fetchLiveTransactions = async (limit = 5) => {
    if (isLoading.value) return; // Предотвращаем множественные запросы
    
    isLoading.value = true;
    error.value = null;
    
    try {
      console.log('🔄 Получение live транзакций...');
      
      const response = await axios.get(`${API_BASE_URL}/api/transactions/live`, {
        params: { limit },
        timeout: 5000
      });
      
      if (response.data && response.data.success) {
        const newTransactions = response.data.data || [];
        
        console.log(`✅ Получено ${newTransactions.length} транзакций`);
        
        // Обновляем список транзакций
        liveTransactions.value = newTransactions;
        lastUpdateTime.value = new Date();
        
        return {
          success: true,
          data: newTransactions,
          count: newTransactions.length
        };
      } else {
        throw new Error(response.data?.message || 'Ошибка получения транзакций');
      }
      
    } catch (err) {
      console.error('❌ Ошибка получения live транзакций:', err);
      
      let errorMessage = 'Ошибка получения транзакций';
      
      if (err.response) {
        errorMessage = err.response.data?.message || `HTTP ${err.response.status}`;
      } else if (err.request) {
        errorMessage = 'Нет ответа от сервера';
      } else {
        errorMessage = err.message;
      }
      
      error.value = errorMessage;
      
      return {
        success: false,
        error: errorMessage,
        data: []
      };
      
    } finally {
      isLoading.value = false;
    }
  };

  /**
   * Получение статистики транзакций
   */
  const fetchTransactionStats = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/api/transactions/stats`, {
        timeout: 5000
      });
      
      if (response.data && response.data.success) {
        return response.data.data;
      } else {
        throw new Error(response.data?.message || 'Ошибка получения статистики');
      }
      
    } catch (err) {
      console.error('❌ Ошибка получения статистики транзакций:', err);
      return null;
    }
  };

  /**
   * Запуск автообновления транзакций
   * @param {number} intervalMs - Интервал обновления в миллисекундах (по умолчанию 10 секунд)
   */
  const startAutoRefresh = (intervalMs = 10000) => {
    console.log(`🔄 Запуск автообновления транзакций каждые ${intervalMs / 1000} секунд`);
    
    // Сначала получаем данные
    fetchLiveTransactions();
    
    // Затем запускаем интервал
    refreshInterval = setInterval(() => {
      fetchLiveTransactions();
    }, intervalMs);
  };

  /**
   * Остановка автообновления
   */
  const stopAutoRefresh = () => {
    if (refreshInterval) {
      console.log('⏹️ Остановка автообновления транзакций');
      clearInterval(refreshInterval);
      refreshInterval = null;
    }
  };

  /**
   * Добавление новой транзакции (для тестирования)
   * @param {Object} transaction - Данные транзакции
   */
  const addTransaction = (transaction) => {
    const newTransaction = {
      id: `test_${Date.now()}`,
      time: new Date().toLocaleTimeString('ru-RU', { 
        hour: '2-digit', 
        minute: '2-digit', 
        second: '2-digit' 
      }),
      timestamp: Date.now() / 1000,
      ...transaction
    };
    
    // Добавляем в начало списка
    liveTransactions.value.unshift(newTransaction);
    
    // Ограничиваем количество транзакций
    if (liveTransactions.value.length > 50) {
      liveTransactions.value = liveTransactions.value.slice(0, 50);
    }
    
    console.log('➕ Добавлена новая транзакция:', newTransaction);
  };

  /**
   * Фильтрация транзакций по типу
   * @param {string} type - Тип транзакции ('deposit', 'withdrawal', 'all')
   */
  const getTransactionsByType = (type = 'all') => {
    if (type === 'all') {
      return liveTransactions.value;
    }
    
    return liveTransactions.value.filter(transaction => transaction.type === type);
  };

  /**
   * Получение последней транзакции
   */
  const getLatestTransaction = () => {
    return liveTransactions.value[0] || null;
  };

  // Вычисляемые свойства
  const transactionCount = computed(() => liveTransactions.value.length);
  const depositCount = computed(() => 
    liveTransactions.value.filter(t => t.type === 'deposit').length
  );
  const withdrawalCount = computed(() => 
    liveTransactions.value.filter(t => t.type === 'withdrawal').length
  );

  // Форматированное время последнего обновления
  const lastUpdateFormatted = computed(() => {
    if (!lastUpdateTime.value) return null;
    
    return lastUpdateTime.value.toLocaleTimeString('ru-RU', {
      hour: '2-digit',
      minute: '2-digit', 
      second: '2-digit'
    });
  });

  // Проверка, давно ли были обновлены данные
  const isDataStale = computed(() => {
    if (!lastUpdateTime.value) return true;
    
    const now = new Date();
    const diffMinutes = (now - lastUpdateTime.value) / (1000 * 60);
    
    return diffMinutes > 2; // Считаем данные устаревшими, если прошло > 2 минут
  });

  return {
    // Состояние
    liveTransactions,
    isLoading,
    error,
    lastUpdateTime,
    
    // Вычисляемые значения
    transactionCount,
    depositCount, 
    withdrawalCount,
    lastUpdateFormatted,
    isDataStale,
    
    // Методы
    fetchLiveTransactions,
    fetchTransactionStats,
    startAutoRefresh,
    stopAutoRefresh,
    addTransaction,
    getTransactionsByType,
    getLatestTransaction
  };
}

/**
 * Функция для создания тестовых транзакций (для разработки)
 */
export function createTestTransaction(type = 'deposit') {
  const cryptoOptions = [
    { name: 'TON', icon: '/icon/ton.svg', color: 'rgb(0, 176, 219)' },
    { name: 'ETH', icon: '/icon/eth.svg', color: 'rgb(17, 192, 167)' },
    { name: 'BTC', icon: '/icon/btc.svg', color: 'rgb(247, 147, 26)' },
    { name: 'USDT', icon: '/icon/teher.webp', color: 'rgb(115, 93, 237)' },
    { name: 'СБП', icon: '/icon/sbp2.svg', color: 'rgb(0, 176, 219)' }
  ];
  
  const crypto = cryptoOptions[Math.floor(Math.random() * cryptoOptions.length)];
  const amount = Math.floor(Math.random() * 5000) + 100; // От 100 до 5100₽
  
  return {
    type: type,
    typeText: type === 'deposit' ? 'Пополнение' : 'Вывод средств',
    borderColor: crypto.color,
    cryptoName: crypto.name,
    cryptoClass: '',
    cryptoIcon: crypto.icon,
    amount: `${type === 'deposit' ? '+' : '-'}${amount}₽`,
    username: `user${Math.floor(Math.random() * 1000)}`,
    telegram_id: Math.floor(Math.random() * 1000000)
  };
}
