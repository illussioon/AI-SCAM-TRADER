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
          
          <header class="flex flex-col gap-0.5 p-4">
              <h2 class="flex items-center justify-center text-[20px] -translate-y-2 gap-x-2 font-semibold text-white">
                <svg viewBox="0 0 17.998 21.814" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="17.998047" height="21.813965" fill="none" style="filter: drop-shadow(rgba(94, 255, 3, 0.4) 0px 0px 17.976px);">
                  <defs>
                    <linearGradient id="paint_linear_1" x1="8.99900246" x2="8.99900246" y1="-6.12311965e-16" y2="19.9996262" gradientUnits="userSpaceOnUse">
                      <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                      <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                    </linearGradient>
                  </defs>
                  <g>
                    <path d="M9.5922 21.2579L9.58119 21.2599L9.51019 21.2949L9.4902 21.2989L9.4762 21.2949L9.4052 21.2599C9.39453 21.2566 9.38653 21.2583 9.3812 21.2649L9.3772 21.2749L9.3602 21.7029L9.3652 21.7229L9.3752 21.7359L9.47919 21.8099L9.49419 21.8139L9.5062 21.8099L9.6102 21.7359L9.6222 21.7199L9.62619 21.7029L9.60919 21.2759C9.60653 21.2653 9.60086 21.2593 9.5922 21.2579ZM9.85719 21.1449L9.8442 21.1469L9.65919 21.2399L9.64919 21.2499L9.6462 21.2609L9.6642 21.6909L9.6692 21.7029L9.6772 21.7099L9.87819 21.8029C9.89086 21.8063 9.90053 21.8036 9.9072 21.7949L9.91119 21.7809L9.8772 21.1669C9.87386 21.1549 9.8672 21.1476 9.85719 21.1449ZM9.14219 21.1469C9.13779 21.1443 9.13252 21.1434 9.12749 21.1445C9.12246 21.1456 9.11806 21.1487 9.1152 21.1529L9.10919 21.1669L9.0752 21.7809C9.07586 21.7929 9.08153 21.8009 9.0922 21.8049L9.10719 21.8029L9.3082 21.7099L9.3182 21.7019L9.3222 21.6909L9.3392 21.2609L9.33619 21.2489L9.32619 21.2389L9.14219 21.1469Z" fill-rule="evenodd"></path>
                    <path d="M0.999003 15L0.999003 3C0.999003 2.20435 1.31507 1.44129 1.87768 0.87868C2.44029 0.316071 3.20335 8.88178e-16 3.999 0L13.999 0C14.7947 4.44089e-16 15.5577 0.316071 16.1203 0.87868C16.6829 1.44129 16.999 2.20435 16.999 3L16.999 15C17.2331 15.0002 17.4597 15.0826 17.6393 15.2327C17.8189 15.3829 17.9402 15.5913 17.982 15.8216C18.0237 16.052 17.9833 16.2897 17.8679 16.4933C17.7524 16.6969 17.5691 16.8536 17.35 16.936L9.35 19.936C9.12369 20.0208 8.87432 20.0208 8.648 19.936L0.648003 16.936C0.428883 16.8536 0.245618 16.6969 0.130137 16.4933C0.0146565 16.2897 -0.0257197 16.052 0.0160427 15.8216C0.0578051 15.5913 0.179059 15.3829 0.358679 15.2327C0.5383 15.0826 0.764901 15.0002 0.999003 15ZM9.999 4C9.999 3.73478 9.89365 3.48043 9.70611 3.29289C9.51857 3.10536 9.26422 3 8.999 3C8.73379 3 8.47943 3.10536 8.2919 3.29289C8.10436 3.48043 7.999 3.73478 7.999 4L7.999 5L6.999 5C6.33596 5 5.70008 5.26339 5.23124 5.73223C4.76239 6.20107 4.499 6.83696 4.499 7.5C4.499 8.16304 4.76239 8.79893 5.23124 9.26777C5.70008 9.73661 6.33596 10 6.999 10L10.999 10C11.1316 10 11.2588 10.0527 11.3526 10.1464C11.4463 10.2402 11.499 10.3674 11.499 10.5C11.499 10.6326 11.4463 10.7598 11.3526 10.8536C11.2588 10.9473 11.1316 11 10.999 11L5.999 11C5.73379 11 5.47943 11.1054 5.2919 11.2929C5.10436 11.4804 4.999 11.7348 4.999 12C4.999 12.2652 5.10436 12.5196 5.2919 12.7071C5.47943 12.8946 5.73379 13 5.999 13L7.999 13L7.999 14C7.999 14.2652 8.10436 14.5196 8.2919 14.7071C8.47943 14.8946 8.73379 15 8.999 15C9.26422 15 9.51857 14.8946 9.70611 14.7071C9.89365 14.5196 9.999 14.2652 9.999 14L9.999 13L10.999 13C11.662 13 12.2979 12.7366 12.7668 12.2678C13.2356 11.7989 13.499 11.163 13.499 10.5C13.499 9.83696 13.2356 9.20107 12.7668 8.73223C12.2979 8.26339 11.662 8 10.999 8L6.999 8C6.86639 8 6.73922 7.94732 6.64545 7.85355C6.55168 7.75979 6.499 7.63261 6.499 7.5C6.499 7.36739 6.55168 7.24021 6.64545 7.14645C6.73922 7.05268 6.86639 7 6.999 7L11.999 7C12.2642 7 12.5186 6.89464 12.7061 6.70711C12.8936 6.51957 12.999 6.26522 12.999 6C12.999 5.73478 12.8936 5.48043 12.7061 5.29289C12.5186 5.10536 12.2642 5 11.999 5L9.999 5L9.999 4Z" fill="rgb(0,0,0)" fill-rule="evenodd"></path>
                    <path d="M0.999003 15L0.999003 3C0.999003 2.20435 1.31507 1.44129 1.87768 0.87868C2.44029 0.316071 3.20335 8.88178e-16 3.999 0L13.999 0C14.7947 4.44089e-16 15.5577 0.316071 16.1203 0.87868C16.6829 1.44129 16.999 2.20435 16.999 3L16.999 15C17.2331 15.0002 17.4597 15.0826 17.6393 15.2327C17.8189 15.3829 17.9402 15.5913 17.982 15.8216C18.0237 16.052 17.9833 16.2897 17.8679 16.4933C17.7524 16.6969 17.5691 16.8536 17.35 16.936L9.35 19.936C9.12369 20.0208 8.87432 20.0208 8.648 19.936L0.648003 16.936C0.428883 16.8536 0.245618 16.6969 0.130137 16.4933C0.0146565 16.2897 -0.0257197 16.052 0.0160427 15.8216C0.0578051 15.5913 0.179059 15.3829 0.358679 15.2327C0.5383 15.0826 0.764901 15.0002 0.999003 15ZM9.999 4C9.999 3.73478 9.89365 3.48043 9.70611 3.29289C9.51857 3.10536 9.26422 3 8.999 3C8.73379 3 8.47943 3.10536 8.2919 3.29289C8.10436 3.48043 7.999 3.73478 7.999 4L7.999 5L6.999 5C6.33596 5 5.70008 5.26339 5.23124 5.73223C4.76239 6.20107 4.499 6.83696 4.499 7.5C4.499 8.16304 4.76239 8.79893 5.23124 9.26777C5.70008 9.73661 6.33596 10 6.999 10L10.999 10C11.1316 10 11.2588 10.0527 11.3526 10.1464C11.4463 10.2402 11.499 10.3674 11.499 10.5C11.499 10.6326 11.4463 10.7598 11.3526 10.8536C11.2588 10.9473 11.1316 11 10.999 11L5.999 11C5.73379 11 5.47943 11.1054 5.2919 11.2929C5.10436 11.4804 4.999 11.7348 4.999 12C4.999 12.2652 5.10436 12.5196 5.2919 12.7071C5.47943 12.8946 5.73379 13 5.999 13L7.999 13L7.999 14C7.999 14.2652 8.10436 14.5196 8.2919 14.7071C8.47943 14.8946 8.73379 15 8.999 15C9.26422 15 9.51857 14.8946 9.70611 14.7071C9.89365 14.5196 9.999 14.2652 9.999 14L9.999 13L10.999 13C11.662 13 12.2979 12.7366 12.7668 12.2678C13.2356 11.7989 13.499 11.163 13.499 10.5C13.499 9.83696 13.2356 9.20107 12.7668 8.73223C12.2979 8.26339 11.662 8 10.999 8L6.999 8C6.86639 8 6.73922 7.94732 6.64545 7.85355C6.55168 7.75979 6.499 7.63261 6.499 7.5C6.499 7.36739 6.55168 7.24021 6.64545 7.14645C6.73922 7.05268 6.86639 7 6.999 7L11.999 7C12.2642 7 12.5186 6.89464 12.7061 6.70711C12.8936 6.51957 12.999 6.26522 12.999 6C12.999 5.73478 12.8936 5.48043 12.7061 5.29289C12.5186 5.10536 12.2642 5 11.999 5L9.999 5L9.999 4Z" fill="url(#paint_linear_1)" fill-rule="evenodd"></path>
                  </g>
                </svg>
                Инвестиции
              </h2>
            </header>
          
          <div style="margin: 0px 13px 0 13px;" class="">
          <PopupContentStake />
          </div>
        </div>
        
      </Transition>
    </div>
  </Teleport>
</template>

<script setup>
import { ref, computed, watch, onUnmounted } from 'vue';
import PopupContentStake from './popup-content-stake.vue';

const props = defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
});
const emit = defineEmits(['update:modelValue']);

const isOpen = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value),
});

// --- Логика перетаскивания (Drag & Swipe) ---
const drawerRef = ref(null);
const isDragging = ref(false);
const startY = ref(0);
const dragDeltaY = ref(0);

const getCoordY = (e) => e.touches ? e.touches[0].clientY : e.clientY;

const onDragStart = (e) => {
  isDragging.value = true;
  startY.value = getCoordY(e);
  window.addEventListener('mousemove', onDragMove);
  window.addEventListener('touchmove', onDragMove, { passive: false });
  window.addEventListener('mouseup', onDragEnd);
  window.addEventListener('touchend', onDragEnd);
};

const onDragMove = (e) => {
  if (!isDragging.value) return;
  e.preventDefault();

  const currentY = getCoordY(e);
  let delta = currentY - startY.value;

  dragDeltaY.value = Math.max(0, delta);
};

const onDragEnd = () => {
  if (!isDragging.value) return;

  isDragging.value = false;

  const closeThreshold = drawerRef.value.clientHeight * 0.4;
  
  if (dragDeltaY.value > closeThreshold) {
    close();
  } else {
    dragDeltaY.value = 0;
  }

  window.removeEventListener('mousemove', onDragMove);
  window.removeEventListener('touchmove', onDragMove);
  window.removeEventListener('mouseup', onDragEnd);
  window.removeEventListener('touchend', onDragEnd);
};

const close = () => {
  isOpen.value = false;
};

watch(isOpen, (newValue) => {
  if (!newValue) {
    dragDeltaY.value = 0;
  }
});

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
  
  if (dragDeltaY.value > 0) {
    styles.transform = `translateY(${dragDeltaY.value}px)`;
  }
  
  return styles;
});

const overlayOpacity = computed(() => {
  if (!drawerRef.value) return 1;
  const progress = dragDeltaY.value / (drawerRef.value.clientHeight || 1);
  return Math.max(0, 1 - progress * 1.5);
});

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