<template>
  <Teleport to="body">
    <div v-if="isOpen" class="fixed inset-0 flex items-end justify-center z-[999]" @mousedown="onOverlayMouseDown">
      <!-- Overlay с анимацией -->
      <Transition name="overlay-fade">
        <div 
          v-if="isOpen"
          class="fixed inset-0 bg-black/60"
          :style="{ opacity: overlayOpacity }"
          @click="close"
        ></div>
      </Transition>

      <!-- Drawer с анимацией -->
      <Transition name="drawer-slide">
        <div
          v-if="isOpen"
          ref="drawerRef"
          role="dialog"
          class="popup-drawer bg-[#141517] fixed bottom-0 flex flex-col w-full rounded-t-lg z-[1000]"
          :class="{ 'transition-transform duration-500 ease-out': !isDragging }"
          :style="drawerStyle"
          @mousedown.stop="onDragStart"
          @touchstart.stop="onDragStart"
        >
          <div class="mx-auto mt-2 h-[4px] w-[76px] shrink-0 rounded-full bg-gray-500/50 cursor-grab active:cursor-grabbing"></div>
          
          <div data-slot="drawer-header" class="flex flex-col gap-0.5 p-4 group-data-[vaul-drawer-direction=bottom]/drawer-content:text-center group-data-[vaul-drawer-direction=top]/drawer-content:text-center md:gap-1.5 md:text-left">
            <h2 data-slot="drawer-title" class="text-foreground font-semibold flex items-center justify-between -translate-y-3 -ml-3">
              <div></div>
              <div class="flex items-center gap-x-2 absolute left-1/2 transform -translate-x-1/2 whitespace-nowrap">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" class="translate-y-[2px]" style="filter: drop-shadow(rgba(94, 255, 3, 0.4) 0px 0px 17.976px);">
                  <defs>
                    <linearGradient id="paint_linear_0" x1="12" x2="12" y1="4" y2="20" gradientUnits="userSpaceOnUse">
                      <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                      <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                    </linearGradient>
                  </defs>
                  <rect width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                  <path d="M6 19.75C4.26667 19.3 2.83333 18.3667 1.7 16.95C0.566667 15.5333 2.96059e-16 13.8833 0 12C-2.96059e-16 10.1167 0.566667 8.46667 1.7 7.05C2.83333 5.63333 4.26667 4.7 6 4.25L6 6.35C4.81667 6.75 3.85433 7.46667 3.113 8.5C2.37167 9.53333 2.00067 10.7 2 12C1.99933 13.3 2.37033 14.4667 3.113 15.5C3.85567 16.5333 4.818 17.25 6 17.65L6 19.75ZM14 20C11.7833 20 9.89567 19.221 8.337 17.663C6.77833 16.105 5.99933 14.2173 6 12C6.00067 9.78267 6.78 7.895 8.338 6.337C9.896 4.779 11.7833 4 14 4C15.1 4 16.1333 4.20833 17.1 4.625C18.0667 5.04167 18.9167 5.61667 19.65 6.35L18.25 7.75C17.7 7.2 17.0627 6.771 16.338 6.463C15.6133 6.155 14.834 6.00067 14 6C12.3333 6 10.9167 6.58333 9.75 7.75C8.58333 8.91667 8 10.3333 8 12C8 13.6667 8.58333 15.0833 9.75 16.25C10.9167 17.4167 12.3333 18 14 18C14.8333 18 15.6127 17.846 16.338 17.538C17.0633 17.23 17.7007 16.8007 18.25 16.25L19.65 17.65C18.9167 18.3833 18.0667 18.9583 17.1 19.375C16.1333 19.7917 15.1 20 14 20ZM20 16L18.6 14.6L20.2 13L13 13L13 11L20.2 11L18.6 9.4L20 8L24 12L20 16Z" fill="rgb(0,0,0)" fill-rule="nonzero"></path>
                  <path d="M6 19.75C4.26667 19.3 2.83333 18.3667 1.7 16.95C0.566667 15.5333 2.96059e-16 13.8833 0 12C-2.96059e-16 10.1167 0.566667 8.46667 1.7 7.05C2.83333 5.63333 4.26667 4.7 6 4.25L6 6.35C4.81667 6.75 3.85433 7.46667 3.113 8.5C2.37167 9.53333 2.00067 10.7 2 12C1.99933 13.3 2.37033 14.4667 3.113 15.5C3.85567 16.5333 4.818 17.25 6 17.65L6 19.75ZM14 20C11.7833 20 9.89567 19.221 8.337 17.663C6.77833 16.105 5.99933 14.2173 6 12C6.00067 9.78267 6.78 7.895 8.338 6.337C9.896 4.779 11.7833 4 14 4C15.1 4 16.1333 4.20833 17.1 4.625C18.0667 5.04167 18.9167 5.61667 19.65 6.35L18.25 7.75C17.7 7.2 17.0627 6.771 16.338 6.463C15.6133 6.155 14.834 6.00067 14 6C12.3333 6 10.9167 6.58333 9.75 7.75C8.58333 8.91667 8 10.3333 8 12C8 13.6667 8.58333 15.0833 9.75 16.25C10.9167 17.4167 12.3333 18 14 18C14.8333 18 15.6127 17.846 16.338 17.538C17.0633 17.23 17.7007 16.8007 18.25 16.25L19.65 17.65C18.9167 18.3833 18.0667 18.9583 17.1 19.375C16.1333 19.7917 15.1 20 14 20ZM20 16L18.6 14.6L20.2 13L13 13L13 11L20.2 11L18.6 9.4L20 8L24 12L20 16Z" fill="url(#paint_linear_0)" fill-rule="nonzero"></path>
                </svg>
                <span class="text-[20px] font-semibold translate-y-[2px] text-white">Вывод средств</span>
              </div>
              <div class="cursor-pointer mr-[10px]" @click="close">
                <svg viewBox="0 0 17 17" xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="none">
                  <path d="M0.355656 0.355656C0.829864 -0.118552 1.59871 -0.118552 2.07292 0.355656L8.5 6.78274L14.9271 0.355656C15.4013 -0.118552 16.1701 -0.118552 16.6443 0.355656C17.1186 0.829864 17.1186 1.59871 16.6443 2.07292L10.2173 8.5L16.6443 14.9271C17.1186 15.4013 17.1186 16.1701 16.6443 16.6443C16.1701 17.1186 15.4013 17.1186 14.9271 16.6443L8.5 10.2173L2.07292 16.6443C1.59871 17.1186 0.829864 17.1186 0.355656 16.6443C-0.118552 16.1701 -0.118552 15.4013 0.355656 14.9271L6.78274 8.5L0.355656 2.07292C-0.118552 1.59871 -0.118552 0.829864 0.355656 0.355656Z" fill="rgb(93.3263,96.3657,111.562)" fill-rule="evenodd"></path>
                </svg>
            </div>
            </h2>
            </div>
          <div style="margin: 0px 13px 0 13px;">
          </div>
          <div class="text-white" style="margin: 0px 13px 0 13px;">
            <VivodContent />
          </div>
         
        </div>
        
      </Transition>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, computed, watch, onUnmounted } from 'vue';
import VivodContent from './vivod-content.vue';

// Используем v-model для управления состоянием из родительского компонента
const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
});
const emit = defineEmits(['update:modelValue']);

// Локальная копия для v-model, чтобы избежать прямого изменения пропа
const isOpen = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

// --- Логика перетаскивания (Drag & Swipe) ---
const drawerRef = ref(null); // Ссылка на DOM-элемент окна
const isDragging = ref(false); // Флаг, указывающий, что идет перетаскивание
const startY = ref(0); // Начальная позиция Y при клике/касании
const dragDeltaY = ref(0); // Смещение по Y во время перетаскивания

// Функция для получения Y-координаты из событий мыши и касания
const getCoordY = (e) => e.touches ? e.touches[0].clientY : e.clientY;

const onDragStart = (e) => {
  isDragging.value = true;
  startY.value = getCoordY(e);
  // Добавляем глобальные слушатели, чтобы отслеживать движение за пределами окна
  window.addEventListener('mousemove', onDragMove);
  window.addEventListener('touchmove', onDragMove, { passive: false });
  window.addEventListener('mouseup', onDragEnd);
  window.addEventListener('touchend', onDragEnd);
};

const onDragMove = (e) => {
  if (!isDragging.value) return;
  e.preventDefault(); // Предотвращаем скролл страницы на мобильных
  
  const currentY = getCoordY(e);
  let delta = currentY - startY.value;

  // Позволяем тащить только вниз
  dragDeltaY.value = Math.max(0, delta);
};

const onDragEnd = () => {
  if (!isDragging.value) return;

  isDragging.value = false;

  // Определяем порог для закрытия (например, 40% высоты окна)
  const closeThreshold = drawerRef.value.clientHeight * 0.4;
  
  if (dragDeltaY.value > closeThreshold) {
    close(); // Если сдвинули достаточно далеко, закрываем
  } else {
    // Иначе возвращаем на место с анимацией
    dragDeltaY.value = 0;
  }

  // Убираем глобальные слушатели
  window.removeEventListener('mousemove', onDragMove);
  window.removeEventListener('touchmove', onDragMove);
  window.removeEventListener('mouseup', onDragEnd);
  window.removeEventListener('touchend', onDragEnd);
};

// Функция закрытия
const close = () => {
  isOpen.value = false;
};

// Принудительный сброс, если попап закрыли программно (не свайпом)
watch(isOpen, (newValue) => {
  if (!newValue) {
    dragDeltaY.value = 0;
  }
});

// Очистка слушателей при размонтировании компонента
onUnmounted(() => {
    window.removeEventListener('mousemove', onDragMove);
    window.removeEventListener('touchmove', onDragMove);
    window.removeEventListener('mouseup', onDragEnd);
    window.removeEventListener('touchend', onDragEnd);
});

// --- Динамические стили для "физики" ---
const drawerStyle = computed(() => {
  const styles = {
    maxHeight: '75dvh',
    height: '71dvh'
  };
  
  // Применяем transform во время перетаскивания или возврата
  if (dragDeltaY.value > 0) {
    styles.transform = `translateY(${dragDeltaY.value}px)`;
  }
  
  return styles;
});

const overlayOpacity = computed(() => {
  if (!drawerRef.value) return 1;
  // Уменьшаем прозрачность фона по мере перетаскивания
  const progress = dragDeltaY.value / (drawerRef.value.clientHeight || 1);
  return Math.max(0, 1 - progress * 1.5); // *1.5 для более быстрого затухания
});

// Хак для предотвращения "прыжка" при клике на оверлей во время свайпа
const onOverlayMouseDown = () => {
  if (isDragging.value) {
    onDragEnd();
  }
}
</script>

<style scoped>
/* Анимация для overlay (затемнения) */
.overlay-fade-enter-active,
.overlay-fade-leave-active {
  transition: opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.overlay-fade-enter-from,
.overlay-fade-leave-to {
  opacity: 0 !important;
}

.overlay-fade-enter-to,
.overlay-fade-leave-from {
  opacity: 1;
}

/* Анимация для drawer (само окно) - выезжает снизу вверх */
.drawer-slide-enter-active,
.drawer-slide-leave-active {
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.drawer-slide-enter-from,
.drawer-slide-leave-to {
  transform: translateY(100%);
}

.drawer-slide-enter-to,
.drawer-slide-leave-from {
  transform: translateY(0);
}
</style>  