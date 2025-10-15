<template>
  <teleport to="body">
    <div class="notifications-container fixed top-4 right-4 z-[9999] flex flex-col gap-3 max-w-sm">
      <transition-group name="notification">
        <div
          v-for="notification in notifications"
          :key="notification.id"
          v-show="notification.visible"
          :class="[
            'notification-card rounded-lg shadow-2xl p-4 backdrop-blur-sm',
            'transform transition-all duration-300 ease-out',
            'border border-opacity-20',
            getNotificationClass(notification.type)
          ]"
          @click="removeNotification(notification.id)"
        >
          <!-- Иконка -->
          <div class="flex items-start gap-3">
            <div class="flex-shrink-0">
              <component :is="getIcon(notification.type)" class="w-6 h-6" />
            </div>
            
            <!-- Контент -->
            <div class="flex-1 min-w-0">
              <h4 class="text-white font-semibold text-sm mb-1">
                {{ notification.title }}
              </h4>
              <p class="text-white text-opacity-90 text-xs leading-relaxed">
                {{ notification.message }}
              </p>
            </div>
            
            <!-- Кнопка закрытия -->
            <button
              @click.stop="removeNotification(notification.id)"
              class="flex-shrink-0 text-white text-opacity-60 hover:text-opacity-100 transition-opacity"
            >
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
              </svg>
            </button>
          </div>
          
          <!-- Прогресс бар (если есть duration) -->
          <div 
            v-if="notification.duration > 0"
            class="h-1 bg-white bg-opacity-30 rounded-full mt-3 overflow-hidden"
          >
            <div 
              class="h-full bg-white transition-all ease-linear"
              :style="{ 
                width: '100%',
                animation: `shrink ${notification.duration}ms linear forwards`
              }"
            ></div>
          </div>
        </div>
      </transition-group>
    </div>
  </teleport>
</template>

<script setup>
import { useNotifications } from '@/composables/useNotifications';
import { h } from 'vue';

const { notifications, removeNotification } = useNotifications();

// Классы для разных типов уведомлений
const getNotificationClass = (type) => {
  const classes = {
    success: 'bg-gradient-to-r from-green-500/90 to-emerald-600/90 border-green-400',
    error: 'bg-gradient-to-r from-red-500/90 to-rose-600/90 border-red-400',
    warning: 'bg-gradient-to-r from-yellow-500/90 to-orange-600/90 border-yellow-400',
    info: 'bg-gradient-to-r from-blue-500/90 to-cyan-600/90 border-blue-400'
  };
  return classes[type] || classes.info;
};

// Иконки для разных типов
const getIcon = (type) => {
  const icons = {
    success: h('svg', { class: 'w-6 h-6 text-white', fill: 'currentColor', viewBox: '0 0 20 20' }, [
      h('path', { 
        'fill-rule': 'evenodd', 
        d: 'M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z',
        'clip-rule': 'evenodd'
      })
    ]),
    error: h('svg', { class: 'w-6 h-6 text-white', fill: 'currentColor', viewBox: '0 0 20 20' }, [
      h('path', { 
        'fill-rule': 'evenodd', 
        d: 'M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z',
        'clip-rule': 'evenodd'
      })
    ]),
    warning: h('svg', { class: 'w-6 h-6 text-white', fill: 'currentColor', viewBox: '0 0 20 20' }, [
      h('path', { 
        'fill-rule': 'evenodd', 
        d: 'M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z',
        'clip-rule': 'evenodd'
      })
    ]),
    info: h('svg', { class: 'w-6 h-6 text-white', fill: 'currentColor', viewBox: '0 0 20 20' }, [
      h('path', { 
        'fill-rule': 'evenodd', 
        d: 'M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z',
        'clip-rule': 'evenodd'
      })
    ])
  };
  return icons[type] || icons.info;
};
</script>

<style scoped>
/* Анимация появления/исчезновения */
.notification-enter-active,
.notification-leave-active {
  transition: all 0.3s ease;
}

.notification-enter-from {
  opacity: 0;
  transform: translateX(100px) scale(0.95);
}

.notification-leave-to {
  opacity: 0;
  transform: translateX(100px) scale(0.95);
}

.notification-move {
  transition: transform 0.3s ease;
}

/* Анимация прогресс бара */
@keyframes shrink {
  from {
    width: 100%;
  }
  to {
    width: 0%;
  }
}

/* Hover эффект */
.notification-card {
  cursor: pointer;
}

.notification-card:hover {
  transform: scale(1.02);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.2), 0 10px 10px -5px rgba(0, 0, 0, 0.1);
}

/* Адаптив для мобильных */
@media (max-width: 640px) {
  .notifications-container {
    left: 1rem;
    right: 1rem;
    max-width: none;
  }
}
</style>

