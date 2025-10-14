<template>
    <div
      data-state="active"
      data-orientation="horizontal"
      role="tabpanel"
      aria-labelledby="radix-«r11»-trigger-deposit"
      id="radix-«r11»-content-deposit"
      tabindex="0"
      data-slot="tabs-content"
      class="flex-1 outline-none"
      style=""
    >
      <img
        alt="bonus"
        class="w-full mt-1"
        loading="eager"
        decoding="async"
        draggable="false"
        src="/img/pay/bonus.webp"
      />
      <p class="text-[20px] font-medium mt-2 mb-2 text-white">Банковский платеж</p>
      <div class="flex w-full gap-3 mb-4">
        <div
          class="flex-1 bg-[#212224] rounded-[11px] overflow-hidden px-[10px] pt-[16px] pb-2 h-[100px] relative cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start justify-between h-full">
            <div class="text-[16px] font-medium text-white">СБП</div>
            <div class="text-[14px] text-white/50">От 100₽</div>
          </div>
          <img
            alt="СБП"
            class="absolute -right-3 scale-100 top-1/2 top-1/2 -translate-y-1/2 "
            loading="eager"
            decoding="async"
            draggable="false"
            src="/img/pay/sbp.webp"
          />
        </div>
        <div
          class="flex-1 bg-[#212224] rounded-[11px] px-[10px] pt-[16px] pb-2 h-[100px] relative overflow-hidden cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start justify-between h-full">
            <div class="text-[16px] font-medium text-white z-20 text-white">Перевод на карту</div>
            <div class="text-[14px] text-white/50">От 100₽</div>
          </div>
          <img
            alt="cards"
            class="absolute scale-50 -right-10 top-12 transform -translate-y-1/2"
            loading="eager"
            decoding="async"
            draggable="false"
            src="/img/pay/cards.webp"
          />
        </div>
      </div>
      <p class="text-[20px] mt-1 mb-1 text-white">Криптовалюта</p>
      <div class="flex w-full gap-3 mb-3">
        <div
          class="flex-1 bg-[#212224] rounded-[11px] px-[10px] pt-[16px] pb-2 h-[100px] relative overflow-hidden cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start">
            <div class="text-[16px] text-white">(BTC)</div>
            <div class="text-[16px] text-white">Bitcoin</div>
          </div>
          <div class="absolute -right-0 -bottom-0 w-[112px] h-[100px]">
            <img
              alt="btc"
              class="w-full h-full object-contain"
              loading="eager"
              decoding="async"
              draggable="false"
              src="/img/pay/btc.webp"
            />
          </div>
        </div>
        <div
          class="flex-1 bg-[#212224] rounded-[11px] px-[10px] pt-[16px] pb-2 h-[100px] relative overflow-hidden cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start">
            <div class="text-[16px] text-white">(TON)</div>
            <div class="text-[16px] text-white">Toncoin</div>
          </div>
          <div class="absolute -right-0 -bottom-1 w-[112px] h-[100px]">
            <img
              alt="ton"
              class="w-full h-full object-contain"
              loading="eager"
              decoding="async"
              draggable="false"
              src="/img/pay/ton.webp"
            />
          </div>
        </div>
      </div>
      <div class="flex w-full gap-3 mb-4">
        <div
          class="flex-1 bg-[#212224] rounded-[11px] px-[10px] pt-[16px] pb-2 h-[100px] relative overflow-hidden cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start">
            <div class="text-[16px] text-white">(USDT)</div>
            <div class="text-[16px] text-white">Tether</div>
          </div>
          <div class="absolute -right-0 -bottom-0 w-[112px] h-[100px]">
            <img
              alt="usdt"
              class="w-full h-full object-contain"
              loading="eager"
              decoding="async"
              draggable="false"
              src="/img/pay/usdt.webp"
            />
          </div>
        </div>
        <div
          class="flex-1 bg-[#212224] rounded-[11px] px-[10px] pt-[16px] pb-2 h-[100px] relative overflow-hidden cursor-pointer hover:bg-[#2a2a2c] transition-colors"
        >
          <div class="flex flex-col items-start">
            <div class="text-[16px] text-white">(USDC)</div>
            <div class="text-[16px] text-white">USD Coin</div>
          </div>
          <div class="absolute -right-0 -bottom-0 w-[112px] h-[100px]">
            <img
              alt="usdc"
              class="w-full h-full object-contain"
              loading="eager"
              decoding="async"
              draggable="false"
              src="/img/pay/usdc.webp"
            />
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  // Здесь можно добавить логику, если нужно (например, обработчики для кликов по карточкам)
  </script>