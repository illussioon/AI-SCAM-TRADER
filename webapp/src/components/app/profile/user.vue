<template>
  <div class="flex flex-col items-center justify-center -mt-6 relative">
    <img 
      :src="telegramStore.userPhoto" 
      :alt="`${telegramStore.fullName} avatar`" 
      class="w-[100px] h-[100px] rounded-full translate-y-7 relative z-30 object-cover" 
      style="border: 2px solid #1c1e1f;"
      @error="$event.target.src = '/img/avatar.webp'"
    />
    <div class="w-full h-[78px] relative" style="background-image: url(&quot;data:image/webp;base64,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&quot;); background-size: cover; background-position: center center; background-repeat: no-repeat;">
      <div class="absolute left-1/2 transform -translate-x-1/2 flex flex-row justify-center items-center z-40" style="top: 16px; width: 90px; height: 27px; gap: 6.95px; padding: 6px 9px 4.17px; box-sizing: border-box; border: 0.5px solid rgba(255, 255, 255, 0.2); border-radius: 35px; box-shadow: rgba(0, 0, 0, 0.25) 0px 3.71501px 3.71501px 0px; backdrop-filter: blur(199.775px); background: linear-gradient(90deg, rgb(22, 23, 24) 0%, rgb(12, 13, 15) 100%), rgba(25, 26, 31, 0.1);">
        <p class="text-[12px]">ID: {{ telegramStore.userId || 'N/A' }}</p>
      </div>
      <div class="absolute top-2 left-4 flex flex-col -space-y-1">
        <p class="text-[20px]">{{ userStats?.current || 0 }}XP</p>
        <p class="text-[14px] opacity-50">{{ userStats?.level || 1 }} Уровень</p>
      </div>
      <div class="absolute top-2 right-4 flex flex-col items-end -space-y-1">
        <p class="text-[20px]">{{ userStats?.max || 100 }}XP</p>
        <p class="text-[14px] opacity-50">До {{ (userStats?.level || 1) + 1 }} уровня</p>
      </div>
      <div class="absolute bottom-2 left-4 right-4 h-2 rounded-[100px]" style="width: calc(100% - 32px); background-color: rgba(217, 217, 217, 0.1);">
        <div 
          class="h-full rounded-[100px] transition-all duration-500 ease-out" 
          :style="`width: ${xpProgressWidth}%; box-shadow: rgba(0, 0, 0, 0.4) 0px 0.351064px 1.04441px 0px inset; background: linear-gradient(rgb(179, 241, 6) 0%, rgb(94, 255, 3) 100%);`"
        ></div>
        <div 
          class="absolute top-0 h-full rounded-[100px] transition-all duration-500 ease-out" 
          :style="`width: ${xpProgressWidth}%; background: linear-gradient(rgb(179, 241, 6) 0%, rgb(94, 255, 3) 100%); filter: blur(18px); opacity: 0.3;`"
        ></div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useTelegramStore } from '../../../stores/telegram.js'
import { useUser } from '../../../composables/useUser.js'

// Инициализация stores
const telegramStore = useTelegramStore()
const { 
  userData, 
  isLoading, 
  error, 
  xpInfo: userStats,
  hasUserData,
  refreshUserData 
} = useUser()

// Вычисляемые свойства
const xpProgressWidth = computed(() => {
  if (!userStats.value) return 0
  const percentage = userStats.value.percentage || 0
  return Math.min(Math.max(percentage, 0), 100) // Ограничиваем от 0 до 100%
})

// Компонент теперь использует автоматически обновляемые данные из user store
// Никаких дополнительных методов инициализации не требуется

// Можно добавить метод для принудительного обновления, если нужно
const handleRefresh = () => {
  refreshUserData()
}
</script>