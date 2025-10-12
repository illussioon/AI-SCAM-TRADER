<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import CryptoIcon from '../../icon.vue'; // Правильный путь к компоненту

// Реактивные данные для криптовалют
const cryptocurrencies = ref([
  {
    id: 'bitcoin',
    name: 'Bitcoin',
    icon: 'bitcoin',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'ethereum',
    name: 'ETH',
    icon: 'eth',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'solana',
    name: 'Solana',
    icon: 'solana',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'tron',
    name: 'Tron',
    icon: 'tron',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'the-open-network',
    name: 'Toncoin',
    icon: 'ton',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'litecoin',
    name: 'Litecoin',
    icon: 'litecoin',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  },
  {
    id: 'ripple',
    name: 'XRP',
    icon: 'xrp',
    price: '₽0',
    change: '0%',
    changeType: 'up'
  }
]);

let updateInterval = null;

// Функция загрузки актуальных цен
async function loadPrices() {
  try {
    const coins = cryptocurrencies.value.map(coin => coin.id).join(',');
    const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=rub&ids=${coins}&price_change_percentage=24h`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    // Обновляем данные криптовалют
    cryptocurrencies.value = cryptocurrencies.value.map(coin => {
      const apiData = data.find(item => item.id === coin.id);
      if (apiData) {
        const change = apiData.price_change_percentage_24h;
        const changeFormatted = `${change.toFixed(2)}%`;
        
        return {
          ...coin,
          price: `₽${apiData.current_price.toLocaleString('ru-RU', { 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
          })}`,
          change: changeFormatted,
          changeType: change >= 0 ? 'up' : 'down'
        };
      }
      return coin;
    });
    
    console.log('Цены криптовалют обновлены');
  } catch (error) {
    console.error('Ошибка загрузки цен криптовалют:', error);
  }
}

// Монтирование компонента
onMounted(() => {
  loadPrices(); // Загружаем сразу
  updateInterval = setInterval(loadPrices, 60000); // Обновляем каждые 60 секунд
});

// Очистка при размонтировании
onUnmounted(() => {
  if (updateInterval) {
    clearInterval(updateInterval);
  }
});
</script>

<template>
  <section class="mt-6">
    <div class="flex items-center gap-2">
      <svg width="19" height="17" viewBox="0 0 19 17" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M2.375 1.375C2.375 0.718164 1.84434 0.1875 1.1875 0.1875C0.530664 0.1875 0 0.718164 0 1.375V13.8438C0 15.484 1.32852 16.8125 2.96875 16.8125H17.8125C18.4693 16.8125 19 16.2818 19 15.625C19 14.9682 18.4693 14.4375 17.8125 14.4375H2.96875C2.64219 14.4375 2.375 14.1703 2.375 13.8438V1.375ZM17.4637 4.58867C17.9275 4.1248 17.9275 3.37148 17.4637 2.90762C16.9998 2.44375 16.2465 2.44375 15.7826 2.90762L11.875 6.81895L9.74492 4.69258C9.28105 4.22871 8.52773 4.22871 8.06387 4.69258L4.50137 8.25508C4.0375 8.71895 4.0375 9.47227 4.50137 9.93613C4.96523 10.4 5.71855 10.4 6.18242 9.93613L8.90625 7.2123L11.0363 9.34238C11.5002 9.80625 12.2535 9.80625 12.7174 9.34238L17.4674 4.59238L17.4637 4.58867Z" fill="#90F705"/>
      </svg>
      <h2 class="font-semibold text-xl text-white">Курс криптовалют</h2>
    </div>
    <table class="w-full border-collapse text-sm mt-3">
      <thead>
        <tr class="text-[14px] text-white">
          <th class="px-3 py-2 text-left font-normal">Монеты</th>
          <th class="px-3 py-2 text-right font-normal">Цена</th>
          <th class="px-3 py-2 text-right font-normal text-white/60">24 часа</th>
        </tr>
      </thead>
      <tbody class="divide-y divide-white/5">
        <tr v-for="crypto in cryptocurrencies" :key="crypto.name" class="text-white">
          <td class="px-3 py-3">
            <div class="flex items-center gap-3">
              <CryptoIcon :name="crypto.icon" class="w-6 h-6" />
              <p class="font-medium text-[18px] text-white">{{ crypto.name }}</p>
            </div>
          </td>
          <td class="px-3 py-3 text-right text-[14px] tabular-nums text-white">
            {{ crypto.price }}
          </td>
          <td class="px-3 py-3 text-right tabular-nums">
            <div class="flex items-center justify-end gap-1">
              <span :class="crypto.changeType === 'up' ? 'text-[#1BE468]' : 'text-[#FF002B]'">
                {{ crypto.change }}
              </span>
              <div
                v-if="crypto.changeType === 'up'"
                class="inline-block"
                style="width: 10px; height: 6px; border-radius: 0.2px; background: rgb(27, 228, 104); clip-path: polygon(50% 0%, 0% 100%, 100% 100%);"
              ></div>
              <div
                v-if="crypto.changeType === 'down'"
                class="inline-block"
                style="width: 10px; height: 6px; border-radius: 0.2px; background: rgb(255, 0, 43); clip-path: polygon(50% 100%, 0% 0%, 100% 0%);"
              ></div>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </section>
</template>