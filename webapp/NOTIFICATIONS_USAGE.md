# Использование системы Popup уведомлений

## Установка

### 1. Добавьте компонент в App.vue

```vue
<template>
  <div id="app">
    <!-- Ваш контент -->
    <router-view />
    
    <!-- Контейнер уведомлений -->
    <NotificationsContainer />
  </div>
</template>

<script setup>
import NotificationsContainer from '@/components/NotificationsContainer.vue';
</script>
```

## Использование в компонентах

### Базовое использование

```vue
<script setup>
import { useNotifications } from '@/composables/useNotifications';

const { showSuccess, showError, showInfo, showWarning } = useNotifications();

// Показать успешное уведомление
const handleSuccess = () => {
  showSuccess(
    'Успешно!',
    'Операция выполнена успешно',
    5000 // 5 секунд (необязательно, по умолчанию 5000)
  );
};

// Показать ошибку
const handleError = () => {
  showError(
    'Ошибка!',
    'Что-то пошло не так',
    7000
  );
};

// Показать информацию
const handleInfo = () => {
  showInfo(
    'Информация',
    'Это информационное сообщение'
  );
};

// Показать предупреждение
const handleWarning = () => {
  showWarning(
    'Внимание!',
    'Это предупреждение'
  );
};
</script>
```

### Интеграция с системой пополнения

```vue
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useDeposit } from '@/composables/deposit';
import { useNotifications } from '@/composables/useNotifications';
import { useTelegram } from '@/composables/useTelegram';

const { showSuccess, showError, showInfo } = useNotifications();
const { createDepositRequest, subscribeToStatusUpdates } = useDeposit();
const { user } = useTelegram();

const amount = ref(1000);
const currentRequestId = ref(null);
let unsubscribe = null;

// Создание запроса на пополнение
const handleDeposit = async () => {
  try {
    showInfo(
      'Обработка...',
      'Создаем запрос на пополнение'
    );
    
    const result = await createDepositRequest(
      user.value.id,
      amount.value,
      'СБП'
    );
    
    if (result.success) {
      currentRequestId.value = result.data.request_id;
      
      showSuccess(
        'Запрос создан!',
        `Ожидайте подтверждения от администратора. Сумма к зачислению: ${result.data.total_amount}₽`
      );
      
      // Подписываемся на обновления статуса
      unsubscribe = subscribeToStatusUpdates(currentRequestId.value, handleStatusUpdate);
    }
  } catch (error) {
    showError(
      'Ошибка создания запроса',
      error.message || 'Попробуйте позже'
    );
  }
};

// Обработка обновления статуса
const handleStatusUpdate = (status) => {
  if (status.status === 'approved') {
    showSuccess(
      '🎉 Пополнение подтверждено!',
      `На ваш баланс зачислено ${status.total_amount}₽`,
      10000 // Показываем 10 секунд
    );
    
    // Обновить баланс в UI
    // updateUserBalance();
    
  } else if (status.status === 'rejected') {
    showError(
      'Пополнение отклонено',
      'Ваш запрос на пополнение был отклонен администратором. Обратитесь в поддержку.',
      10000
    );
  }
};

// Отписываемся при размонтировании
onUnmounted(() => {
  if (unsubscribe) {
    unsubscribe();
  }
});
</script>

<template>
  <div>
    <input v-model="amount" type="number" />
    <button @click="handleDeposit">
      Пополнить баланс
    </button>
  </div>
</template>
```

### Интеграция с bank-dep.vue

Добавьте в `webapp/src/components/app/wallet/popup/deposit/bank-dep.vue`:

```javascript
import { useDeposit } from '@/composables/deposit';
import { useNotifications } from '@/composables/useNotifications';
import { useUser } from '@/composables/useUser';

const { createDepositRequest, subscribeToStatusUpdates } = useDeposit();
const { showSuccess, showError, showInfo } = useNotifications();
const { user } = useUser(); // или useTelegram()

let statusUnsubscribe = null;

const handleContinueClick = async () => {
  try {
    // Получаем сумму из компонента
    const depositAmount = parseInt(amount.value);
    
    if (!depositAmount || depositAmount < 100) {
      showError('Ошибка', 'Минимальная сумма пополнения 100₽');
      return;
    }
    
    showInfo('Создание запроса...', 'Пожалуйста, подождите');
    
    // Создаем запрос на пополнение
    const result = await createDepositRequest(
      user.value.telegram_id,
      depositAmount,
      selectedPaymentMethod.value || 'СБП'
    );
    
    if (result.success) {
      // Переключаем на dep-sbp компонент
      showDepSbp.value = true;
      
      showSuccess(
        'Запрос создан!',
        `Ожидайте подтверждения. К зачислению: ${result.data.total_amount}₽`
      );
      
      // Подписываемся на обновления
      statusUnsubscribe = subscribeToStatusUpdates(
        result.data.request_id,
        (status) => {
          if (status.status === 'approved') {
            showSuccess(
              '🎉 Баланс пополнен!',
              `Зачислено: ${status.total_amount}₽`,
              10000
            );
          } else if (status.status === 'rejected') {
            showError(
              'Отказ в пополнении',
              'Запрос отклонен. Свяжитесь с поддержкой.',
              10000
            );
          }
        }
      );
    }
  } catch (error) {
    showError(
      'Ошибка',
      error.message || 'Не удалось создать запрос'
    );
  }
};

// В onUnmounted
onUnmounted(() => {
  if (statusUnsubscribe) {
    statusUnsubscribe();
  }
});
```

## Продвинутое использование

### Кастомная длительность

```javascript
// Показать на 10 секунд
showSuccess('Заголовок', 'Сообщение', 10000);

// Показать бесконечно (пока пользователь не закроет)
showSuccess('Заголовок', 'Сообщение', 0);
```

### Программное закрытие

```javascript
const { showSuccess, removeNotification } = useNotifications();

// Получаем ID уведомления
const notificationId = showSuccess('Загрузка...', 'Пожалуйста, подождите', 0);

// Позже закрываем программно
setTimeout(() => {
  removeNotification(notificationId);
}, 3000);
```

### Очистка всех уведомлений

```javascript
const { clearAll } = useNotifications();

clearAll(); // Закрывает все активные уведомления
```

### Доступ к списку уведомлений

```javascript
const { notifications } = useNotifications();

console.log('Активных уведомлений:', notifications.value.length);
```

## Типы уведомлений

1. **success** - Успешные операции (зеленый)
2. **error** - Ошибки (красный)
3. **warning** - Предупреждения (оранжевый)
4. **info** - Информационные сообщения (синий)

## Особенности

- ✅ Автоматическое закрытие через заданное время
- ✅ Ручное закрытие по клику
- ✅ Прогресс бар времени
- ✅ Плавные анимации появления/исчезновения
- ✅ Адаптивный дизайн (мобильные устройства)
- ✅ Стек уведомлений (несколько одновременно)
- ✅ Красивые градиенты и иконки

## Стилизация

Все стили находятся в `NotificationsContainer.vue`. Вы можете кастомизировать:
- Цвета градиентов
- Размеры и отступы
- Анимации
- Позиционирование (сейчас: top-right)

