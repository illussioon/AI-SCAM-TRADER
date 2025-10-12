<script setup>
import { ref } from 'vue';
import BalancePopup from './balance-popup.vue';

// Состояние для управления видимостью попапа
const isBalancePopupVisible = ref(false);

// Функция для показа/скрытия попапа
const toggleBalancePopup = () => {
  isBalancePopupVisible.value = !isBalancePopupVisible.value;
};

// Обработчик клика на кнопку кошелька в попапе
const handleWalletClick = () => {
  console.log('Переход в кошелек');
  // Здесь можно добавить логику перехода в кошелек
  isBalancePopupVisible.value = false; // Закрываем попап
};
</script>

<template>
  <header class="flex flex-col">
    <div class="flex justify-between items-center px-[8px] border-b border-[#272727]">
      <div class="flex items-center gap-x-1">
        <div class="-mt-1">
            <img src="/icon/mini-logo.svg" alt="Royal Logo" class="logo-image" width="56.933594" height="67.57959" fill="none" customframe="#000000"/>
        </div>
        <div class="w-[86px] h-[36px] border border-[#212022] bg-[#090A0B] rounded-[72px] flex justify-center items-center gap-x-1 relative overflow-hidden">
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-gradient-to-b from-[#B3F106] to-[#5EFF03] left-[-20px] bottom-[-14px] pointer-events-none z-0"></div>
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-gradient-to-b from-[#B3F106] to-[#5EFF03] right-[-20px] top-[-14px] pointer-events-none z-0"></div>
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-[#636668] right-[-10px] bottom-[-14px] pointer-events-none z-0"></div>
          <div class="flex justify-center items-center gap-x-1 relative z-10 w-full h-full">
            <svg viewBox="0 0 24 21" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="21" fill="none" customframe="#000000">
              <defs>
                <clipPath id="clipPath_0">
                  <rect width="24" height="21" x="0" y="0" fill="rgb(255,255,255)"></rect>
                </clipPath>
                <clipPath id="clipPath_1">
                  <rect width="21" height="21" x="1.5" y="0" rx="10.5" fill="rgb(255,255,255)"></rect>
                </clipPath>
                <clipPath id="clipPath_2">
                  <rect width="41.538464" height="30" x="-9" y="-4.5" fill="rgb(255,255,255)"></rect>
                </clipPath>
              </defs>
              <rect id="Frame 1171277187" width="24" height="21" x="0" y="0"></rect>
              <g id="Text Layout" customframe="url(#clipPath_0)">
                <rect id="Text Layout" width="24" height="21" x="0" y="0"></rect>
                <g id="Russia" clip-path="url(#clipPath_1)" customframe="url(#clipPath_1)">
                  <rect id="Russia" width="21" height="21" x="1.5" y="0" rx="10.5" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                  <g id="1f1f7-1f1fa" clip-path="url(#clipPath_2)" customframe="url(#clipPath_2)">
                    <rect id="1f1f7-1f1fa" width="41.538464" height="30" x="-9" y="-4.5" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                    <path id="Vector" d="M-9 4.73047L32.5385 4.73047L32.5385 16.2689L-9 16.2689L-9 4.73047Z" fill="rgb(34,64,140)" fill-rule="nonzero"></path>
                    <path id="Vector" d="M32.5385 18.6349C32.5385 21.1838 30.4719 23.2503 27.9231 23.2503L-4.38461 23.2503C-6.93346 23.2503 -9 21.1838 -9 18.6349L-9 14.0195L32.5385 14.0195L32.5385 18.6349Z" fill="rgb(206,32,40)" fill-rule="nonzero"></path>
                    <path id="Vector" d="M27.9231 -2.25L-4.38461 -2.25C-6.93346 -2.25 -9 -0.183462 -9 2.36538L-9 6.98077L32.5385 6.98077L32.5385 2.36538C32.5385 -0.183462 30.4719 -2.25 27.9231 -2.25Z" fill="rgb(238,238,238)" fill-rule="nonzero"></path>
                  </g>
                </g>
              </g>
            </svg>
            <p class="text-[17.65px] font-semibold leading-[15px] mt-1">RU</p>
            <svg viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="16" height="16" fill="none" customframe="#000000">
              <rect id="chevron_right_16" width="16" height="16" x="0" y="0" transform="matrix(6.12323e-17,1,-1,6.12323e-17,16,0)"></rect>
              <path id="Vector 1" d="M1.13687e-13 0L5 5L0 10" stroke="rgb(161.79,172.166,176.317)" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" transform="matrix(6.12323e-17,1,-1,6.12323e-17,13,6)"></path>
            </svg>
          </div>
        </div>
      </div>
      <div class="flex items-center gap-x-1">
        <div class="relative overflow-hidden w-[133px] h-[39px] border border-[#212022] rounded-[72px] backdrop-blur-[12px] flex justify-between items-center pr-[6px] pl-2">
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-gradient-to-b from-[#B3F106] to-[#5EFF03] -left-4 bottom-[-14px] pointer-events-none z-0"></div>
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-80 bg-[#636668] left-1/2 -translate-x-1/2 bottom-[-14px] pointer-events-none z-0"></div>
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-gradient-to-b from-[#B3F106] to-[#5EFF03] -right-4 bottom-[-14px] pointer-events-none z-0"></div>
          <div class="absolute w-[37.51px] h-[28.68px] blur-[40.8px] opacity-40 bg-gradient-to-b from-[#B3F106] to-[#5EFF03] -right-4 bottom-[20px] pointer-events-none z-0"></div>
          <div class="relative z-10 flex items-center justify-between w-full">
            <svg viewBox="0 0 21 21" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="21" height="21" fill="none" customframe="url(#clipPath_3)">
              <defs>
                <linearGradient id="paint_linear_4" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                  <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                  <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                </linearGradient>
                <linearGradient id="paint_linear_5" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                  <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                  <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                </linearGradient>
                <linearGradient id="paint_linear_6" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                  <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                  <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                </linearGradient>
                <clipPath id="clipPath_3">
                  <rect width="21" height="21" x="0" y="0" rx="10.5" fill="rgb(255,255,255)"></rect>
                </clipPath>
                <g id="pixso_custom_effect_8">
                  <effect x="0" y="3.861111" visibility="visible" fill="rgb(0,0,0)" fill-opacity="0.25" effecttype="dropShadow" stdDeviation="24.0354156" radius="0"></effect>
                </g>
                <filter id="filter_8" width="7.722168" height="9" x="6.638916" y="6" filterUnits="userSpaceOnUse" customeffect="url(#pixso_custom_effect_8)" color-interpolation-filters="sRGB">
                  <feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood>
                  <feOffset dx="0" dy="3.861111" in="SourceAlpha"></feOffset>
                  <feGaussianBlur stdDeviation="8.01180553"></feGaussianBlur>
                  <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0 "></feColorMatrix>
                  <feBlend result="effect_dropShadow_1" in2="BackgroundImageFix" mode="normal"></feBlend>
                  <feBlend result="shape" in="SourceGraphic" in2="effect_dropShadow_1" mode="normal"></feBlend>
                </filter>
              </defs>
              <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_4)"></rect>
              <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_5)"></rect>
              <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_6)"></rect>
              <g filter="url(#filter_8)">
                <path id="\u20BD" d="M11.3475 10.2702C11.5596 10.2702 11.7599 10.2302 11.9484 10.15C12.1369 10.0652 12.2972 9.95443 12.4292 9.81775C12.5659 9.67635 12.6719 9.51374 12.7473 9.32993C12.8274 9.14611 12.8675 8.95286 12.8675 8.75019C12.8675 8.54752 12.8274 8.35428 12.7473 8.17046C12.6719 7.98664 12.5659 7.82639 12.4292 7.68971C12.2972 7.54831 12.1369 7.43755 11.9484 7.35742C11.7599 7.27258 11.5596 7.23016 11.3475 7.23016L9.45981 7.23016L9.45981 10.2702L11.3475 10.2702ZM14.2391 8.75019C14.2391 9.11783 14.166 9.46661 14.0199 9.79654C13.8785 10.1218 13.6758 10.414 13.4119 10.6732C13.1527 10.9277 12.8463 11.1304 12.4928 11.2812C12.144 11.4273 11.7622 11.5004 11.3475 11.5004L9.45981 11.5004L9.45981 12.4407L12.21 12.4407L12.21 13.6708L9.45981 13.6708L9.45981 15.1202L8.08825 15.1202L8.08825 13.6708L6.99948 13.6708L6.99948 12.4407L8.08825 12.4407L8.08825 11.5004L6.99948 11.5004L6.99948 10.2702L8.08825 10.2702L8.08825 6L11.3475 6C11.7622 6 12.144 6.07541 12.4928 6.22624C12.8463 6.37235 13.1527 6.57502 13.4119 6.83425C13.6758 7.08877 13.8785 7.38334 14.0199 7.71799C14.166 8.04792 14.2391 8.39198 14.2391 8.75019Z" fill="rgb(12,13,15)" fill-rule="nonzero"></path>
              </g>
            </svg>
            <p class="text-[18px] font-semibold leading-[15px] mt-1">0</p>
            <button 
              @click="toggleBalancePopup"
              class="cursor-pointer" 
              type="button" 
              aria-haspopup="dialog" 
              :aria-expanded="isBalancePopupVisible" 
              aria-controls="balance-popup" 
              :data-state="isBalancePopupVisible ? 'open' : 'closed'"
            >
              <svg width="31" height="31" viewBox="0 0 31 31" fill="none" xmlns="http://www.w3.org/2000/svg" class="w-[31px] h-[31px]">
                <rect width="31" height="31" rx="15.5" fill="url(#paint0_linear_184_1624)"></rect>
                <rect width="31" height="31" rx="15.5" fill="url(#paint1_linear_184_1624)"></rect>
                <rect x="0.316652" y="0.316652" width="30.3667" height="30.3667" rx="15.1833" stroke="white" stroke-opacity="0.3" stroke-width="0.633304"></rect>
                <path d="M21.9166 16.4149H16.4166V21.9149H14.5833V16.4149H9.08325V14.5815H14.5833V9.08154H16.4166V14.5815H21.9166V16.4149Z" fill="black"></path>
                <defs>
                  <linearGradient id="paint0_linear_184_1624" x1="15.5" y1="0" x2="15.5" y2="31" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#B3F106"></stop>
                    <stop offset="1" stop-color="#5EFF03"></stop>
                  </linearGradient>
                  <linearGradient id="paint1_linear_184_1624" x1="15.5" y1="0" x2="15.5" y2="31" gradientUnits="userSpaceOnUse">
                    <stop stop-color="#B3F106"></stop>
                    <stop offset="1" stop-color="#5EFF03"></stop>
                  </linearGradient>
                </defs>
              </svg>
            </button>
          </div>
        </div>
        <a href="/profile" data-discover="true">
          <div class="w-[37px] h-[37px] rounded-full border-[1px] border-[#5EFF03] shadow-[0_0_25px_rgba(94,255,3,0.25)] p-[1px] flex items-center justify-center">
            <div class="w-full h-full bg-white border border-[#18191D] rounded-full"></div>
          </div>
        </a>
      </div>
    </div>
    
    <!-- Backdrop и попап баланса -->
    <div 
      v-if="isBalancePopupVisible"
      @click="toggleBalancePopup"
      class="fixed inset-0 bg-black/50 z-40"
    ></div>
    
    <BalancePopup 
      :visible="isBalancePopupVisible" 
      @wallet-click="handleWalletClick"
      @click.stop
      id="balance-popup"
    />
  </header>
</template>

<style scoped>
@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Regular-ClstCj-k.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Medium-DHgsE3TE.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Bold-DVcClD20.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

/* Применяем шрифт TTCommons к тексту в header */
header {
  font-family: 'TTCommons', system-ui, -apple-system, sans-serif;
}

/* You can add component-specific styles here. */
/* For example, if you need to style something that cannot be achieved with Tailwind CSS classes alone. */
</style>
