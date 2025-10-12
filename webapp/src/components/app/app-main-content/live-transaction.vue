<template>
    <section class="mt-5">
      <div class="flex items-center gap-2">
        <div class="w-[9px] h-[9px] rounded-full bg-[#90F705] shadow-[0_0_20px_4px_#5EFF0366,0_0_0_4px_rgba(144,247,5,0.1)] waving-glow"></div>
        <h2 class="font-semibold text-xl">Live транзакции:</h2>
      </div>
      
      <div class="mt-3 space-y-2">
        <div class="space-y-2" style="position: relative; opacity: 1; filter: blur(0px);">
          <div 
            v-for="transaction in transactions" 
            :key="transaction.id"
            class="flex items-center gap-3 rounded-xl bg-gradient-to-b from-[#1A1C20]/80 to-[#0F1013]/40 p-2 h-[52px]"
          >
            <div class="relative">
              <div class="w-full h-full rounded-full border-2" :style="{ borderColor: transaction.borderColor }">
                <img 
                  class="w-[35px] h-[35px] object-cover rounded-full" 
                  src="/img/avatar.webp"
                  alt="Avatar"
                >
              </div>
              <div 
                class="absolute -bottom-1 left-[0px] flex items-center gap-[2px] px-2 py-[2px] rounded-md font-bold text-[8px]"
                :class="transaction.cryptoClass"
                :style="{ backgroundColor: transaction.borderColor }"
              >
                <img 
                  :alt="transaction.cryptoName" 
                  class="block w-[10px]" 
                  :src="transaction.cryptoIcon"
                >
                <p class="leading-none mt-[2px]">{{ transaction.cryptoName }}</p>
              </div>
            </div>
            
            <div class="flex-1">
              <div class="flex-col items-center gap-1">
                <p 
                  class="text-[18px]"
                  :class="transaction.type === 'deposit' ? 'text-[#1AE268]' : 'text-[#E41C1F]'"
                >
                  {{ transaction.typeText }}
                </p>
                <p class="text-[12px] text-white/40 -mt-1">ID: {{ transaction.id }}</p>
              </div>
            </div>
            
            <div class="text-right flex flex-col mt-1">
              <div class="text-[13px]">{{ transaction.time }}</div>
              <div 
                class="text-[18px] -mt-[2px]"
                :class="transaction.type === 'deposit' ? 'text-[#1AE268]' : 'text-[#E41B1F]'"
              >
                {{ transaction.amount }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const transactions = ref([
    {
      id: '140213313',
      type: 'deposit',
      typeText: 'Пополнение',
      borderColor: 'rgb(0, 176, 219)',
      cryptoName: 'TON',
      cryptoClass: '',
      cryptoIcon: "data:image/svg+xml,%3csvg%20viewBox='0%200%207.78821%205.84106'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%20width='7.788208'%20height='5.841064'%20fill='none'%3e%3crect%20id='token:ton'%20width='7.788235'%20height='5.841177'%20x='0.000000'%20y='0.000000'%20fill='rgb(255,255,255)'%20fill-opacity='0'%20/%3e%3cpath%20id='Vector'%20d='M6.70468%201.36934L4.15858%205.42377C4.12743%205.47287%204.08435%205.51327%204.03335%205.54121C3.98235%205.56914%203.9251%205.58369%203.86696%205.5835C3.80881%205.5833%203.75166%205.56837%203.70085%205.5401C3.65004%205.51182%203.60723%205.47113%203.57641%205.42182L1.07996%201.36739C1.00989%201.2539%200.973013%201.12305%200.973516%200.989665C0.976506%200.792625%201.05764%200.604841%201.19906%200.467612C1.34049%200.330383%201.53064%200.254947%201.72768%200.257896L6.06378%200.257896C6.47818%200.257571%206.81469%200.584028%206.81469%200.987718C6.81469%201.12174%206.77705%201.25414%206.70468%201.36934ZM1.69328%201.23305L3.55045%204.09717L3.55045%200.944883L1.88734%200.944883C1.69523%200.944883%201.60923%201.07209%201.69328%201.2337M4.23744%204.09782L6.09525%201.23305C6.18125%201.07177%206.09331%200.944234%205.90087%200.944234L4.23808%200.944234L4.23744%204.09782Z'%20fill='rgb(255,255,255)'%20fill-rule='nonzero'%20/%3e%3c/svg%3e",
      time: '18:39:39',
      amount: '+920₽'
    },
    {
      id: '140213313-2',
      type: 'deposit',
      typeText: 'Пополнение',
      borderColor: 'rgb(17, 192, 167)',
      cryptoName: 'ETH',
      cryptoClass: '',
      cryptoIcon: "data:image/svg+xml,%3csvg%20viewBox='0%200%205.21692%208.34521'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%20width='5.216919'%20height='8.345215'%20fill='none'%20customFrame='%23000000'%3e%3cg%20id='Group'%3e%3cpath%20id='Vector'%20d='M2.60767%200L2.60767%203.08493L5.21508%204.25004L2.60767%200Z'%20fill='rgb(255,255,255)'%20fill-opacity='0.601999998'%20fill-rule='nonzero'%20/%3e%3cpath%20id='Vector'%20d='M2.60776%200L0%204.25004L2.60776%203.08493L2.60776%200Z'%20fill='rgb(255,255,255)'%20fill-rule='nonzero'%20/%3e%3cpath%20id='Vector'%20d='M2.60767%206.24895L2.60767%208.34511L5.21682%204.73535L2.60767%206.24895Z'%20fill='rgb(255,255,255)'%20fill-opacity='0.601999998'%20fill-rule='nonzero'%20/%3e%3cpath%20id='Vector'%20d='M2.60776%208.34511L2.60776%206.2486L0%204.73535L2.60776%208.34511Z'%20fill='rgb(255,255,255)'%20fill-rule='nonzero'%20/%3e%3cpath%20id='Vector'%20d='M2.60767%205.76406L5.21508%204.25011L2.60767%203.08569L2.60767%205.76406Z'%20fill='rgb(255,255,255)'%20fill-opacity='0.200000003'%20fill-rule='nonzero'%20/%3e%3cpath%20id='Vector'%20d='M0%204.25011L2.60776%205.76406L2.60776%203.08569L0%204.25011Z'%20fill='rgb(255,255,255)'%20fill-opacity='0.601999998'%20fill-rule='nonzero'%20/%3e%3c/g%3e%3c/svg%3e",
      time: '18:39:39',
      amount: '+920₽'
    },
    {
      id: '140213313-3',
      type: 'deposit',
      typeText: 'Пополнение',
      borderColor: 'rgb(115, 93, 237)',
      cryptoName: 'USDT',
      cryptoClass: '-left-1',
      cryptoIcon: "data:image/svg+xml,%3csvg%20viewBox='0%200%2010.3334%2010.3333'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%20width='10.333374'%20height='10.333252'%20fill='none'%3e%3crect%20id='cryptocurrency-color:usdt'%20width='10.333333'%20height='10.333333'%20x='0.000000'%20y='0.000244'%20fill='rgb(255,255,255)'%20fill-opacity='0'%20/%3e%3cg%20id='Group'%3e%3cpath%20id='Vector'%20d='M5.78724%205.61352L5.78724%205.61288C5.75172%205.61546%205.56862%205.62644%205.16013%205.62644C4.83399%205.62644%204.6044%205.61675%204.52367%205.61288L4.52367%205.61384C3.26817%205.55863%202.33106%205.34001%202.33106%205.07845C2.33106%204.81689%203.26817%204.59859%204.52367%204.54241L4.52367%205.3962C4.60569%205.40201%204.84077%205.4159%205.16562%205.4159C5.55538%205.4159%205.75075%205.39975%205.78724%205.39652L5.78724%204.54305C7.04016%204.59892%207.975%204.81753%207.975%205.07845C7.975%205.34001%207.04016%205.55798%205.78724%205.61352ZM5.78724%204.45425L5.78724%203.69023L7.53551%203.69023L7.53551%202.52515L2.7754%202.52515L2.7754%203.69023L4.52367%203.69023L4.52367%204.45393C3.10283%204.51916%202.0343%204.80074%202.0343%205.13787C2.0343%205.47499%203.10283%205.75625%204.52367%205.8218L4.52367%208.27016L5.78724%208.27016L5.78724%205.82116C7.20581%205.75593%208.27176%205.47467%208.27176%205.13787C8.27176%204.80106%207.20581%204.5198%205.78724%204.45425Z'%20fill='rgb(255,255,255)'%20fill-rule='evenodd'%20/%3e%3c/g%3e%3c/svg%3e",
      time: '18:39:39',
      amount: '+920₽'
    },
    {
      id: '140213314',
      type: 'withdrawal',
      typeText: 'Вывод средств',
      borderColor: 'rgb(61, 217, 255)',
      cryptoName: 'TON',
      cryptoClass: '',
      cryptoIcon: "data:image/svg+xml,%3csvg%20viewBox='0%200%207.78821%205.84106'%20xmlns='http://www.w3.org/2000/svg'%20xmlns:xlink='http://www.w3.org/1999/xlink'%20width='7.788208'%20height='5.841064'%20fill='none'%3e%3crect%20id='token:ton'%20width='7.788235'%20height='5.841177'%20x='0.000000'%20y='0.000000'%20fill='rgb(255,255,255)'%20fill-opacity='0'%20/%3e%3cpath%20id='Vector'%20d='M6.70468%201.36934L4.15858%205.42377C4.12743%205.47287%204.08435%205.51327%204.03335%205.54121C3.98235%205.56914%203.9251%205.58369%203.86696%205.5835C3.80881%205.5833%203.75166%205.56837%203.70085%205.5401C3.65004%205.51182%203.60723%205.47113%203.57641%205.42182L1.07996%201.36739C1.00989%201.2539%200.973013%201.12305%200.973516%200.989665C0.976506%200.792625%201.05764%200.604841%201.19906%200.467612C1.34049%200.330383%201.53064%200.254947%201.72768%200.257896L6.06378%200.257896C6.47818%200.257571%206.81469%200.584028%206.81469%200.987718C6.81469%201.12174%206.77705%201.25414%206.70468%201.36934ZM1.69328%201.23305L3.55045%204.09717L3.55045%200.944883L1.88734%200.944883C1.69523%200.944883%201.60923%201.07209%201.69328%201.2337M4.23744%204.09782L6.09525%201.23305C6.18125%201.07177%206.09331%200.944234%205.90087%200.944234L4.23808%200.944234L4.23744%204.09782Z'%20fill='rgb(255,255,255)'%20fill-rule='nonzero'%20/%3e%3c/svg%3e",
      time: '18:39:39',
      amount: '-920₽'
    }
  ]);
  </script>
  
  <style scoped>
  .waving-glow {
    animation: wave-glow 2s ease-in-out infinite;
  }
  
  @keyframes wave-glow {
    0%, 100% {
      box-shadow: 0 0 20px 4px #5EFF0366, 0 0 0 4px rgba(144, 247, 5, 0.1);
    }
    50% {
      box-shadow: 0 0 30px 6px #5EFF0388, 0 0 0 6px rgba(144, 247, 5, 0.2);
    }
  }
  </style>