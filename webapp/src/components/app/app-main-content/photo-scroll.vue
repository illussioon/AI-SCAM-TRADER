<template>
    <!-- Основной контейнер карусели -->
    <div class="relative overflow-hidden rounded-[22px] bg-[#0E1114] ring-1 ring-white/10">
      
      <!-- Контейнер для слайдов с динамическим смещением -->
      <div 
        class="flex transition-transform duration-500 ease-out" 
        :style="sliderStyle"
      >
        <!-- Рендеринг каждого слайда с помощью v-for -->
        <div 
          v-for="(image, index) in images" 
          :key="index" 
          class="relative h-[170px] w-full flex-shrink-0"
        >
          <img :src="image" :alt="'Banner ' + (index + 1)" class="h-full w-full object-cover" />
        </div>
      </div>
      
      <!-- Контейнер для точек навигации (пагинации) -->
      <div class="absolute bottom-3 left-1/2 z-[2] -translate-x-1/2 flex justify-center">
        <div class="flex items-center gap-2 rounded-full bg-[#373737B2] px-3 py-1 ring-1 ring-white/10">
          <!-- Рендеринг кнопок-точек для каждого слайда -->
          <button
            v-for="(image, index) in images"
            :key="'dot-' + index"
            @click="goToSlide(index)"
            class="pointer-events-auto h-2 w-2 rounded-full transition-all duration-200"
            :class="currentIndex === index ? 'bg-[#9AFE00] shadow-[0_0_14px_rgba(154,254,0,0.8)]' : 'bg-white/20'"
            :aria-label="'Показать слайд ' + (index + 1)"
          ></button>
        </div>
      </div>
      
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted, onUnmounted } from 'vue';
  
  // --- Состояние компонента ---
  
  // Массив с путями к изображениям
  const images = [
    '/img-scroll/1.webp',
    '/img-scroll/2.webp',
    '/img-scroll/3.webp',
    '/img-scroll/4.webp',
    '/img-scroll/5.webp'
  ];
  
  // Индекс текущего активного слайда
  const currentIndex = ref(0);
  // ID для интервала автоматической прокрутки
  let intervalId = null;

  const sliderStyle = computed(() => ({
    transform: `translateX(-${currentIndex.value * 100}%)`,
  }));
  
  // --- Методы ---
  
  // Переход к следующему слайду
  const nextSlide = () => {
    currentIndex.value = (currentIndex.value + 1) % images.length;
  };
  
  // Переход к конкретному слайду по индексу
  const goToSlide = (index) => {
    currentIndex.value = index;
    // Сбрасываем таймер автопрокрутки при ручном переключении
    resetInterval();
  };
  
  // Запуск автоматической прокрутки
  const startInterval = () => {
    intervalId = setInterval(nextSlide, 3000); // Меняет слайд каждые 3 секунды
  };
  
  // Сброс (перезапуск) интервала
  const resetInterval = () => {
      clearInterval(intervalId);
      startInterval();
  };
  
  
  // --- Хуки жизненного цикла ---
  
  // Запускаем автопрокрутку после того, как компонент будет смонтирован
  onMounted(() => {
    startInterval();
  });
  
  // Очищаем интервал, когда компонент будет размонтирован, чтобы избежать утечек памяти
  onUnmounted(() => {
    clearInterval(intervalId);
  });
  </script>
  