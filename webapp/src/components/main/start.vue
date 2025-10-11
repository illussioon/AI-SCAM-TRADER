<template>
  <div class="menu-container">
    <p class="title">
      Добро пожаловать <br> в стейкинг валют
    </p>
    
    <p class="subtitle">
      Для начала работы вы можете выбрать <br>пройти обучение или пропустить
    </p>
    
    <button class="btn-primary" @click="openTutorial">
      Пройти обучение
    </button>
    
    <button class="btn-secondary" @click="go_start_app">
      Пропустить
    </button>
  </div>
</template>

<script setup>
import { playClickSound } from '../../utils/sounds.js'

const openTutorial = () => {
  playClickSound()
  window.open('https://rutube.ru/video/181e5442291ab5e6f36a0af704dd629d/', '_blank');
};

const go_start_app = () => {
  playClickSound()
  // Переходим на главную страницу через роутер
  window.location.href = '/';
};
</script>

<style scoped>
.menu-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 20px;
  z-index: 10;
  margin-bottom: 0;
}

.title {
  font-size: 32px;
  font-weight: 600;
  text-align: center;
  line-height: 2.25rem;
  color: #ffffff;
  margin: 0 0 12px 0;
}

.subtitle {
  font-size: 16px;
  text-align: center;
  opacity: 0.5;
  margin-top: 12px;
  color: #ffffff;
  margin-bottom: 12px;
}

.btn-primary, .btn-secondary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  white-space: nowrap;
  border-radius: 0.375rem;
  transition: all 0.2s;
  cursor: pointer;
  border: none;
  outline: none;
  padding: 0.5rem 0.75rem;
  height: 48px;
  width: 100%;
  font-size: 18px;
  font-weight: 600;
  margin-top: 12px;
  max-width: 400px;
}

.btn-primary:disabled, .btn-secondary:disabled {
  pointer-events: none;
  opacity: 0.5;
}

.btn-primary:focus-visible, .btn-secondary:focus-visible {
  outline: 3px solid rgba(59, 130, 246, 0.5);
  outline-offset: 2px;
}

/* Стили для кнопки "Пройти обучение" */
.btn-primary {
  background: #a8ff00;
  color: #000000;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}

.btn-primary:hover {
  background: rgba(168, 255, 0, 0.9);
  transform: translateY(-1px);
}

/* Стили для кнопки "Пропустить" */
.btn-secondary {
  box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  box-shadow: inset 0px 4px 4px 0px rgba(255, 255, 255, 0.25);
  background: linear-gradient(to bottom, rgb(45, 45, 45), rgb(33, 33, 33));
  color: #ffffff;
}

.btn-secondary:hover {
  background: linear-gradient(to bottom, rgb(50, 50, 50), rgb(38, 38, 38));
  transform: translateY(-1px);
}

.btn-primary:active, .btn-secondary:active {
  transform: translateY(0);
}

/* Адаптивность */
@media (max-width: 768px) {
  .menu-container {
    padding: 15px 10px;
  }
  
  .title {
    font-size: 28px;
  }
  
  .subtitle {
    font-size: 15px;
  }
  
  .btn-primary, .btn-secondary {
    font-size: 16px;
    height: 44px;
    margin-left: 0;
    margin-right: 0;
  }
}

@media (max-width: 480px) {
  .menu-container {
    padding: 15px 8px;
  }
  
  .title {
    font-size: 24px;
    line-height: 1.8rem;
  }
  
  .subtitle {
    font-size: 14px;
  }
  
  .btn-primary, .btn-secondary {
    font-size: 15px;
    height: 42px;
    margin-left: 0;
    margin-right: 0;
    width: 100%;
  }
}
</style>