<template>
    <div class="h-[158px] flex flex-col relative overflow-hidden rounded-[10px] mb-2 -mt-1 px-[15.4px]">
      <svg
        width="365"
        height="158"
        viewBox="0 0 365 158"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="absolute inset-0 w-full h-full"
        preserveAspectRatio="xMidYMid slice"
        style="width: 100%; height: 100%; object-fit: cover;"
      >
        <g clip-path="url(#clip0_1099_510)">
          <rect width="365" height="158" rx="11" fill="white"></rect>
          <rect x="0.5" y="0.5" width="364" height="157" rx="9.5" fill="#131417"></rect>
          <rect x="0.5" y="0.5" width="364" height="157" rx="9.5" fill="url(#paint0_linear_1099_510)"></rect>
          <rect x="0.5" y="0.5" width="364" height="157" rx="9.5" stroke="#2A2B2D"></rect>
          <g filter="url(#filter0_f_1099_510)">
            <rect x="162" y="24" width="47.1625" height="36" fill="#7CFA04"></rect>
          </g>
        </g>
        <g clip-path="url(#clip1_1099_510)">
          <rect opacity="0.4" x="-49" y="78" width="426" height="2" fill="url(#paint1_linear_1099_510)"></rect>
          <g opacity="0.3">
            <rect opacity="0.4" x="25" y="59" width="2" height="37" fill="url(#paint2_linear_1099_510)"></rect>
            <rect opacity="0.4" x="184" y="59" width="2" height="37" fill="url(#paint3_linear_1099_510)"></rect>
            <rect opacity="0.4" x="343" y="59" width="2" height="37" fill="url(#paint4_linear_1099_510)"></rect>
          </g>
        </g>
        <defs>
          <filter
            id="filter0_f_1099_510"
            x="-19"
            y="-157"
            width="409.163"
            height="398"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood>
            <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend>
            <feGaussianBlur stdDeviation="90.5" result="effect1_foregroundBlur_1099_510"></feGaussianBlur>
          </filter>
          <linearGradient
            id="paint0_linear_1099_510"
            x1="207.067"
            y1="-0.00000186923"
            x2="248.502"
            y2="136.215"
            gradientUnits="userSpaceOnUse"
          >
            <stop stop-color="#141518"></stop>
            <stop offset="1" stop-color="#1E2025"></stop>
          </linearGradient>
          <linearGradient
            id="paint1_linear_1099_510"
            x1="-49"
            y1="79"
            x2="377"
            y2="79"
            gradientUnits="userSpaceOnUse"
          >
            <stop stop-color="#D9D9D9" stop-opacity="0"></stop>
            <stop offset="0.524038" stop-color="#9C9C9C"></stop>
            <stop offset="1" stop-color="#737373" stop-opacity="0"></stop>
          </linearGradient>
          <linearGradient
            id="paint2_linear_1099_510"
            x1="26"
            y1="59"
            x2="26"
            y2="96"
            gradientUnits="userSpaceOnUse"
          >
            <stop offset="0.110577" stop-color="#D9D9D9" stop-opacity="0"></stop>
            <stop offset="0.451923" stop-color="#D9D9D9"></stop>
            <stop offset="0.629808" stop-color="#D9D9D9"></stop>
            <stop offset="0.879808" stop-color="#D9D9D9" stop-opacity="0"></stop>
          </linearGradient>
          <linearGradient
            id="paint3_linear_1099_510"
            x1="185"
            y1="59"
            x2="185"
            y2="96"
            gradientUnits="userSpaceOnUse"
          >
            <stop offset="0.110577" stop-color="#D9D9D9" stop-opacity="0"></stop>
            <stop offset="0.451923" stop-color="#D9D9D9"></stop>
            <stop offset="0.629808" stop-color="#D9D9D9"></stop>
            <stop offset="0.879808" stop-color="#D9D9D9" stop-opacity="0"></stop>
          </linearGradient>
          <linearGradient
            id="paint4_linear_1099_510"
            x1="344"
            y1="59"
            x2="344"
            y2="96"
            gradientUnits="userSpaceOnUse"
          >
            <stop offset="0.110577" stop-color="#D9D9D9" stop-opacity="0"></stop>
            <stop offset="0.451923" stop-color="#D9D9D9"></stop>
            <stop offset="0.629808" stop-color="#D9D9D9"></stop>
            <stop offset="0.879808" stop-color="#D9D9D9" stop-opacity="0"></stop>
          </linearGradient>
          <clipPath id="clip0_1099_510">
            <rect width="365" height="158" rx="11" fill="white"></rect>
          </clipPath>
          <clipPath id="clip1_1099_510">
            <rect width="336" height="37" fill="white" transform="translate(15 60)"></rect>
          </clipPath>
        </defs>
      </svg>
      <div class="relative z-10 flex flex-col">
        <div class="flex justify-between mt-1">
          <div class="flex items-center gap-x-2">
            <img
              class="h-7 w-7"
              :alt="currentTariff.name"
              :src="currentTariff.icon"
            />
            <div class="flex flex-col -space-y-1">
              <p class="text-[14px] opacity-50 font-semibold">Тариф</p>
              <div class="flex items-baseline gap-x-1">
                <p class="text-[18px] opacity-80 font-semibold">{{ currentTariff.name }}</p>
                <p class="text-[10px] opacity-60">{{ currentTariff.rate }}%</p>
              </div>
            </div>
          </div>
          <div v-if="nextTariff" class="flex items-center gap-x-2 transition-opacity duration-200" :class="{ 'opacity-40': progressToNext.percentage < 50 }">
            <div class="flex flex-col -space-y-1 items-end">
              <p class="text-[14px] opacity-50 font-semibold">Тариф</p>
              <div class="flex items-baseline gap-x-1">
                <p class="text-[18px] opacity-80 font-semibold">{{ nextTariff.name }}</p>
                <p class="text-[10px] opacity-60">{{ nextTariff.rate }}%</p>
              </div>
            </div>
            <img
              class="h-7 w-7"
              :alt="nextTariff.name"
              :src="nextTariff.icon"
            />
          </div>
          <div v-else class="flex items-center gap-x-2">
            <div class="flex flex-col -space-y-1 items-end">
              <p class="text-[14px] opacity-50 font-semibold">Статус</p>
              <p class="text-[16px] text-green-400 font-semibold">MAX</p>
            </div>
            <div class="h-7 w-7 rounded-full bg-green-400/20 flex items-center justify-center">
              <svg class="h-4 w-4 text-green-400" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" />
              </svg>
            </div>
          </div>
        </div>
        <div class="flex justify-between px-5 mt-2">
          <p class="text-[14px] opacity-50">Текущий тариф</p>
          <p class="text-[14px] opacity-50">{{ nextTariff ? 'Следующий тариф' : 'Максимальный' }}</p>
        </div>
        <div class="relative h-[2px] mt-px rounded w-[97%] ml-[7px] overflow-visible">
          <div class="absolute inset-0 h-full bg-gray-600/30 rounded"></div>
          <div 
            class="absolute inset-0 h-full transition-all duration-1000 ease-out rounded" 
            :style="{ width: `${progressToNext.percentage}%` }"
          >
            <div
              class="absolute inset-0 w-full h-full rounded"
              style="background-image: linear-gradient(rgb(179, 241, 6), rgb(94, 255, 3) 100%); background-color: rgb(13, 197, 106);"
            ></div>
            <div
              class="absolute inset-0 w-full h-full opacity-40 backdrop-blur-sm rounded"
              style="background-image: linear-gradient(rgb(179, 241, 6), rgb(94, 255, 3) 100%); background-color: rgb(13, 197, 106);"
            ></div>
          </div>
        </div>
        <div class="flex justify-between items-center text-[10px] font-mont mt-7">
          <p>Личный депозит:</p>
          <p class="translate-y-px">{{ formatAmount(stakeData.stakeBalance) }}<span class="font-sans">₽</span></p>
        </div>
        <div class="w-full h-px opacity-50 bg-[#4B4B4B] mt-[2px]"></div>
        <div class="flex justify-between items-center text-[10px] font-mont mt-1">
          <p>{{ nextTariff ? 'До следующего тарифа:' : 'Максимальный тариф' }}</p>
          <p class="translate-y-px">
            <span v-if="nextTariff">{{ formatAmount(progressToNext.needed) }}<span class="font-sans">₽</span></span>
            <span v-else class="text-green-400">✓</span>
          </p>
        </div>
        <div v-if="nextTariff" class="w-full h-px opacity-50 bg-[#4B4B4B] mt-[2px]"></div>
        <div v-if="nextTariff" class="flex justify-between items-center text-[10px] font-mont mt-1">
          <p>Прирост доходности:</p>
          <p class="translate-y-px text-green-400">+{{ (nextTariff.rate - currentTariff.rate).toFixed(1) }}%</p>
        </div>
        <div class="w-full h-px opacity-50 bg-[#4B4B4B] mt-[2px]"></div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { computed } from 'vue'
  import { useUserStore } from '../../../stores/user.js'
  
  // Подключаем пользовательский store
  const userStore = useUserStore()
  
  // Данные стейкинга
  const stakeData = computed(() => userStore.stakeData)
  
  // Конфигурация тарифов (должна совпадать с серверной)
  const tariffConfig = {
    'TON': {
      name: 'TON',
      icon: '/icon/ton.svg',
      threshold: 0,
      rate: 1.7
    },
    'ETH': {
      name: 'ETH',
      icon: '/icon/eth.webp',
      threshold: 10000,
      rate: 2.1
    },
    'USDT': {
      name: 'USDT',
      icon: '/icon/teher.webp',
      threshold: 100000,
      rate: 2.7
    }
  }
  
  // Текущий тариф
  const currentTariff = computed(() => {
    return tariffConfig[stakeData.value.currentTariff] || tariffConfig['TON']
  })
  
  // Следующий тариф
  const nextTariff = computed(() => {
    const currentBalance = stakeData.value.stakeBalance
    
    if (currentBalance < tariffConfig.ETH.threshold) {
      return tariffConfig.ETH
    } else if (currentBalance < tariffConfig.USDT.threshold) {
      return tariffConfig.USDT
    }
    
    return null // Уже максимальный тариф
  })
  
  // Прогресс до следующего тарифа
  const progressToNext = computed(() => {
    const currentBalance = stakeData.value.stakeBalance
    const next = nextTariff.value
    
    if (!next) return { percentage: 100, needed: 0 }
    
    const needed = next.threshold - currentBalance
    const progress = (currentBalance / next.threshold) * 100
    
    return {
      percentage: Math.max(0, Math.min(100, progress)),
      needed: Math.max(0, needed)
    }
  })
  
  // Форматирование сумм
  const formatAmount = (amount) => {
    return parseFloat(amount || 0).toLocaleString('ru-RU', {
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
    })
  }
  </script>