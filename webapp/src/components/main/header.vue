<template>
  <header class="header">
    <div class="header-container">
      <!-- Логотип -->
      <div class="header-left">
        <div class="logo">
          <img src="/icon/logo.svg" alt="Royal Logo" class="logo-image" />
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
// Header компонент с логотипом Royal
</script>

<style scoped>
.header {
  width: 100%;
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(10px);
}

.header-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  height: 80px;
}

/* Логотип */
.header-left {
  display: flex;
  align-items: center;
}

.logo {
  display: flex;
  align-items: center;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.logo:hover {
  transform: scale(1.05);
}

.logo-image {
  height: 60px;
  width: auto;
}

/* Мобильная адаптация */
@media (max-width: 768px) {
  .header-container {
    padding: 0 1rem;
    height: 70px;
  }
  
  .logo-image {
    height: 50px;
  }
}

@media (max-width: 480px) {
  .header-container {
    padding: 0 0.0rem;
    height: 65px;
  }
  
  .logo-image {
    width:165px;
    height: 68px;
  }
}
</style>
