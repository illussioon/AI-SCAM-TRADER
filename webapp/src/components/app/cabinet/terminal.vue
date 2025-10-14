<template>
    <div class="w-full h-[250px] relative flex flex-col px-2 pt-4 mt-3">
      <svg
        width="365"
        height="240"
        viewBox="0 0 365 240"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        class="absolute inset-0 w-full h-full rounded-[10px]"
        preserveAspectRatio="xMidYMid slice"
        style="width: 100%; height: 100%; object-fit: cover;"
      >
        <g clip-path="url(#clip0_1170_1652)">
          <rect width="365" height="240" rx="11" fill="white"></rect>
          <rect x="0.5" y="0.5" width="364" height="248" rx="9.5" fill="#131417"></rect>
          <rect x="0.5" y="0.5" width="364" height="248" rx="9.5" fill="url(#paint0_linear_1170_1652)"></rect>
          <rect x="0.5" y="0.5" width="364" height="248" rx="9.5" stroke="#2A2B2D"></rect>
          <g filter="url(#filter0_f_1170_1652)">
            <rect x="162" y="18" width="47.1625" height="36" fill="#7CFA04"></rect>
          </g>
        </g>
        <defs>
          <filter
            id="filter0_f_1170_1652"
            x="-19"
            y="-163"
            width="409.163"
            height="398"
            filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB"
          >
            <feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood>
            <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"></feBlend>
            <feGaussianBlur stdDeviation="90.5" result="effect1_foregroundBlur_1170_1652"></feGaussianBlur>
          </filter>
          <linearGradient
            id="paint0_linear_1170_1652"
            x1="207.067"
            y1="-0.00000294581"
            x2="298.488"
            y2="190.706"
            gradientUnits="userSpaceOnUse"
          >
            <stop stop-color="#141518"></stop>
            <stop offset="1" stop-color="#1E2025"></stop>
          </linearGradient>
          <clipPath id="clip0_1170_1652">
            <rect width="365" height="240" rx="11" fill="white"></rect>
          </clipPath>
        </defs>
      </svg>
      <div class="z-30 flex flex-col">
        <div
          class="w-full h-[26px] bg-[#1E2025] rounded-t-[12px] border border-[#2A2B2D] flex items-center pl-3 space-x-[10px]"
        >
          <div class="w-[10px] h-[10px] rounded-full bg-[#D9D9D9]"></div>
          <div class="w-[10px] h-[10px] rounded-full bg-[#D9D9D9] opacity-70"></div>
          <div class="w-[10px] h-[10px] rounded-full bg-[#D9D9D9] opacity-20"></div>
        </div>
        <div
          class="h-[94px] bg-[#0B0B0B] rounded-b-[12px] pt-[6px] px-3 flex flex-col overflow-hidden"
        >
          <p class="text-[10px] text-[#85F906] font-mono" style="opacity: 1;">
            $ sudo ./royale_trading_init
          </p>
          <div class="flex flex-col space-y-[2px] mt-1">
            <div 
              v-for="(message, index) in displayedMessages" 
              :key="`${cycleCount}-${index}`" 
              class="text-[10px] text-[#85F906] font-mono transition-opacity duration-500 pl-2"
              :class="{ 'opacity-0': message.isHiding }"
            >
              > {{ message.text }}
            </div>
          </div>
        </div>
        <div class="flex items-center justify-between mt-2">
          <p class="text-[14px] text-[#828282]">Покупка</p>
          <p class="text-[14px] text-[#828282]">Продажа</p>
        </div>
        <div class="flex w-full h-[60px]">
          <div class="w-1/2 flex flex-col justify-end space-y-1 pr-2 overflow-hidden">
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span
                class="text-[12px] font-mono opacity-50"
                style="color: rgb(3, 255, 0);"
              >
                $45069.29
              </span>
            </div>
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span
                class="text-[12px] font-mono opacity-50"
                style="color: rgb(3, 255, 0);"
              >
                $45074.64
              </span>
            </div>
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span class="text-[12px] font-mono" style="color: rgb(3, 255, 0); opacity: 1;">
                $45068.59
              </span>
            </div>
          </div>
          <div class="w-1/2 flex flex-col justify-end space-y-1 pl-2 overflow-hidden">
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span
                class="text-[12px] font-mono opacity-50"
                style="color: rgb(255, 0, 5);"
              >
                $44894.27
              </span>
            </div>
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span
                class="text-[12px] font-mono opacity-50"
                style="color: rgb(255, 0, 5);"
              >
                $44888.58
              </span>
            </div>
            <div class="flex justify-between">
              <span class="text-[12px] text-white">BTC/USD</span>
              <span class="text-[12px] font-mono" style="color: rgb(255, 0, 5); opacity: 1;">
                $44894.16
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// Пул сообщений для терминала
const messagePool = [
  'Initializing trading system...',
  'Connecting to blockchain network...',
  'Analyzing market data...',
  'Executing smart contracts...',
  'Scanning for profitable opportunities...',
  'Optimizing trading algorithms...',
  'Verifying transaction signatures...',
  'Loading market indicators...',
  'Calculating risk parameters...',
  'Establishing secure connections...',
  'Monitoring price fluctuations...',
  'Processing order book data...',
  'Activating auto-trading mode...',
  'Synchronizing wallet balances...',
  'Deploying trading strategies...',
  'Checking network latency...',
  'Validating trading pairs...',
  'Updating market liquidity...',
  'Configuring stop-loss limits...',
  'Initializing profit targets...'
]

// Реактивные данные
const displayedMessages = ref([])
const cycleCount = ref(0)
let currentMessageIndex = 0
let currentCycleMessages = []
let typingInterval = null
let nextMessageTimeout = null
let isTyping = false

// Функция для получения случайных сообщений
const getRandomMessages = (count = 4) => {
  const shuffled = [...messagePool].sort(() => 0.5 - Math.random())
  return shuffled.slice(0, count)
}

// Функция для анимации печати одного сообщения
const typeMessage = (fullText) => {
  return new Promise((resolve) => {
    let currentText = ''
    let charIndex = 0
    
    // Добавляем новое пустое сообщение
    const messageIndex = displayedMessages.value.length
    displayedMessages.value.push({ text: '', isHiding: false })
    
    typingInterval = setInterval(() => {
      currentText += fullText[charIndex]
      displayedMessages.value[messageIndex].text = currentText
      charIndex++
      
      if (charIndex >= fullText.length) {
        clearInterval(typingInterval)
        typingInterval = null
        resolve()
      }
    }, 50) // Скорость печати - 50мс между символами
  })
}

// Функция для показа следующего сообщения
const showNextMessage = async () => {
  if (isTyping || currentMessageIndex >= currentCycleMessages.length) return
  
  isTyping = true
  const message = currentCycleMessages[currentMessageIndex]
  
  await typeMessage(message)
  currentMessageIndex++
  isTyping = false
  
  if (currentMessageIndex < currentCycleMessages.length) {
    // Показываем следующее сообщение через 1.5 секунды
    nextMessageTimeout = setTimeout(() => {
      showNextMessage()
    }, 1500)
  } else {
    // Все 4 сообщения показаны, ждем 3 секунды и начинаем исчезновение
    nextMessageTimeout = setTimeout(() => {
      hideMessagesAndStartNewCycle()
    }, 3000)
  }
}

// Функция для скрытия сообщений и начала нового цикла
const hideMessagesAndStartNewCycle = () => {
  // Помечаем все сообщения для исчезновения
  displayedMessages.value.forEach(message => {
    message.isHiding = true
  })
  
  // Через 500ms (время анимации) очищаем и начинаем новый цикл
  setTimeout(() => {
    startNewCycle()
  }, 500)
}

// Функция для начала нового цикла
const startNewCycle = () => {
  // Очищаем сообщения и сбрасываем счетчики
  displayedMessages.value = []
  currentMessageIndex = 0
  cycleCount.value++
  
  // Получаем новые случайные сообщения
  currentCycleMessages = getRandomMessages(4)
  
  // Начинаем показ с первого сообщения
  setTimeout(() => {
    showNextMessage()
  }, 500)
}

// Функция для очистки таймаутов и интервалов
const clearAllTimeouts = () => {
  if (typingInterval) {
    clearInterval(typingInterval)
    typingInterval = null
  }
  if (nextMessageTimeout) {
    clearTimeout(nextMessageTimeout)
    nextMessageTimeout = null
  }
}

// Инициализация при монтировании компонента
onMounted(() => {
  // Небольшая задержка перед началом анимации
  setTimeout(() => {
    startNewCycle()
  }, 1000)
})

// Очистка при размонтировании
onUnmounted(() => {
  clearAllTimeouts()
})
</script>
  
  <style scoped>
  /* Add any custom styles here if needed beyond Tailwind */
  </style>