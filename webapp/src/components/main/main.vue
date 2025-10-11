<template>
  <div class="main-container">
    <!-- Светящийся блок в правом верхнем углу -->
    <div class="glow-background"></div>
    
    <!-- 3D Сфера на заднем плане -->
    <div class="sphere-background">
      <Sphere />
    </div>
    
    <!-- Подключаем Header компонент -->
    <Header />
    
    <!-- Добавляем Start компонент в низ страницы -->
    <div class="start-section">
      <Start />
    </div>
  </div>
</template>

<script setup>
import Header from './header.vue'
import Sphere from './sphere.vue'
import Start from './start.vue'

// Компонент обучения/tutorial
</script>

<style scoped>
.main-container {
  min-height: 100vh;
  background-color: #0b0c0d;
  color: #ffffff;
  position: relative;
  overflow: hidden;
}

.glow-background {
  position: absolute;
  top: -100px;
  right: -100px;
  width: 406.99px;
  height: 264.16px;
  transform: rotate(24.56deg);
  filter: blur(154.535px);
  background: rgb(168, 243, 6);
  opacity: 0.22;
  z-index: 50;
  pointer-events: none;
}

.sphere-background {
  position: absolute;
  top: 80px;
  left: 0;
  width: 100%;
  height: calc(100% - 80px);
  z-index: 1;
  pointer-events: none;
  display: flex;
  justify-content: center;
  align-items: flex-start;
}

.start-section {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 100;
  padding: 0;
}

/* Адаптивность для сферы */
@media (max-width: 768px) {
  .sphere-background {
    top: 70px;
    height: calc(100% - 70px);
  }
}

@media (max-width: 480px) {
  .sphere-background {
    top: 65px;
    height: calc(100% - 65px);
  }
}
</style>