<template>
  <div
    data-state="active"
    data-orientation="horizontal"
    role="tabpanel"
    aria-labelledby="radix-r11-trigger-history"
    id="radix-r11-content-history"
    tabindex="0"
    data-slot="tabs-content"
    class="flex-1 outline-none"
  >
    <!-- Support Image -->
    <img
      alt="support"
      class="w-full mt-1"
      loading="eager"
      decoding="async"
      draggable="false"
      src="/img/pay/support.webp"
    />

    <!-- Write Button -->
    <div class="relative">
      <button
        data-slot="button"
        class="absolute inline-flex items-center justify-center gap-2 whitespace-nowrap font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive hover:bg-primary/90 h-10 rounded-md px-6 has-[>svg]:px-4 text-[16px] text-white bg-[#54585D4D] shadow-[-1px_2px_4px_0px_#FFFFFF1A_inset] -top-12 left-5"
        @click="handleWriteClick"
      >
        Написать
      </button>
    </div>

    <!-- Empty State -->
    <div class="flex flex-col items-center justify-center p-6 -mt-18">
      <p class="text-white/70 text-lg mb-2">История пуста</p>
      <p class="text-white/50 text-sm">У вас пока нет операций</p>
    </div>

    <!-- Spacing -->
    <div class="h-20 mt-2"></div>
  </div>
</template>

<script setup>
const handleWriteClick = () => {
  // Ваша логика при клике на кнопку "Написать"
  console.log('Написать clicked')
}
</script>