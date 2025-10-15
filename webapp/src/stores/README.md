# User Store - Автоматическое управление данными пользователя

## 🚀 Описание

User Store предоставляет централизованное управление данными пользователя с автоматическим обновлением каждые 30 секунд. Интегрируется с существующим API и Telegram WebApp.

## 📁 Файлы

- `user.js` - Основной Pinia store для данных пользователя
- `../composables/useUser.js` - Композабл для удобного доступа к данным
- `../components/UserDataDemo.vue` - Демонстрационный компонент

## 🔧 Использование

### Базовое использование в компоненте

```vue
<script setup>
import { useUser } from '@/composables/useUser.js'

// Получаем все необходимые данные и методы
const {
  userData,           // Полные данные пользователя
  isLoading,         // Статус загрузки
  hasUserData,       // Есть ли данные
  error,             // Ошибка загрузки
  
  // Основная информация
  userInfo,          // { id, username, telegramId, ref, createAccount }
  
  // Балансы
  balance,           // Основной баланс
  stakeBalance,      // Баланс стейкинга
  profitAll,         // Общая прибыль
  partnersBalance,   // Партнерский баланс
  
  // XP и уровень
  xpInfo,            // { raw, current, max, percentage, level }
  
  // Методы
  refreshUserData,   // Принудительное обновление
  getTotalBalance,   // Общий баланс
  formatBalance      // Форматирование баланса
} = useUser()
</script>

<template>
  <div>
    <div v-if="isLoading">Загрузка...</div>
    <div v-else-if="error">Ошибка: {{ error }}</div>
    <div v-else-if="hasUserData">
      <h2>{{ userInfo.username }}</h2>
      <p>Баланс: {{ formatBalance(balance) }}</p>
      <p>Уровень: {{ xpInfo.level }}</p>
      <button @click="refreshUserData">Обновить</button>
    </div>
  </div>
</template>
```

### Отображение балансов

```vue
<template>
  <div class="balances">
    <div class="balance-item">
      <span>Основной баланс:</span>
      <span>{{ formattedBalances.balance }}</span>
    </div>
    <div class="balance-item">
      <span>Стейкинг:</span>
      <span>{{ formattedBalances.stakeBalance }}</span>
    </div>
    <div class="balance-item">
      <span>Партнерский:</span>
      <span>{{ formattedBalances.partnersBalance }}</span>
    </div>
    <div class="total-balance">
      <span>Общий баланс:</span>
      <span>{{ formatBalance(getTotalBalance()) }}</span>
    </div>
  </div>
</template>

<script setup>
import { useUser } from '@/composables/useUser.js'

const { formattedBalances, getTotalBalance, formatBalance } = useUser()
</script>
```

### Отображение XP и уровня

```vue
<template>
  <div class="xp-display">
    <div class="level">Уровень {{ xpInfo.level }}</div>
    <div class="xp-bar">
      <div class="xp-progress" :style="`width: ${xpInfo.percentage}%`"></div>
    </div>
    <div class="xp-text">{{ xpInfo.current }}/{{ xpInfo.max }} XP</div>
  </div>
</template>

<script setup>
import { useUser } from '@/composables/useUser.js'

const { xpInfo } = useUser()
</script>

<style scoped>
.xp-bar {
  width: 100%;
  height: 8px;
  background-color: #333;
  border-radius: 4px;
  overflow: hidden;
}

.xp-progress {
  height: 100%;
  background: linear-gradient(90deg, #b3f106, #5eff03);
  transition: width 0.3s ease;
}
</style>
```

## 🔄 Автоматическое обновление

Store автоматически:
- Инициализируется при запуске приложения (`App.vue`)
- Обновляет данные каждые 30 секунд
- Обрабатывает ошибки и повторные попытки
- Создает пользователя, если он не существует

## 📊 Доступные данные

### userData (полные данные)
```javascript
{
  id: 1,
  username: "user123",
  telegram_id: "123456789",
  balance: "100.50",
  stake_balance: "50.25",
  profit_all: "75.00",
  partners_balance: "25.75",
  ref: null,
  create_account: "2023-01-01T00:00:00.000Z",
  xp: {
    raw: "150/200",
    current: 150,
    max: 200,
    percentage: 75,
    level: 2
  }
}
```

### userInfo (основная информация)
```javascript
{
  id: 1,
  username: "user123",
  telegramId: "123456789",
  ref: null,
  createAccount: "2023-01-01T00:00:00.000Z"
}
```

### xpInfo (опыт и уровень)
```javascript
{
  raw: "150/200",       // Исходная строка
  current: 150,         // Текущий XP
  max: 200,            // Максимальный XP для уровня
  percentage: 75,       // Процент заполнения
  level: 2             // Текущий уровень
}
```

## 🛠️ Методы

### refreshUserData()
Принудительно обновляет данные пользователя.

```javascript
const { refreshUserData } = useUser()

// Обновить данные сейчас
await refreshUserData()
```

### formatBalance(value)
Форматирует числовое значение баланса для отображения.

```javascript
const { formatBalance } = useUser()

const formatted = formatBalance(1234.56) // "1 234,56"
```

### getTotalBalance()
Возвращает общий баланс пользователя (сумма всех балансов).

```javascript
const { getTotalBalance } = useUser()

const total = getTotalBalance() // 251.50
```

### getLastUpdatedFormatted()
Возвращает отформатированное время последнего обновления.

```javascript
const { getLastUpdatedFormatted } = useUser()

const time = getLastUpdatedFormatted() // "13.10.2023, 14:30:25"
```

## 🚨 Обработка ошибок

```vue
<script setup>
import { useUser } from '@/composables/useUser.js'

const { error, hasError, getErrorMessage, isLoading } = useUser()
</script>

<template>
  <div>
    <div v-if="isLoading" class="loading">
      Загрузка данных пользователя...
    </div>
    
    <div v-else-if="hasError()" class="error">
      ❌ {{ getErrorMessage() }}
      <button @click="refreshUserData">Повторить</button>
    </div>
    
    <div v-else class="content">
      <!-- Контент с данными пользователя -->
    </div>
  </div>
</template>
```

## 🔧 Настройка

### Изменение интервала обновления

В `stores/user.js`:

```javascript
// Изменить интервал на 60 секунд
startAutoUpdate(60000)
```

### Остановка автообновления

```javascript
const { stopAutoUpdate } = useUser()

// Остановить автообновление
stopAutoUpdate()
```

## 🎯 Интеграция с существующими компонентами

Для обновления существующих компонентов:

1. Заменить локальные `ref()` данные на `useUser()`
2. Удалить методы `onMounted()` для загрузки данных
3. Обновить шаблоны для новой структуры данных

Пример миграции:

```javascript
// Было:
const userStats = ref(null)
const isLoading = ref(false)

onMounted(async () => {
  isLoading.value = true
  userStats.value = await fetchUserData()
  isLoading.value = false
})

// Стало:
const { userStats, isLoading } = useUser()
// Все остальное работает автоматически!
```

## 📱 Демо компонент

Для тестирования функциональности используйте `UserDataDemo.vue`:

```vue
<template>
  <UserDataDemo />
</template>

<script setup>
import UserDataDemo from '@/components/UserDataDemo.vue'
</script>
```

## 🔍 Отладка

Включить подробные логи в консоли браузера:

```javascript
// В stores/user.js все операции логируются с эмодзи:
// 🚀 Инициализация пользовательских данных...
// 📊 Получение данных пользователя 123456789...
// ✅ Данные пользователя получены
// 🔄 Автоматическое обновление данных пользователя...
```







