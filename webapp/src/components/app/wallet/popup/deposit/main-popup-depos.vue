<template>
    <div 
      v-if="isOpen" 
      class="modal-overlay"
      @click="closeModal"
    >
      <div 
        ref="modalContent"
        class="modal-content"
        :class="{ 'modal-open': isOpen, 'is-dragging': isDragging }"
        :style="{ transform: `translateY(${dragOffset}px)` }"
        @click.stop
        @touchstart="onTouchStart"
        @touchmove="onTouchMove"
        @touchend="onTouchEnd"
      >
        <!-- Полоска сверху -->
        <div class="drag-handle"></div>
        
        <!-- Header Component -->
        <div style="margin: -4px 8px 0 8px;">
          <DepHeader @close="closeModal" />
        </div>
        
        <div class="modal-body">
          <p class="text-white/70">Выберите способ пополнения:</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import DepHeader from './dep-header.vue';
  import { ref, watch } from 'vue';
  import { playClickSound } from '../../../../../utils/sounds.js';
  
  const props = defineProps({
    modelValue: {
      type: Boolean,
      default: false
    }
  });
  
  const emit = defineEmits(['update:modelValue']);
  
  const isOpen = ref(props.modelValue);
  const modalContent = ref(null);
  const dragOffset = ref(0);
  const isDragging = ref(false);
  const startY = ref(0);
  const startDragOffset = ref(0);
  
  watch(() => props.modelValue, (newValue) => {
    isOpen.value = newValue;
    if (newValue) {
      dragOffset.value = 0;
    }
  });
  
  const onTouchStart = (e) => {
    isDragging.value = true;
    startY.value = e.touches[0].clientY;
    startDragOffset.value = dragOffset.value;
  };
  
  const onTouchMove = (e) => {
    if (!isDragging.value) return;
    
    const currentY = e.touches[0].clientY;
    const deltaY = currentY - startY.value;
    
    if (startDragOffset.value + deltaY >= 0) {
      dragOffset.value = startDragOffset.value + deltaY;
    }
  };
  
  const onTouchEnd = () => {
    if (!isDragging.value) return;
    
    isDragging.value = false;
    
    if (dragOffset.value > 100) {
      closeModal();
    } else {
      dragOffset.value = 0;
    }
  };
  
  const closeModal = () => {
    playClickSound();
    dragOffset.value = 0;
    isOpen.value = false;
    emit('update:modelValue', false);
  };
  </script>
  
  <style scoped>
  .modal-overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    display: flex;
    align-items: flex-end;
    backdrop-filter: blur(4px);
  }
  
  .modal-content {
    width: 100%;
    height: 715px;
    background-color: #141517;
    border: 0.01px solid #292a30;
    border-radius: 10px 10px 0 0;
    padding: 0;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.3);
    transform: translateY(100%);
    transition: transform 0.3s ease-out;
    position: relative;
    user-select: none;
    touch-action: none;
    animation: slideUp 0.3s ease-out forwards;
  }
  
  .modal-content.modal-open {
    transform: translateY(0);
  }
  
  .modal-content.is-dragging {
    transition: none;
  }
  
  .modal-body {
    color: white;
    padding: 0 20px 20px;
    overflow-y: auto;
    max-height: calc(715px - 100px);
  }
  
  .drag-handle {
    width: 76px;
    height: 3px;
    background-color: #5d6070;
    border-radius: 2px;
    margin: 12px auto 0;
    opacity: 0.6;
    cursor: grab;
  }
  
  .drag-handle:active {
    cursor: grabbing;
  }
  </style>