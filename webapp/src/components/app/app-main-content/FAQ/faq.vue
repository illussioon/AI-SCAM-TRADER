<template>
    <div class="mt-10">
      <h2 class="flex items-center gap-2 text-[28px] font-bold text-white">
        <img alt="FAQ" src="data:image/svg+xml,%3csvg%20width='32'%20height='26'%20viewBox='0%200%2032%2026'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M3.25008%2013C1.69175%2013%200.416748%2011.725%200.416748%2010.1667V3.08333C0.416748%201.525%201.69175%200.25%203.25008%200.25H14.5834C16.1417%200.25%2017.4167%201.525%2017.4167%203.08333V10.1667C17.4167%2011.725%2016.1417%2013%2014.5834%2013H11.7501V17.25L7.50008%2013H3.25008ZM28.7501%2021.5C30.3084%2021.5%2031.5834%2020.225%2031.5834%2018.6667V11.5833C31.5834%2010.025%2030.3084%208.75%2028.7501%208.75H20.2501V10.1667C20.2501%2013.2833%2017.7001%2015.8333%2014.5834%2015.8333V18.6667C14.5834%2020.225%2015.8584%2021.5%2017.4167%2021.5H20.2501V25.75L24.5001%2021.5H28.7501Z'%20fill='black'/%3e%3cpath%20d='M3.25008%2013C1.69175%2013%200.416748%2011.725%200.416748%2010.1667V3.08333C0.416748%201.525%201.69175%200.25%203.25008%200.25H14.5834C16.1417%200.25%2017.4167%201.525%2017.4167%203.08333V10.1667C17.4167%2011.725%2016.1417%2013%2014.5834%2013H11.7501V17.25L7.50008%2013H3.25008ZM28.7501%2021.5C30.3084%2021.5%2031.5834%2020.225%2031.5834%2018.6667V11.5833C31.5834%2010.025%2030.3084%208.75%2028.7501%208.75H20.2501V10.1667C20.2501%2013.2833%2017.7001%2015.8333%2014.5834%2015.8333V18.6667C14.5834%2020.225%2015.8584%2021.5%2017.4167%2021.5H20.2501V25.75L24.5001%2021.5H28.7501Z'%20fill='%2390F705'/%3e%3c/svg%3e">
        <p>F.A.Q</p>
      </h2>
      <div class="mt-4 rounded-lg flex flex-col gap-y-2">
        <div 
          v-for="(item, index) in faqItems" 
          :key="index"
          class="p-4 cursor-pointer hover:bg-white/5 border-t"
          :class="index === 0 ? 'border-[#A5FA3C]' : 'border-[#32343E]'"
          @click="toggleItem(index)"
        >
          <div class="flex justify-between items-center text-[13px]">
            <p class="font-medium text-white">{{ item.question }}</p>
            <img 
              alt="toggle" 
              class="w-4 h-4" 
              :src="openItems[index] ? arrowUp : arrowDown"
            >
          </div>
          <div 
            class="transition-all duration-300 ease-in-out overflow-hidden"
            :class="openItems[index] ? 'max-h-40 mt-2' : 'max-h-0'"
          >
            <p class="text-[13px] text-[#A6A6A6]">{{ item.answer }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const arrowUp = "data:image/svg+xml,%3csvg%20width='14'%20height='8'%20viewBox='0%200%2014%208'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M1%207L7%201L13%207'%20stroke='white'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e";
  const arrowDown = "data:image/svg+xml,%3csvg%20width='14'%20height='8'%20viewBox='0%200%2014%208'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M1%201L7%207L13%201'%20stroke='white'%20stroke-width='2'%20stroke-linecap='round'%20stroke-linejoin='round'/%3e%3c/svg%3e";
  
  const faqItems = [
    {
      question: "Платформа Royal что это?",
      answer: "Наша платформа напрямую взаимодействует с крипто-торговыми ботами и внедрением ИИ."
    },
    {
      question: "Сколько я могу заработать?",
      answer: "В нашей платформе существует 3 тарифа, уровень вашего заработка напрямую зависит от вас."
    },
    {
      question: "Как заработать без вложений?",
      answer: "Приглашайте партнеров по своей ссылке и зарабатывайте без вложений, система из 3 уровней."
    },
    {
      question: "Сколько платформа будет работать?",
      answer: "Платформа будет работать без сроков окончания, наша цель развиваться и идти вперед."
    },
    {
      question: "Откуда берутся доходы в платформе?",
      answer: "Наш торговый бот совместно с GPT-5 выстроил первую в своем роде систему из ИИ агентов которые выступают в роле трейдеров."
    }
  ];
  
  const openItems = ref([true, false, false, false, false]);
  
  const toggleItem = (index) => {
    openItems.value[index] = !openItems.value[index];
  };
  </script>