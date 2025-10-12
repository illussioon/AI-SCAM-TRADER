<template>
    <div class="sticky top-[6px] z-10 w-full overflow-hidden border border-white/10 bg-[#282828]/[0.01] backdrop-blur-[11.03px]">
      <div class="relative mx-auto max-w-md">
        <!-- Gradient blur effect -->
        <div class="pointer-events-none absolute left-0 top-[25px] h-[29px] w-full opacity-40">
          <div class="h-full w-full rounded-[12px] bg-gradient-to-b from-[#D9D9D9] to-[#636668] blur-[40.82px]"></div>
        </div>
  
        <div class="mx-auto max-w-md overflow-hidden">
          <div class="animate-marquee flex gap-6 whitespace-nowrap py-1 text-xs/5 opacity-90" style="width: 200%;">
            <!-- Render the list of cryptocurrencies twice for a seamless loop -->
            <div v-for="crypto in cryptoData" :key="crypto.alt" class="flex shrink-0 items-center gap-1">
              <CryptoIcon 
                v-if="crypto.iconName" 
                :name="crypto.iconName" 
                class="w-3 h-3 rounded-full -translate-y-0.5" 
              />
              <img 
                v-else
                :alt="crypto.alt" 
                class="w-3 h-3 rounded-full -translate-y-0.5" 
                :src="crypto.iconSrc" 
              />
              <span class="font-medium">{{ crypto.alt }}</span>
              <span class="ml-1">{{ crypto.price }}</span>
              <span :class="crypto.change.includes('+') ? 'text-green-400' : 'text-red-400'">
                {{ crypto.change }}
              </span>
            </div>
            <!-- Second set of items for the animation -->
             <div v-for="crypto in cryptoData" :key="crypto.alt + '-clone'" class="flex shrink-0 items-center gap-1">
              <CryptoIcon 
                v-if="crypto.iconName" 
                :name="crypto.iconName" 
                class="w-4 h-4 rounded-full -translate-y-0.5" 
              />
              <img 
                v-else
                :alt="crypto.alt" 
                class="w-4 h-4 rounded-full -translate-y-0.5" 
                :src="crypto.iconSrc" 
              />
              <span class="font-medium">{{ crypto.alt }}</span>
              <span class="ml-1">{{ crypto.price }}</span>
              <span :class="crypto.change.includes('+') ? 'text-green-400' : 'text-red-400'">
                {{ crypto.change }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import CryptoIcon from '../icon.vue';

// Реактивные данные для криптовалют
const cryptoData = ref([
  {
    id: 'solana',
    alt: 'SOL',
    iconName: 'solana',
    price: '$0.00',
    change: '(0.00%)',
  },
  {
    id: 'ethereum',
    alt: 'ETH',
    iconSrc: '/icon/eth.svg',
    price: '$0.00',
    change: '(0.00%)',
  },
  {
    id: 'bitcoin',
    alt: 'BTC',
    iconSrc: '/icon/btc.svg',
    price: '$0.00',
    change: '(0.00%)',
  },
  {
    id: 'the-open-network',
    alt: 'TON',
    iconSrc: '/icon/ton.svg',
    price: '$0.00',
    change: '(0.00%)',
  },
  {
    id: 'litecoin',
    alt: 'LTC',
    iconSrc: '/icon/ltc.svg',
    price: '$0.00',
    change: '(0.00%)',
  },
]);

let updateInterval = null;

// Функция загрузки актуальных цен
async function loadPrices() {
  try {
    const coins = cryptoData.value.map(coin => coin.id).join(',');
    const url = `https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=${coins}&price_change_percentage=24h`;
    
    const response = await fetch(url);
    const data = await response.json();
    
    // Обновляем данные криптовалют
    cryptoData.value = cryptoData.value.map(coin => {
      const apiData = data.find(item => item.id === coin.id);
      if (apiData) {
        const change = apiData.price_change_percentage_24h;
        const changeFormatted = change >= 0 ? `(+${change.toFixed(2)}%)` : `(${change.toFixed(2)}%)`;
        
        return {
          ...coin,
          price: `$${apiData.current_price.toLocaleString('en-US', { 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
          })}`,
          change: changeFormatted,
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
  
<style scoped>
/* Улучшенная анимация для бесконечной прокрутки без отброски */
.animate-marquee {
  animation: marquee 30s linear infinite;
  will-change: transform;
}

@keyframes marquee {
  0% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(-50%);
  }
}

/* Дополнительные стили для улучшения производительности */
.animate-marquee {
  backface-visibility: hidden;
  perspective: 1000px;
}
</style>