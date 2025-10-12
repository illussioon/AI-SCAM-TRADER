<template>
  <div class="mt-4">
    <!-- Tab navigation -->
    <div class="flex justify-between border-b border-white/10 relative">
      <!-- Animated glow effect -->
      <div 
        class="absolute bottom-0 h-[20px] opacity-20 blur-[4px] transition-all duration-300 ease-out" 
        :style="{
          left: glowPosition.left,
          width: glowPosition.width,
          background: 'linear-gradient(353.81deg, rgb(144, 247, 5) -68.16%, rgba(144, 247, 5, 0) 94.31%)'
        }"
      ></div>
      
      <!-- Animated line indicator -->
      <div 
        class="absolute bottom-0 h-px bg-[#90F705] transition-all duration-300 ease-out" 
        :style="{
          left: glowPosition.left,
          width: glowPosition.width
        }"
      ></div>
      
      <!-- Tab buttons -->
      <button
        v-for="(tab, index) in tabs"
        :key="index"
        ref="tabRefs"
        @click="activeTab = index"
        :class="[
          'relative w-full px-4 pb-2 text-sm font-semibold transition-colors duration-200',
          activeTab === index ? 'text-white' : 'text-white/20 hover:text-white/70'
        ]"
      >
        {{ tab }}
      </button>
    </div>
    
    <!-- Tab content -->
    <div class="tab-content">
      <!-- Новости таб -->
      <div v-if="activeTab === 0">
        <div class="text-center text-white/60 py-8">
            <div style="margin: 6px;">
          <Nesw />
        </div>
        </div>  
      </div>
      
      <!-- Тарифы таб -->
      <div v-if="activeTab === 1">
        <div style="margin: 6px;">
          <LiveTransaction />
        </div>
        <div style="margin: 6px;">
          <Tarifs />
        </div>
        <div style="margin: -4px 8px 0 8px;">
          <NEWSslider />
        </div>
      </div>
      
      <!-- FAQ таб -->
      <div v-if="activeTab === 2">
        <div class="text-center text-white/60 py-8">
          FAQ контент будет здесь
        </div>
      </div>
    </div>
  </div>
</template>
  
  <script setup>
  import Tarifs from './app-main-content/tarifs.vue'
  import NEWSslider from './app-main-content/NEWS-slider.vue'
  import LiveTransaction from './app-main-content/live-transaction.vue'
  import Nesw from './app-main-content/news-main.vue'
  import { ref, computed, onMounted, nextTick } from 'vue'
  
  const tabs = ['Новости', 'Тарифы', 'FAQ']
  const activeTab = ref(0)
  const tabRefs = ref([])
  
  const glowPosition = computed(() => {
    if (tabRefs.value.length === 0) {
      return { left: '0px', width: '0px' }
    }
    
    const activeButton = tabRefs.value[activeTab.value]
    if (!activeButton) {
      return { left: '0px', width: '0px' }
    }
    
    const left = activeButton.offsetLeft
    const width = activeButton.offsetWidth
    
    return {
      left: `${left}px`,
      width: `${width}px`
    }
  })
  </script>