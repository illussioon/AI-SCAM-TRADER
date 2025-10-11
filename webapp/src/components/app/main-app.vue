<template>
  <div class="app-container">
    <!-- Основное содержимое приложения -->
    <div class="content">
      <h1 class="welcome-title">Добро пожаловать в приложение</h1>
      <p class="welcome-text">Это главная страница приложения</p>
    </div>
    
    <!-- Подключаем Menu компонент -->
    <Menu />
  </div>
</template>

<script setup>
import Menu from './menu.vue'

// Главная страница приложения
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background-color: #0b0c0d;
  color: #ffffff;
  position: relative;
  padding: 20px;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: calc(100vh - 120px);
  text-align: center;
}

.welcome-title {
  font-size: 32px;
  font-weight: 700;
  color: #8EF804;
  margin-bottom: 16px;
  font-family: 'TTCommons', system-ui, -apple-system, sans-serif;
}

.welcome-text {
  font-size: 18px;
  color: #9EA5AD;
  font-family: 'TTCommons', system-ui, -apple-system, sans-serif;
}

@media (max-width: 768px) {
  .welcome-title {
    font-size: 28px;
  }
  
  .welcome-text {
    font-size: 16px;
  }
}

@media (max-width: 480px) {
  .welcome-title {
    font-size: 24px;
  }
  
  .welcome-text {
    font-size: 14px;
  }
  
  .app-container {
    padding: 15px;
  }
}
</style>
