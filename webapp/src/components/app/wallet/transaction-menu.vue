<template>
    <div class="h-[300px] rounded-t-[14px] bg-[rgba(19,20,23,0.7)] mt-4 px-[8px] pt-[6px] flex flex-col">
      <div class="flex gap-x-[6px]">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          @click="activeTab = tab.id"
          :class="[
            'gap-2 whitespace-nowrap disabled:pointer-events-none disabled:opacity-50',
            '[&_svg]:pointer-events-none [&_svg:not([class*=\'size-\'])]:size-4 shrink-0 [&_svg]:shrink-0',
            'outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px]',
            'aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive',
            'shadow-xs hover:bg-primary/90 px-4 py-2 has-[>svg]:px-3',
            'flex items-center justify-center box-border border-[0.55px] rounded-[72px]',
            'backdrop-blur-[11.0317px] text-[17.65px] font-semibold leading-[15px]',
            'transition-colors duration-300 ease-in-out',
            tab.width,
            'h-[33px]',
            activeTab === tab.id 
              ? 'border-[rgba(255,255,255,0.1)] bg-gradient-to-b from-[#B3F106] to-[#5EFF03] text-black'
              : 'border-[#2e3032] bg-[rgba(255,255,255,0.05)] text-white'
          ]"
          data-slot="button"
        >
          <p class="mt-1">{{ tab.label }}</p>
        </button>
      </div>
  
      <div class="flex-1 pt-[14px] pb-[8px] flex flex-col gap-y-[6px] overflow-y-auto">
        <div class="flex flex-col items-center justify-center p-4">
          <p class="text-white/70 text-sm mb-1">Операций не найдено</p>
          <p class="text-white/50 text-xs">У вас пока нет операций</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const activeTab = ref('all')
  
  const tabs = [
    { id: 'all', label: 'Все', width: 'w-[86px]' },
    { id: 'deposits', label: 'Пополнения', width: 'w-[117px]' },
    { id: 'withdrawals', label: 'Вывод', width: 'w-[88px]' }
  ]
  </script>