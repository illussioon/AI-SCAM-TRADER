<template>
  <teleport to="body">
    <!-- Оверлей -->
    <transition
      enter-active-class="duration-300 ease-out"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="duration-200 ease-in"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isVisible"
        class="fixed inset-0 bg-black bg-opacity-60 backdrop-blur-sm z-[9999] flex items-center justify-center p-4"
        @click="closePopup"
      >
        <!-- Popup контейнер -->
        <transition
          enter-active-class="duration-300 ease-out"
          enter-from-class="opacity-0 scale-95 translate-y-4"
          enter-to-class="opacity-100 scale-100 translate-y-0"
          leave-active-class="duration-200 ease-in"
          leave-from-class="opacity-100 scale-100 translate-y-0"
          leave-to-class="opacity-0 scale-95 translate-y-4"
        >
          <div
            v-if="currentNotification"
            class="relative bg-gradient-to-br from-gray-900 to-black rounded-2xl shadow-2xl max-w-sm w-full mx-4 overflow-hidden border border-gray-700"
            @click.stop
          >
            <!-- Декоративный градиент сверху -->
            <div :class="getHeaderGradient(currentNotification.type)" class="h-1"></div>
            
            <!-- Контент -->
            <div class="p-6">
              <!-- Заголовок с иконкой -->
              <div class="flex items-start gap-4 mb-4">
                <div :class="getIconClass(currentNotification.type)" class="flex-shrink-0 w-12 h-12 rounded-full flex items-center justify-center">
                  <component :is="getIconComponent(currentNotification.type)" class="w-6 h-6 text-white" />
                </div>
                
                <div class="flex-1 min-w-0">
                  <h3 class="text-white font-bold text-lg mb-1 leading-tight">
                    {{ currentNotification.title }}
                  </h3>
                  <p class="text-gray-300 text-sm leading-relaxed">
                    {{ currentNotification.message }}
                  </p>
                </div>
                
                <!-- Кнопка закрытия -->
                <button
                  @click="closePopup"
                  class="flex-shrink-0 text-gray-400 hover:text-white transition-colors p-1 rounded-lg hover:bg-white/10"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                  </svg>
                </button>
              </div>
              
              <!-- Дополнительная информация (если есть) -->
              <div v-if="currentNotification.details" class="mb-4 p-3 rounded-lg bg-white/5 border border-white/10">
                <div v-if="currentNotification.details.amount" class="flex justify-between items-center mb-2">
                  <span class="text-gray-400 text-sm">Сумма:</span>
                  <span class="text-white font-semibold">{{ currentNotification.details.amount }}₽</span>
                </div>
                <div v-if="currentNotification.details.bonus" class="flex justify-between items-center mb-2">
                  <span class="text-gray-400 text-sm">Бонус:</span>
                  <span class="text-green-400 font-semibold">+{{ currentNotification.details.bonus }}₽</span>
                </div>
                <div v-if="currentNotification.details.total" class="flex justify-between items-center pt-2 border-t border-white/10">
                  <span class="text-gray-300 text-sm font-medium">Итого зачислено:</span>
                  <span class="text-white font-bold text-lg">{{ currentNotification.details.total }}₽</span>
                </div>
              </div>
              
              <!-- Время получения -->
              <div class="flex justify-between items-center text-xs text-gray-500 mb-4">
                <span>{{ formatTime(currentNotification.timestamp) }}</span>
                <span v-if="hasMoreNotifications" class="text-blue-400">
                  +{{ pendingNotifications.length }} уведомлений
                </span>
              </div>
              
              <!-- Кнопки действий -->
              <div class="flex gap-3">
                <button
                  @click="closePopup"
                  class="flex-1 px-4 py-2.5 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-medium rounded-xl transition-all duration-200 transform hover:scale-[1.02] active:scale-98"
                >
                  {{ hasMoreNotifications ? 'Следующее' : 'Понятно' }}
                </button>
                
                <button
                  v-if="hasMoreNotifications"
                  @click="closeAllPopups"
                  class="px-4 py-2.5 bg-gray-700 hover:bg-gray-600 text-white font-medium rounded-xl transition-all duration-200"
                >
                  Закрыть все
                </button>
              </div>
            </div>
            
            <!-- Анимированная полоска прогресса (если есть таймер) -->
            <div v-if="autoCloseTimer > 0" class="h-1 bg-gray-800 overflow-hidden">
              <div 
                class="h-full bg-gradient-to-r from-blue-500 to-cyan-500 transition-all ease-linear"
                :style="{ 
                  width: `${progressPercentage}%`,
                  transitionDuration: '100ms'
                }"
              ></div>
            </div>
          </div>
        </transition>
      </div>
    </transition>
  </teleport>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';
import { usePersistentNotifications } from '@/composables/usePersistentNotifications';

// Получаем систему уведомлений
const { 
  pendingNotifications, 
  markAsRead, 
  clearAllNotifications,
  getCurrentNotification 
} = usePersistentNotifications();

// Локальное состояние
const isVisible = ref(false);
const currentNotification = ref(null);
const autoCloseTimer = ref(0);
const progressPercentage = ref(100);

let autoCloseInterval = null;
let progressInterval = null;

// Вычисляемые свойства
const hasMoreNotifications = computed(() => pendingNotifications.value.length > 1);

// Методы для стилизации
const getHeaderGradient = (type) => {
  const gradients = {
    success: 'bg-gradient-to-r from-green-500 to-emerald-600',
    error: 'bg-gradient-to-r from-red-500 to-rose-600',
    info: 'bg-gradient-to-r from-blue-500 to-cyan-600',
    warning: 'bg-gradient-to-r from-yellow-500 to-orange-600'
  };
  return gradients[type] || gradients.info;
};

const getIconClass = (type) => {
  const classes = {
    success: 'bg-gradient-to-br from-green-500 to-emerald-600',
    error: 'bg-gradient-to-br from-red-500 to-rose-600',
    info: 'bg-gradient-to-br from-blue-500 to-cyan-600',
    warning: 'bg-gradient-to-br from-yellow-500 to-orange-600'
  };
  return classes[type] || classes.info;
};

const getIconComponent = (type) => {
  const icons = {
    success: 'IconCheck',
    error: 'IconX',
    info: 'IconInfo',
    warning: 'IconWarning'
  };
  return icons[type] || 'IconInfo';
};

// Форматирование времени
const formatTime = (timestamp) => {
  const date = new Date(timestamp);
  const now = new Date();
  const diffMinutes = Math.floor((now - date) / (1000 * 60));
  
  if (diffMinutes < 1) return 'Только что';
  if (diffMinutes < 60) return `${diffMinutes} мин назад`;
  
  const diffHours = Math.floor(diffMinutes / 60);
  if (diffHours < 24) return `${diffHours} ч назад`;
  
  return date.toLocaleString('ru-RU', {
    day: '2-digit',
    month: '2-digit',
    hour: '2-digit',
    minute: '2-digit'
  });
};

// Показать следующее уведомление
const showNext = () => {
  const notification = getCurrentNotification();
  if (notification) {
    currentNotification.value = notification;
    isVisible.value = true;
    
    // Автозакрытие для успешных уведомлений
    if (notification.type === 'success' && notification.autoClose !== false) {
      startAutoClose(5000); // 5 секунд
    }
  } else {
    isVisible.value = false;
    currentNotification.value = null;
  }
};

// Закрыть текущее уведомление
const closePopup = () => {
  if (currentNotification.value) {
    markAsRead(currentNotification.value.id);
  }
  
  stopAutoClose();
  isVisible.value = false;
  
  // Показываем следующее уведомление через небольшую задержку
  setTimeout(() => {
    showNext();
  }, 300);
};

// Закрыть все уведомления
const closeAllPopups = () => {
  clearAllNotifications();
  stopAutoClose();
  isVisible.value = false;
  currentNotification.value = null;
};

// Автозакрытие
const startAutoClose = (duration) => {
  autoCloseTimer.value = duration;
  progressPercentage.value = 100;
  
  const interval = 100; // Обновление каждые 100мс
  const step = (interval / duration) * 100;
  
  progressInterval = setInterval(() => {
    progressPercentage.value -= step;
    autoCloseTimer.value -= interval;
    
    if (autoCloseTimer.value <= 0) {
      closePopup();
    }
  }, interval);
};

const stopAutoClose = () => {
  if (progressInterval) {
    clearInterval(progressInterval);
    progressInterval = null;
  }
  autoCloseTimer.value = 0;
  progressPercentage.value = 100;
};

// Компоненты иконок
const IconCheck = {
  template: `
    <svg fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd" />
    </svg>
  `
};

const IconX = {
  template: `
    <svg fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clip-rule="evenodd" />
    </svg>
  `
};

const IconInfo = {
  template: `
    <svg fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd" />
    </svg>
  `
};

const IconWarning = {
  template: `
    <svg fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
    </svg>
  `
};

// Регистрируем компоненты локально
const components = {
  IconCheck,
  IconX, 
  IconInfo,
  IconWarning
};

// Слежение за изменениями в уведомлениях
watch(pendingNotifications, (notifications) => {
  if (notifications.length > 0 && !isVisible.value) {
    setTimeout(() => showNext(), 500); // Небольшая задержка для плавности
  }
}, { deep: true, immediate: true });

// Остановка таймеров при размонтировании
onUnmounted(() => {
  stopAutoClose();
});

// Проверяем уведомления при монтировании
onMounted(() => {
  if (pendingNotifications.value.length > 0) {
    setTimeout(() => showNext(), 1000); // Показываем через 1 секунду после загрузки
  }
});
</script>

<style scoped>
/* Дополнительные стили для анимаций */
.duration-300 { transition-duration: 300ms; }
.duration-200 { transition-duration: 200ms; }
.ease-out { transition-timing-function: cubic-bezier(0, 0, 0.2, 1); }
.ease-in { transition-timing-function: cubic-bezier(0.4, 0, 1, 1); }
.scale-95 { transform: scale(0.95); }
.scale-98 { transform: scale(0.98); }
.translate-y-4 { transform: translateY(1rem); }
</style>
