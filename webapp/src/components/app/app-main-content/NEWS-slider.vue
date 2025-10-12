<template>
    <section class="embla">
      <div class="embla__viewport" ref="emblaRef">
        <div class="embla__container">
          <div class="embla__slide">
            <img alt="slide-1" class="embla__slide__img" src="/img/NEWS-slider/1.webp">
          </div>
          <div class="embla__slide">
            <img alt="slide-2" class="embla__slide__img" src="/img/NEWS-slider/2.webp">
          </div>
        </div>
      </div>
    </section>
  </template>
    
  <script setup>
  import emblaCarouselVue from 'embla-carousel-vue'
  import Autoplay from 'embla-carousel-autoplay'
  import { onMounted } from 'vue'
  
  // Настройка Embla с плавными переходами
  const [emblaRef, emblaApi] = emblaCarouselVue(
    { 
      loop: true,
      align: 'start',
      // Ключевые параметры для плавности
      duration: 25, // Увеличена длительность анимации для плавности
      dragFree: false, // Фиксированная прокрутка по слайдам
      inViewThreshold: 0, // Порог видимости
      skipSnaps: false, // Не пропускать слайды
      containScroll: 'trimSnaps' // Оптимизация скроллинга
    },
    [Autoplay({ delay: 5000, stopOnInteraction: false })]
  )
  
  onMounted(() => {
    if (emblaApi.value) {
      console.log('Embla Carousel инициализирован')
    }
  })
  </script>
    
  <style scoped>
  .embla {
    overflow: hidden;
    width: 100%;
    border-radius: 12px;
  }
  
  .embla__viewport {
    overflow: hidden;
    width: 100%;
    cursor: grab;
  }
  
  .embla__viewport:active {
    cursor: grabbing;
  }
  
  .embla__container {
    display: flex;
    backface-visibility: hidden;
    touch-action: pan-y pinch-zoom;
    /* Убираем transition отсюда - Embla сам управляет анимацией */
  }
  
  .embla__slide {
    position: relative;
    flex: 0 0 100%;
    min-width: 0;
    /* Оптимизация для плавной анимации */
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
  }
  
  .embla__slide__img {
    width: 100%;
    height: auto;
    object-fit: cover;
    display: block;
    border-radius: 12px;
    /* Предотвращение мерцания при анимации */
    -webkit-transform: translateZ(0);
    transform: translateZ(0);
    pointer-events: none;
    user-select: none;
  }
  </style>