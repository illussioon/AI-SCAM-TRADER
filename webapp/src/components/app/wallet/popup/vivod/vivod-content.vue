<template>
    <div class="flex flex-col" :class="{ 'relative': true }">
      <button
        type="button"
        role="combobox"
        :aria-controls="`select-content-${id}`"
        :aria-expanded="isOpen"
        aria-autocomplete="none"
        dir="ltr"
        :data-state="isOpen ? 'open' : 'closed'"
        data-slot="select-trigger"
        data-size="default"
        class="border-input data-[placeholder]:text-muted-foreground [&_svg:not([class*='text-'])]:text-muted-foreground focus-visible:border-ring focus-visible:ring-ring/50 aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive dark:bg-[#27282A] dark:hover:bg-input/50 flex items-center justify-between gap-2 rounded-[17px] bg-transparent px-3 py-2 text-[20px] whitespace-nowrap shadow-xs transition-[color,box-shadow] outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50 data-[size=default]:h-[47px] data-[size=sm]:h-[47px] *:data-[slot=select-value]:line-clamp-1 *:data-[slot=select-value]:flex *:data-[slot=select-value]:items-center *:data-[slot=select-value]:gap-2 [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4 w-full mb-3"
        @click="toggleSelect"
      >
        <div class="flex items-center gap-2">
          <span data-slot="select-value" style="pointer-events: none;">
            <div class="flex items-center gap-2">
              <img
                :alt="selectedMethod"
                class="w-5 h-5 -translate-y-[2px]"
                loading="eager"
                decoding="async"
                draggable="false"
                :src="selectedIcon"
              />
              <span>{{ selectedMethod }}</span>
            </div>
          </span>
        </div>
        <svg
          viewBox="0 0 15 16"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          width="15"
          height="16"
          fill="none"
          customFrame="#000000"
          class="opacity-50 transition-transform duration-200"
          :class="{ 'rotate-180': isOpen }"
          aria-hidden="true"
        >
          <rect id="Symbol 1" width="15" height="16" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
          <path
            id="Polygon 3"
            d="M12.3657 5.05662C12.9771 5.69193 12.5268 6.75 11.6452 6.75L3.35484 6.75C2.47318 6.75 2.02294 5.69193 2.63426 5.05662L6.77942 0.748845C7.17282 0.340012 7.82718 0.340012 8.22058 0.748845L12.3657 5.05662Z"
            fill="rgb(143.438,143.438,143.438)"
            fill-rule="evenodd"
          ></path>
          <path
            id="Polygon 4"
            d="M12.3657 5.05662C12.9771 5.69193 12.5268 6.75 11.6452 6.75L3.35484 6.75C2.47318 6.75 2.02294 5.69193 2.63426 5.05662L6.77942 0.748845C7.17282 0.340012 7.82718 0.340012 8.22058 0.748845L12.3657 5.05662Z"
            fill="rgb(143.438,143.438,143.438)"
            fill-rule="evenodd"
            transform="matrix(1,0,0,-1,0,16)"
          ></path>
        </svg>
      </button>
  
      <div
        v-if="isOpen"
        :id="`select-content-${id}`"
        role="listbox"
        class="absolute z-50 w-full bottom-[calc(45%)] left-0 bg-white dark:bg-[#27282A] border border-input rounded-[17px] shadow-lg max-h-60 overflow-y-auto"
      >
        <div
          v-for="option in options"
          :key="option.name"
          class="flex items-center justify-between gap-2 px-3 py-2 cursor-pointer hover:bg-gray-100 dark:hover:bg-input/50 text-[18px] transition-colors"
          @click="selectOption(option)"
        >
          <div class="flex items-center gap-2">
            <img
              :alt="option.name"
              class="w-5 h-5 -translate-y-[2px]"
              loading="eager"
              decoding="async"
              draggable="false"
              :src="option.icon"
            />
            <span>{{ option.name }}</span>
          </div>
          <svg 
            v-if="selectedMethod === option.name"
            viewBox="0 0 16 16" 
            xmlns="http://www.w3.org/2000/svg" 
            width="16" 
            height="16" 
            fill="none"
            class="text-primary"
          >
            <path d="M13.8536 3.85355C14.0488 3.65829 14.0488 3.34171 13.8536 3.14645C13.6583 2.95118 13.3417 2.95118 13.1464 3.14645L6 10.2929L2.85355 7.14645C2.65829 6.95118 2.34171 6.95118 2.14645 7.14645C1.95118 7.34171 1.95118 7.65829 2.14645 7.85355L5.64645 11.3536C5.84171 11.5488 6.15829 11.5488 6.35355 11.3536L13.8536 3.85355Z" fill="#90F705" fill-rule="evenodd"/>
          </svg>
        </div>
      </div>
  
      <div class="mb-4">
        <input
          data-slot="input"
          class="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-[#27282A] border-input flex h-[47px] w-full min-w-0 placeholder:font-normal rounded-[17px] bg-transparent px-3 pt-1 text-[17px] font-semibold transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive placeholder:text-[17px]"
          :placeholder="inputPlaceholder"
          inputmode="text"
          type="text"
          v-model="cardNumber"
        />
      </div>
  
      <div class="mb-2">
        <input
          data-slot="input"
          class="file:text-foreground placeholder:text-muted-foreground selection:bg-primary selection:text-primary-foreground dark:bg-[#27282A] border-input flex h-[47px] w-full min-w-0 placeholder:font-normal rounded-[17px] bg-transparent px-3 pt-1 text-[17px] font-semibold transition-[color,box-shadow] outline-none file:inline-flex file:h-7 file:border-0 file:bg-transparent file:text-sm file:font-medium disabled:pointer-events-none disabled:cursor-not-allowed disabled:opacity-50 md:text-sm focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive placeholder:text-[17px]"
          placeholder="Мин. сумма: 50₽"
          inputmode="numeric"
          type="text"
          v-model="amount"
          @input="handleAmountInput"
        />
      </div>
  
      <p class="text-[16px] opacity-40">Ваш текущий баланс: {{ balance }}₽</p>
  
      <div class="h-[47px] w-full border border-[#595959] rounded-[17px] flex items-center justify-between pl-[10px] pr-[14px] mt-3">
        <p class="text-[17px] opacity-50">На счет поступит:</p>
        <p class="text-[16px]">{{ amount || '0' }}₽</p>
      </div>
  
      <button
        data-slot="button"
        class="inline-flex items-center justify-center gap-2 whitespace-nowrap font-semibold transition-all disabled:pointer-events-none disabled:opacity-50 outline-none w-full mb-20 text-black h-[48px] text-[18px] mt-6 rounded-[17px] bg-gradient-to-b from-[#B3F106] to-[#5EFF03] hover:opacity-90 active:scale-[0.98]"
        @click="handleWithdraw"
      >
        Вывести средства
      </button>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue'
  
  const props = defineProps({
    id: {
      type: String,
      default: 'select-1'
    }
  })
  
  const emit = defineEmits(['select'])
  
  const options = ref([
    {
      name: 'Банковская карта',
      icon: '/icon/card.svg'
    },
    {
      name: 'СБП',
      icon: '/icon/sbp2.svg'
    },
    {
      name: 'Toncoin',
      icon: '/icon/ton.svg'
    },
    {
      name: 'Tether',
      icon: '/icon/teher.webp'
    }
  ])
  
  const selectedMethod = ref('Банковская карта')
  const selectedIcon = ref(options.value[0].icon)
  const cardNumber = ref('')
  const amount = ref('')
  const balance = ref(0.0)
  const isOpen = ref(false)
  
  const inputPlaceholder = computed(() => {
    switch(selectedMethod.value) {
      case 'Банковская карта':
        return 'Номер банковской карты'
      case 'СБП':
        return 'Номер телефона'
      case 'Toncoin':
        return 'Адрес кошелька TON'
      case 'Tether':
        return 'Адрес кошелька USDT'
      default:
        return 'Введите данные'
    }
  })
  
  const toggleSelect = () => {
    isOpen.value = !isOpen.value
  }
  
  const selectOption = (option) => {
    selectedMethod.value = option.name
    selectedIcon.value = option.icon
    cardNumber.value = '' // Очищаем поле при смене метода
    isOpen.value = false
    emit('select', option)
  }
  
  // Close dropdown when clicking outside
  onMounted(() => {
    const handleClickOutside = (event) => {
      const target = event.target.closest(`#select-content-${props.id}`)
      if (!target && !event.target.closest('button[role="combobox"]')) {
        isOpen.value = false
      }
    }
    document.addEventListener('click', handleClickOutside)
    return () => {
      document.removeEventListener('click', handleClickOutside)
    }
  })
  
  const handleAmountInput = (event) => {
    // Разрешаем только цифры
    const value = event.target.value
    const filteredValue = value.replace(/[^0-9]/g, '')
    amount.value = filteredValue
  }
  
  const handleWithdraw = () => {
    // Add withdrawal logic here
    console.log('Withdrawing:', { method: selectedMethod.value, cardNumber: cardNumber.value, amount: amount.value })
  }
  </script>