<template>
    <!-- Wallet Card Container -->
    <div class="relative z-0 w-full h-[200px] bg-cover bg-center flex items-center pl-4 mt-2">
      <!-- Background Image -->
      <img
        alt="Wallet card background"
        class="pointer-events-none select-none absolute inset-0 w-full h-full object-cover -z-10 rounded-[11px]"
        loading="eager"
        decoding="async"
        draggable="false"
        :src="cardBackground"
      />
  
      <!-- Balance Information -->
      <div class="flex flex-col w-[140px] -mt-3">
        <p class="text-[16px] font-medium opacity-50">Мой баланс:</p>
        <div class="justify-baseline flex -mt-2">
          <p class="text-[33px] font-semibold">
            <span class="opacity-60">₽</span>{{ formattedBalance.integer }}<span class="text-[20px] opacity-60">{{ formattedBalance.fraction }}</span>
          </p>
          <!-- Loading indicator -->
          <div v-if="isLoading" class="ml-2 mt-2">
            <div class="animate-spin rounded-full h-4 w-4 border-b-2 border-white opacity-60"></div>
          </div>
        </div>
        <div class="w-full h-px bg-[#86F903] -mt-2"></div>
  
        <!-- Daily Stats -->
        <div class="flex mt-2 space-x-1" v-if="!error">
          <!-- Daily Gain -->
          <div class="rounded-[4px] backdrop-blur-[68px] bg-[rgba(134,248,4,0.3)] flex h-[18px] px-1 justify-center items-center text-center">
            <p class="text-[15px] mt-[2px] text-[rgb(134,248,4)]">+{{ dailyGain }}₽</p>
          </div>
          <!-- Percentage Change -->
          <div class="rounded-[4px] backdrop-blur-[68px] bg-[rgba(134,248,4,0.3)] flex h-[18px] px-1 justify-center items-center text-center">
            <div class="text-[15px] mt-[2px] text-[rgb(134,248,4)] flex items-center">
              <svg viewBox="0 0 13 8" xmlns="http://www.w3.org/2000/svg" width="13" height="8" fill="none" class="mb-1">
                <path d="M10.549 4.31579C11.1482 4.95436 10.6954 6 9.81976 6L3.18024 6C2.30462 6 1.85185 4.95436 2.45095 4.31579L5.77072 0.777328C6.16574 0.356275 6.83426 0.356275 7.22928 0.777328L10.549 4.31579Z" fill="rgb(134,248,4)" fill-rule="evenodd"></path>
              </svg>
              <div class="flex items-baseline gap-x-1">
                {{ percentageChange }}%<span class="text-[10px] text-white opacity-40">24h</span>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Error State -->
        <div v-if="error" class="flex mt-2">
          <div class="rounded-[4px] backdrop-blur-[68px] bg-[rgba(255,0,0,0.3)] flex h-[18px] px-1 justify-center items-center text-center">
            <p class="text-[13px] mt-[2px] text-red-300">Ошибка загрузки</p>
          </div>
        </div>
      </div>
  
      <!-- Action Buttons -->
      <div class="absolute bottom-0 left-0 right-0 px-1 mb-2 flex space-x-1">
        <!-- Deposit Button -->
        <button 
          @click="handleDepositClick"
          type="button" 
          class="flex-1 wallet-button"
        >
          <div class="flex-1" tabindex="0">
            <button 
              data-slot="button" 
              class="justify-center gap-2 whitespace-nowrap text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg:not([class*='size-'])]:size-4 shrink-0 [&amp;_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive text-primary-foreground shadow-xs hover:bg-primary/90 px-4 py-2 has-[&gt;svg]:px-3 relative overflow-hidden flex items-center box-border border border-white/30 rounded-[10px] backdrop-blur-[182px] bg-gradient-to-b h-[40px] from-[rgba(179,241,6,1)] to-[rgba(94,255,3,1)] w-full"
            >
              <svg viewBox="0 0 45.6772 45.6772" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="45.677246" height="45.677246" opacity="0.100000001" fill="none" customFrame="#000000" class="absolute left-[-5%] top-[13%]  !w-[46px] !h-[46px]">
                <rect id="Frame 2087325194" width="45.677368" height="45.677368" x="0" y="0" transform="matrix(-1,0,0,-1,45.6772,45.6772)"></rect>
                <circle id="Ellipse 2243" cx="22.8386841" cy="22.8386841" r="22.8386841" fill="rgb(217,217,217)" fill-opacity="0" transform="matrix(-1,0,0,-1,45.6772,45.6772)"></circle>
                <circle id="Ellipse 2243" cx="22.8386841" cy="22.8386841" r="21.8386841" stroke="rgb(0,0,0)" stroke-width="2" transform="matrix(-1,0,0,-1,45.6772,45.6772)"></circle>
                <path id="Vector 1782" d="M14.1881 0.695224L0.718794 14.6211L-0.718794 13.2307L12.7505 -0.695224L14.1881 0.695224ZM12.7509 -0.666944L12.7505 -0.695224C13.1398 -1.09775 13.762 -1.10812 14.1645 -0.718794C14.567 -0.329469 14.5774 0.2927 14.1881 0.695224L14.1598 0.695695L12.7509 -0.666944ZM0.983195 12.9094L7.98222 12.7927C8.54214 12.7834 8.98942 13.216 8.99875 13.7759C9.00808 14.3358 8.57548 14.7831 8.01555 14.7924L0.0166674 14.9258C-0.543255 14.9351 -0.990529 14.5025 -0.999862 13.9426L-1.13319 5.9437C-1.14253 5.38377 -0.70992 4.9365 -0.149998 4.92717C0.409925 4.91783 0.857197 5.35044 0.86653 5.91036L0.983195 12.9094Z" fill="rgb(0,0,0)" fill-rule="nonzero" transform="matrix(-1,0,0,-1,29.4675,29.9238)"></path>
              </svg>
              <span class="text-center w-full text-[18px] font-semibold text-black">Пополнить</span>
            </button>
          </div>
        </button>
        
        <!-- Withdraw Button -->
        <button 
          @click="handleWithdrawClick"
          type="button" 
          class="flex-1 wallet-button"
        >
          <div class="flex-1" tabindex="0">
            <button 
              data-slot="button" 
              class="justify-center gap-2 whitespace-nowrap text-sm font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&amp;_svg]:pointer-events-none [&amp;_svg:not([class*='size-'])]:size-4 shrink-0 [&amp;_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive text-primary-foreground shadow-xs hover:bg-primary/90 px-4 py-2 has-[&gt;svg]:px-3 relative overflow-hidden flex items-center box-border border border-white/30 rounded-[10px] backdrop-blur-[182px] bg-gradient-to-b h-[40px] from-[rgba(179,241,6,1)] to-[rgba(94,255,3,1)] w-full"
            >
              <svg viewBox="0 0 45.6772 45.6772" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="45.677246" height="45.677246" opacity="0.100000001" fill="none" customFrame="#000000" class="absolute left-[-2%] top-[20%] !w-[46px] !h-[46px]">
                <rect id="Frame 2087325194" width="45.677368" height="45.677368" x="0" y="0"></rect>
                <circle id="Ellipse 2243" cx="22.8386841" cy="22.8386841" r="22.8386841" fill="rgb(217,217,217)" fill-opacity="0"></circle>
                <circle id="Ellipse 2243" cx="22.8386841" cy="22.8386841" r="21.8386841" stroke="rgb(0,0,0)" stroke-width="2"></circle>
                <path id="Vector 1782" d="M30.398 16.4486L16.9288 30.3746L15.4912 28.9841L28.9604 15.0582L30.398 16.4486ZM28.9609 15.0865L28.9604 15.0582C29.3498 14.6557 29.9719 14.6453 30.3745 15.0346C30.777 15.4239 30.7874 16.0461 30.398 16.4486L30.3697 16.4491L28.9609 15.0865ZM17.1932 28.6628L24.1922 28.5461C24.7521 28.5368 25.1994 28.9694 25.2087 29.5293C25.218 30.0893 24.7854 30.5365 24.2255 30.5459L16.2266 30.6792C15.6667 30.6885 15.2194 30.2559 15.2101 29.696L15.0768 21.6971C15.0674 21.1372 15.5 20.6899 16.06 20.6806C16.6199 20.6713 17.0672 21.1039 17.0765 21.6638L17.1932 28.6628Z" fill="rgb(0,0,0)" fill-rule="nonzero"></path>
              </svg>
              <span class="text-center w-full text-[18px] font-semibold text-black">Вывести</span>
            </button>
          </div>
        </button>
      </div>
    </div>

    <!-- Modals -->
     <div style="z-index: 9999;">
      <DepositModal v-model="showDepositModal" />
      <WithdrawModal v-model="showWithdrawModal" />
    </div>
  </template>
  
<script setup>
import { ref, computed } from 'vue';
import { playClickSound } from '../../../utils/sounds.js';
import { useUser } from '../../../composables/useUser.js';
import DepositModal from './popup/deposit/main-popup-depos.vue';
import WithdrawModal from './popup/vivod/main-popup-vivod.vue';

// --- Props ---
// You can define props to pass data from a parent component
// const props = defineProps({
//   initialBalance: {
//     type: Number,
//     default: 0
//   },
//   // ... other props
// });

// --- User Data Integration ---
const { 
  balance, 
  profitAll, 
  isLoading, 
  hasUserData,
  error,
  formattedBalances 
} = useUser();

// --- Modal State ---
const showDepositModal = ref(false); // Modal visibility state
const showWithdrawModal = ref(false); // Withdrawal modal visibility state

// --- Computed Daily Stats ---
const dailyGain = computed(() => {
  // Используем profitAll как дневной прирост
  if (!hasUserData.value) return 0;
  const profit = parseFloat(profitAll.value) || 0;
  return profit.toFixed(2);
});

const percentageChange = computed(() => {
  // Простой расчет процента изменения
  if (!hasUserData.value) return 0;
  const currentBalance = parseFloat(balance.value) || 0;
  const profit = parseFloat(profitAll.value) || 0;
  
  if (currentBalance === 0) return 0;
  return ((profit / currentBalance) * 100).toFixed(1);
});

// --- Computed Properties ---
// Форматируем баланс для отображения с разделением на целую и дробную части
const formattedBalance = computed(() => {
  if (isLoading.value) {
    return { integer: '---', fraction: '.--' };
  }
  
  if (!hasUserData.value) {
    return { integer: '0', fraction: '.00' };
  }
  
  const balanceValue = parseFloat(balance.value) || 0;
  const [integer, fraction] = balanceValue.toFixed(2).split('.');
  return {
    integer: integer || '0',
    fraction: `.${fraction || '00'}`,
  };
});

// --- Methods ---
const handleDepositClick = () => {
  playClickSound();
  showDepositModal.value = true;
  console.log('Открыть пополнение баланса');
};

const handleWithdrawClick = () => {
  playClickSound();
  showWithdrawModal.value = true;
  console.log('Открыть вывод средств');
};

// --- Handling the image ---
// It's best practice in Vue to import images so your bundler (like Vite or Webpack)
// can handle them correctly. Place your card.png in the assets folder.
// import cardBackground from './img/wallet/card.png';
// If the image is in the `public` directory, you can just use:
const cardBackground = '/img/wallet/card.png';
  
  </script>
  
<style scoped>
/* Button press effect */
.wallet-button {
  transition: all 0.15s ease-in-out;
}

.wallet-button:active {
  transform: scale(0.95) translateY(1px);
  opacity: 0.8;
}

.wallet-button:hover {
  opacity: 0.95;
}

/* Add subtle shadow animation */
.wallet-button:active > div > button {
  box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3) !important;
}

.wallet-button:hover > div > button {
  box-shadow: 0 4px 12px rgba(179, 241, 6, 0.3) !important;
}

/* Ensure smooth transitions for nested elements */
.wallet-button > div > button {
  transition: all 0.15s ease-in-out;
}
</style>
  
  