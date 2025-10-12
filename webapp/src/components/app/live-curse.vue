<template>
    <section class="mt-6">
      <div class="flex items-center gap-2">
        <img 
          alt="Rate" 
          src="data:image/svg+xml,%3csvg%20width='19'%20height='17'%20viewBox='0%200%2019%2017'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M2.375%201.375C2.375%200.718164%201.84434%200.1875%201.1875%200.1875C0.530664%200.1875%200%200.718164%200%201.375V13.8438C0%2015.484%201.32852%2016.8125%202.96875%2016.8125H17.8125C18.4693%2016.8125%2019%2016.2818%2019%2015.625C19%2014.9682%2018.4693%2014.4375%2017.8125%2014.4375H2.96875C2.64219%2014.4375%202.375%2014.1703%202.375%2013.8438V1.375ZM17.4637%204.58867C17.9275%204.1248%2017.9275%203.37148%2017.4637%202.90762C16.9998%202.44375%2016.2465%202.44375%2015.7826%202.90762L11.875%206.81895L9.74492%204.69258C9.28105%204.22871%208.52773%204.22871%208.06387%204.69258L4.50137%208.25508C4.0375%208.71895%204.0375%209.47227%204.50137%209.93613C4.96523%2010.4%205.71855%2010.4%206.18242%209.93613L8.90625%207.2123L11.0363%209.34238C11.5002%209.80625%2012.2535%209.80625%2012.7174%209.34238L17.4674%204.59238L17.4637%204.58867Z'%20fill='%2390F705'/%3e%3c/svg%3e"
        >
        <h2 class="font-semibold text-xl">Курс криптовалют</h2>
      </div>
  
      <table class="w-full border-collapse text-sm mt-3">
        <thead>
          <tr class="text-[14px]">
            <th class="px-3 py-2 text-left font-normal">Монеты</th>
            <th class="px-3 py-2 text-right font-normal">Цена</th>
            <th class="px-3 py-2 text-right font-normal text-white/60">24 часа</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-white/5">
          <tr v-for="crypto in cryptoData" :key="crypto.id">
            <td class="px-3 py-3">
              <div class="flex items-center gap-3">
                <CryptoIcon :name="crypto.icon" />
                <p class="font-medium text-[18px]">{{ crypto.name }}</p>
              </div>
            </td>
            <td class="px-3 py-3 text-right text-[14px] tabular-nums">{{ crypto.price }}</td>
            <td class="px-3 py-3 text-right tabular-nums">
              <div class="flex items-center justify-end gap-1">
                <span :class="crypto.change >= 0 ? 'text-[#1BE468]' : 'text-[#FF002B]'">
                  {{ crypto.change }}%
                </span>
                <div 
                  class="inline-block"
                  :class="crypto.change >= 0 ? 'triangle-up' : 'triangle-down'"
                  :style="{
                    width: '10px',
                    height: '6px',
                    borderRadius: '0.2px',
                    background: crypto.change >= 0 ? 'rgb(27, 228, 104)' : 'rgb(255, 0, 43)',
                    clipPath: crypto.change >= 0 ? 'polygon(50% 0%, 0% 100%, 100% 100%)' : 'polygon(50% 100%, 0% 0%, 100% 0%)'
                  }"
                />
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import CryptoIcon from '../icon.vue'
  
  const cryptoData = ref([
    {
      id: 1,
      icon: 'bitcoin',
      name: 'Bitcoin',
      price: '₽122 336,90',
      change: 3.91
    },
    {
      id: 2,
      icon: 'eth',
      name: 'ETH',
      price: '₽122 336,90',
      change: 3.91
    },
    {
      id: 3,
      icon: 'solana',
      name: 'Solana',
      price: '₽122 336,90',
      change: -3.91
    },
    {
      id: 4,
      icon: 'tron',
      name: 'Tron',
      price: '₽122 336,90',
      change: 3.91
    },
    {
      id: 5,
      icon: 'ton',
      name: 'Toncoin',
      price: '₽122 336,90',
      change: 3.91
    },
    {
      id: 6,
      icon: 'litecoin',
      name: 'Litecoin',
      price: '₽122 336,90',
      change: 3.91
    },
    {
      id: 7,
      icon: 'xrp',
      name: 'XRP',
      price: '₽122 345,90',
      change: 3.91
    }
  ])
  </script>