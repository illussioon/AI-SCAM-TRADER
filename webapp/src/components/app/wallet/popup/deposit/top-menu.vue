<template>
    <div>
      <!-- Tab list container -->
      <div 
        role="tablist" 
        aria-orientation="horizontal" 
        data-slot="tabs-list" 
        class="bg-[#27282A] inline-flex h-[45px] items-center justify-center rounded-lg p-[3px] w-full" 
        tabindex="0" 
        data-orientation="horizontal" 
        style="outline: none;"
      >
        <button 
          v-for="tab in tabs" 
          :key="tab.name"
          type="button" 
          role="tab" 
          :aria-selected="currentTab === tab.name" 
          :aria-controls="`tab-content-${tab.name}`" 
          :data-state="currentTab === tab.name ? 'active' : 'inactive'" 
          :id="`tab-trigger-${tab.name}`" 
          data-slot="tabs-trigger" 
          class="data-[state=active]:text-white text-[#6E6F70] text-[20px] font-normal data-[state=active]:font-semibold dark:data-[state=active]:bg-[#3C3D42] inline-flex h-[41px] flex-1 items-center justify-center gap-1.5 rounded-md border border-transparent px-2 py-1 whitespace-nowrap transition-[color,box-shadow] disabled:pointer-events-none disabled:opacity-50 data-[state=active]:shadow-sm [&_svg]:pointer-events-none [&_svg]:shrink-0 [&_svg:not([class*='size-'])]:size-4" 
          :tabindex="currentTab === tab.name ? 0 : -1" 
          data-orientation="horizontal" 
          data-radix-collection-item=""
          @click="currentTab = tab.name"
        >
          {{ tab.label }}
        </button>
      </div>
  
      <!-- Tab panels container -->
      <div class="mt-4">
        <!-- This part is responsible for outputting the deposit section -->
        <div 
          v-show="currentTab === 'deposit'" 
          role="tabpanel" 
          :id="`tab-content-deposit`"
          class=""
        >
         <Deposit />
        </div>
  
        <!-- This part is responsible for outputting the withdrawal section -->
        <div 
          v-show="currentTab === 'withdrawal'" 
          role="tabpanel" 
          :id="`tab-content-withdrawal`"
          class=""
        >
          <Witdraft />
        </div>
  
        <!-- This part is responsible for outputting the history section -->
        <div 
          v-show="currentTab === 'history'" 
          role="tabpanel" 
          :id="`tab-content-history`"
          class=""
        >
        <History />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import Witdraft from './withdrawal.vue'
  import History from './history.vue'
  import Deposit from './dep.vue'
  
  const currentTab = ref('deposit')
  
  const tabs = [
    { name: 'deposit', label: 'Депозит' },
    { name: 'withdrawal', label: 'Вывод' },
    { name: 'history', label: 'История' }
  ]
  </script>