<template>
    <!-- 
      Используем Transition для плавного появления/исчезновения попапа
    -->
    <Transition name="popup" mode="out-in">
      <div
        v-if="visible"
        role="dialog"
        aria-labelledby="dialog-title"
        :data-state="visible ? 'open' : 'closed'"
        class="bg-[#141517] fixed top-[55px] right-[25px] z-50 grid w-[313px] h-[232px] gap-4 rounded-lg border border-[#2A2B2D] p-6 shadow-lg pt-5 px-3"
        tabindex="-1"
        style="pointer-events: auto;"
      >
      <div class="flex flex-col">
        <p id="dialog-title" class="text-[20px] font-semibold">Баланс</p>
        
        <!-- Секция основного счета -->
        <div class="flex justify-between mt-1">
          <div class="flex flex-col -space-y-2">
            <p class="text-[16px] opacity-50">Основной счет</p>
            <!-- Отображение баланса с индикатором загрузки -->
            <div class="flex items-center gap-2">
              <p class="text-[18px] font-semibold">{{ mainBalance }}₽</p>
              <div v-if="isLoading" class="animate-spin rounded-full h-3 w-3 border-b-2 border-white opacity-60"></div>
              <div v-if="error && !isLoading" class="text-red-400 text-xs">⚠</div>
            </div>
          </div>
          <div class="rounded-[13px] bg-[#26272C] h-[41px] w-[116px] flex items-center pl-[17px] pr-[17px] justify-between">
            <!-- Иконка флага РФ -->
            <svg viewBox="0 0 24 21" xmlns="http://www.w3.org/2000/svg" width="24" height="21" fill="none">
              <defs>
                <clipPath id="clipPath_1">
                  <rect width="21" height="21" x="1.5" y="0" rx="10.5"></rect>
                </clipPath>
              </defs>
              <g clip-path="url(#clipPath_1)">
                <path fill="#fff" d="M1.5 0h21v7h-21z"></path>
                <path fill="#0039A6" d="M1.5 7h21v7h-21z"></path>
                <path fill="#D52B1E" d="M1.5 14h21v7h-21z"></path>
              </g>
            </svg>
            <p class="text-[16px] translate-y-[1px]">RUB</p>
            <!-- Иконки стрелок -->
            <svg width="13" height="17" viewBox="0 0 13 17" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M5.59846 1.90021C6.07284 1.32505 6.95397 1.32505 7.42835 1.90021L10.0483 5.07678C10.6864 5.85034 10.1361 7.01743 9.1334 7.01743H3.89341C2.89068 7.01743 2.34044 5.85034 2.97846 5.07678L5.59846 1.90021Z" fill="#989CA5"></path>
              <path d="M5.5987 15.0998C6.07308 15.6749 6.95422 15.6749 7.4286 15.0998L10.0486 11.9232C10.6866 11.1497 10.1364 9.98257 9.13364 9.98257H3.89366C2.89093 9.98257 2.34069 11.1497 2.97871 11.9232L5.5987 15.0998Z" fill="#989CA5"></path>
            </svg>
          </div>
        </div>
        
        <!-- Секция стейкинг счета -->
        <div 
          @click="navigateToCabinet"
          class="w-full bg-[#1A1B20] rounded-[12px] h-[58px] mt-2 pr-[22px] pl-4 flex justify-between items-center cursor-pointer hover:bg-[#1F2025] transition-colors"
        >
          <div class="flex flex-col -space-y-[6px]">
            <p class="text-[16px] opacity-50">Стейкинг счет</p>
            <!-- Отображение стейкинг баланса с индикатором -->
            <div class="flex items-center gap-2">
              <p class="text-[18px] font-semibold">{{ stakingBalance }}₽</p>
              <div v-if="isLoading" class="animate-spin rounded-full h-3 w-3 border-b-2 border-white opacity-60"></div>
              <div v-if="error && !isLoading" class="text-red-400 text-xs">⚠</div>
            </div>
          </div>
          <!-- Иконка стрелки вправо -->
          <svg viewBox="0 0 8.20972 13.835" width="8.209717" height="13.834961" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M0.91748 0.91748L6.91748 6.91748L0.91748 12.9175" stroke="rgb(255,255,255)" stroke-opacity="0.5" stroke-linecap="round" stroke-width="1.82746458"></path>
          </svg>
        </div>
  
        <!-- Кнопка Кошелек -->
        <button
          @click="navigateToWallet"
          class="inline-flex items-center justify-center gap-2 whitespace-nowrap transition-all disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg:not([class*='size-'])]:size-4 shrink-0 [&amp;_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive hover:bg-primary/90 h-9 px-4 py-2 has-[&gt;svg]:px-3 text-[20px] text-black font-semibold box-border border border-white/30 rounded-[12.18px] shadow-[0px_0px_25.046154022216797px_0px_rgba(94,255,3,0.25)] relative overflow-hidden bg-gradient-to-b from-[#B1F202] to-[#60FF06] mt-2 gap-x-2"
        >
          <!-- Иконка кошелька -->
          <svg viewBox="0 0 22 22" width="22" height="22" fill="none" class="scale-[1.3]" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.3416 7.33683C19.2897 7.33377 19.2344 7.33255 19.1757 7.33316H16.8611C14.9655 7.33316 13.3439 8.82549 13.3439 10.7707C13.3439 12.7158 14.9664 14.2082 16.8611 14.2082H19.1757C19.2344 14.2088 19.29 14.2076 19.3425 14.2045C19.7321 14.181 20.0999 14.0167 20.3773 13.7421C20.6548 13.4676 20.8229 13.1015 20.8505 12.7122C20.8541 12.6572 20.8541 12.5976 20.8541 12.5426V8.99874C20.8541 8.94374 20.8541 8.88416 20.8505 8.82916C20.8229 8.43982 20.6548 8.07377 20.3773 7.79921C20.0999 7.52465 19.7312 7.36032 19.3416 7.33683ZM16.6585 11.6873C17.1462 11.6873 17.5413 11.2767 17.5413 10.7707C17.5413 10.2647 17.1462 9.85399 16.6585 9.85399C16.17 9.85399 15.7749 10.2647 15.7749 10.7707C15.7749 11.2767 16.17 11.6873 16.6585 11.6873Z" fill="black"></path>
            <path fill-rule="evenodd" clip-rule="evenodd" d="M19.1749 15.5833C19.2066 15.5821 19.2381 15.5883 19.2669 15.6015C19.2958 15.6147 19.3211 15.6345 19.3408 15.6593C19.3606 15.6842 19.3742 15.7133 19.3805 15.7444C19.3869 15.7754 19.3858 15.8076 19.3775 15.8382C19.1941 16.4908 18.9017 17.0482 18.4333 17.5157C17.7467 18.2032 16.8768 18.5066 15.8025 18.6514C14.7575 18.7917 13.4237 18.7917 11.7389 18.7917H9.80287C8.11804 18.7917 6.78337 18.7917 5.73929 18.6514C4.66496 18.5066 3.79504 18.2023 3.10846 17.5166C2.42279 16.83 2.11846 15.9601 1.97362 14.8858C1.83337 13.8408 1.83337 12.507 1.83337 10.8222V10.7195C1.83337 9.03467 1.83337 7.7 1.97362 6.655C2.11846 5.58067 2.42279 4.71075 3.10846 4.02417C3.79504 3.3385 4.66496 3.03417 5.73929 2.88933C6.78429 2.75 8.11804 2.75 9.80287 2.75H11.7389C13.4237 2.75 14.7584 2.75 15.8025 2.89025C16.8768 3.03508 17.7467 3.33942 18.4333 4.02508C18.9017 4.49442 19.1941 5.05083 19.3775 5.7035C19.3858 5.73409 19.3869 5.76622 19.3805 5.79729C19.3742 5.82836 19.3606 5.8575 19.3408 5.88232C19.3211 5.90715 19.2958 5.92697 19.2669 5.94018C19.2381 5.95339 19.2066 5.95961 19.1749 5.95833H16.8612C14.2606 5.95833 11.969 8.01167 11.969 10.7708C11.969 13.53 14.2606 15.5833 16.8612 15.5833H19.1749ZM5.27087 6.41667C5.08854 6.41667 4.91367 6.4891 4.78474 6.61803C4.65581 6.74696 4.58337 6.92183 4.58337 7.10417C4.58337 7.2865 4.65581 7.46137 4.78474 7.5903C4.91367 7.71923 5.08854 7.79167 5.27087 7.79167H8.93754C9.11988 7.79167 9.29474 7.71923 9.42368 7.5903C9.55261 7.46137 9.62504 7.2865 9.62504 7.10417C9.62504 6.92183 9.55261 6.74696 9.42368 6.61803C9.29474 6.4891 9.11988 6.41667 8.93754 6.41667H5.27087Z" fill="black"></path>
          </svg>
          Кошелек
        </button>
      </div>
    </div>
  </Transition>
</template>
  
  <script setup>
  import { computed } from 'vue';
  import { useRouter } from 'vue-router';
  import { useUser } from '../../composables/useUser.js';
  
  // Определяем пропсы, которые компонент может принимать
  // 'visible' - для управления видимостью диалогового окна
  defineProps({
    visible: {
      type: Boolean,
      default: false,
    },
  });
  
  // Определяем события, которые компонент может генерировать
  const emit = defineEmits(['close']);
  
  // Router для навигации
  const router = useRouter();
  
  // Интеграция пользовательских данных
  const { balance, stakeBalance, isLoading, hasUserData, error, formattedBalances } = useUser();
  
  // Вычисляемые свойства для форматированного отображения балансов
  const mainBalance = computed(() => {
    if (isLoading.value) return '...';
    if (!hasUserData.value) return '0.00';
    return formattedBalances.balance.value;
  });
  
  const stakingBalance = computed(() => {
    if (isLoading.value) return '...';
    if (!hasUserData.value) return '0.00';
    return formattedBalances.stakeBalance.value;
  });
  
  // Навигация на страницу Кошелек
  const navigateToWallet = () => {
    router.push('/wallet');
    emit('close'); // Закрываем попап после навигации
  };
  
  // Навигация на страницу Кабинет (Стейкинг)
  const navigateToCabinet = () => {
    router.push('/cabinet');
    emit('close'); // Закрываем попап после навигации
  };
  </script>
  
  <style scoped>
  /* CSS анимации для плавного появления/исчезновения popup */
  .popup-enter-active,
  .popup-leave-active {
    transition: all 0.3s ease-in-out;
  }
  
  .popup-enter-from {
    opacity: 0;
    transform: scale(0.8) translateY(-10px);
  }
  
  .popup-leave-to {
    opacity: 0;
    transform: scale(0.8) translateY(-10px);
  }
  
  .popup-enter-to,
  .popup-leave-from {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
  </style>