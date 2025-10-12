<template>
  <div class="app-container">
    <!-- Подключаем Header компонент -->
    <HeaderApp />
    
    <!-- Подключаем криптовалютную ленту -->
    <div style="margin-top: 6px;">
      <CryptoScroll />
    </div>
    
    <div style="margin: 6px;">
      <PhotoScroll />
    </div>

   <Topmenu />

   <div style="margin: -4px 8px 0 8px;">
      <Footer />
    </div>

    
    <!-- Основное содержимое приложения -->
    <div class="absolute w-[27px] h-[54px] blur-[40px] opacity-[0.77] pointer-events-none will-change-auto" style="background: rgb(140, 246, 5); top: 60px; left: 0px; z-index: 30; transform: translateZ(0px); backface-visibility: hidden;"></div>
  
    
    <!-- Подключаем Menu компонент -->
    <div style="margin-top: 120px;">
      <Menu />
    </div>
   
  </div>
</template>

<script setup>
import Menu from './menu.vue'
import HeaderApp from './header-app.vue'
import CryptoScroll from './crypto-scroll.vue'
import PhotoScroll from './app-main-content/photo-scroll.vue'
import NewsMain from './app-main-content/news-main.vue'
import Footer from './footer.vue'
import Topmenu from './topmenu.vue'

// Главная страница приложения
</script>

<style scoped>
.app-container {
  min-height: 100vh;
  background-color: #0b0c0d;
  color: #ffffff;
  position: relative;
  padding: 0; /* Убираем padding для header */
  display: flex;
  flex-direction: column;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  flex: 1; /* Заполняем доступное пространство */
  min-height: calc(100vh - 180px); /* Учитываем header и menu */
  text-align: center;
  padding: 20px;
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
  
  .content {
    min-height: calc(100vh - 160px);
    padding: 15px;
  }
}

@media (max-width: 480px) {
  .welcome-title {
    font-size: 24px;
  }
  
  .welcome-text {
    font-size: 14px;
  }
  
  .content {
    min-height: calc(100vh - 140px);
    padding: 15px;
  }
}
</style>
