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
          
          <header class="flex items-center justify-between p-4 -translate-y-2">
            <div class="flex items-center gap-x-2">
              <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="filter: drop-shadow(rgba(94, 255, 3, 0.4) 0px 0px 17.976px);"><path fill-rule="evenodd" clip-rule="evenodd" d="M18.4101 7.85991C18.3518 7.8572 18.2934 7.8562 18.2351 7.85691H15.8C13.808 7.85691 12.1021 9.43791 12.1021 11.4999C12.1021 13.5619 13.8081 15.1429 15.8011 15.1429H18.234C18.2954 15.1436 18.3537 15.1422 18.4091 15.1389C18.8201 15.1122 19.2074 14.9372 19.4992 14.6465C19.7909 14.3557 19.9671 13.9688 19.9951 13.5579C19.9991 13.4989 19.9991 13.4359 19.9991 13.3779V9.62191C19.9991 9.56391 19.9991 9.50091 19.9951 9.44191C19.9671 9.03113 19.791 8.64444 19.4995 8.35367C19.208 8.0629 18.8209 7.88781 18.4101 7.86091M15.5871 12.4719C16.1001 12.4719 16.5171 12.0379 16.5171 11.5009C16.5171 10.9639 16.1001 10.5299 15.5871 10.5299C15.0741 10.5299 14.6581 10.9639 14.6581 11.5009C14.6581 12.0379 15.0731 12.4719 15.5871 12.4719Z" fill="#90F705"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M18.234 16.6C18.2675 16.5988 18.3008 16.6055 18.3312 16.6196C18.3617 16.6337 18.3884 16.6547 18.4092 16.6809C18.43 16.7072 18.4444 16.738 18.4511 16.7708C18.4579 16.8037 18.4568 16.8377 18.448 16.87C18.254 17.562 17.947 18.152 17.454 18.648C16.733 19.375 15.818 19.698 14.688 19.851C13.59 20 12.188 20 10.416 20H8.379C6.608 20 5.205 20 4.107 19.851C2.977 19.698 2.062 19.375 1.341 18.648C0.62 17.923 0.3 17 0.148 15.862C0 14.754 0 13.34 0 11.555V11.445C0 9.66 0 8.245 0.148 7.139C0.3 6 0.62 5.08 1.34 4.351C2.061 3.625 2.976 3.301 4.106 3.149C5.205 3 6.608 3 8.379 3H10.416C12.187 3 13.59 3 14.688 3.149C15.818 3.302 16.733 3.625 17.454 4.351C17.947 4.848 18.254 5.438 18.448 6.131C18.4566 6.16328 18.4575 6.19714 18.4507 6.22984C18.4439 6.26255 18.4295 6.2932 18.4087 6.31935C18.3879 6.3455 18.3613 6.36641 18.3309 6.38042C18.3006 6.39442 18.2674 6.40113 18.234 6.4H15.801C13.067 6.4 10.658 8.577 10.658 11.5C10.658 14.423 13.068 16.6 15.802 16.6H18.234ZM3.614 6.886C3.51879 6.88639 3.42459 6.90554 3.33678 6.94233C3.24897 6.97913 3.16927 7.03287 3.10222 7.10047C3.03518 7.16807 2.98211 7.24821 2.94604 7.33633C2.90997 7.42444 2.89161 7.51879 2.892 7.614C2.892 8.017 3.215 8.343 3.614 8.343H7.47C7.87 8.343 8.193 8.017 8.193 7.614C8.19353 7.42163 8.11769 7.2369 7.98213 7.10041C7.84657 6.96391 7.66237 6.88679 7.47 6.886H3.614Z" fill="#90F705"></path><path d="M5.7771 2.0241L7.7351 0.5811C8.2461 0.203515 8.86473 -0.000244141 9.5001 -0.000244141C10.1355 -0.000244141 10.7541 0.203515 11.2651 0.5811L13.2341 2.0321C12.4101 2.0001 11.4901 2.0001 10.4831 2.0001H8.3131C7.3911 2.0001 6.5441 2.0001 5.7771 2.0241Z" fill="#90F705"></path></svg>
              <span class="text-white text-[20px] font-semibold translate-y-px">Кошелек</span>
            </div>
            <div class="cursor-pointer" @click="close">
              <svg viewBox="0 0 17 17" xmlns="http://www.w3.org/2000/svg" width="17" height="17" fill="none"><path d="M0.355656 0.355656C0.829864 -0.118552 1.59871 -0.118552 2.07292 0.355656L8.5 6.78274L14.9271 0.355656C15.4013 -0.118552 16.1701 -0.118552 16.6443 0.355656C17.1186 0.829864 17.1186 1.59871 16.6443 2.07292L10.2173 8.5L16.6443 14.9271C17.1186 15.4013 17.1186 16.1701 16.6443 16.6443C16.1701 17.1186 15.4013 17.1186 14.9271 16.6443L8.5 10.2173L2.07292 16.6443C1.59871 17.1186 0.829864 17.1186 0.355656 16.6443C-0.118552 16.1701 -0.118552 15.4013 0.355656 14.9271L6.78274 8.5L0.355656 2.07292C-0.118552 1.59871 -0.118552 0.829864 0.355656 0.355656Z" fill="rgb(93,96,111)" fill-rule="evenodd"></path></svg>
            </div>
          </header>
          <div style="margin: 0px 13px 0 13px;">
            <TopMenu /> 
          </div>
        </div>
        
      </Transition>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, computed, watch, onUnmounted } from 'vue';
import TopMenu from './top-menu.vue'

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
    maxHeight: '90dvh',
    height: '80dvh'
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