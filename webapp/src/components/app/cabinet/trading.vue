<template>
  <div
    class="w-full h-[240px] rounded-[10px] flex flex-col px-[15.4px] pt-[13px]"
    :style="{
      backgroundImage: `url('/img/trading.webp')`,
      backgroundSize: 'cover',
      backgroundPosition: 'center center',
      backgroundRepeat: 'no-repeat'
    }"
  >
    <div class="flex flex-row items-center justify-between">
      <div class="flex flex-row items-center gap-x-1">
        <div class="flex justify-center items-center h-8 w-8 bg-[#90F806] rounded-full border border-[#B7FA5C]">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" fill="none">
            <rect id="hugeicons:chat-gpt" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
            <g id="Group">
              <path id="Vector" d="M11.745 14.85L6.90503 12L6.90503 7C6.90503 4.79 8.73003 3 10.981 3C12.378 3 13.611 3.69 14.346 4.741" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path id="Vector" d="M9.6001 19.1799C9.97597 19.7417 10.4849 20.2018 11.0816 20.5193C11.6783 20.8369 12.3442 21.002 13.0201 20.9999C15.2701 20.9999 17.0961 19.2099 17.0961 16.9999L17.0961 11.9999L12.1601 9.09692" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path id="Vector" d="M9.4519 13.5001L9.4519 7.67006L13.8639 5.17006C15.8139 4.06506 18.3069 4.72006 19.4329 6.63306C19.7777 7.21625 19.9659 7.87868 19.9793 8.55606C19.9926 9.23344 19.8306 9.90276 19.5089 10.4991" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path id="Vector" d="M4.4899 13.4999C4.16811 14.0961 4.00591 14.7654 4.01905 15.4427C4.03219 16.1201 4.22023 16.7826 4.5649 17.3659C5.6909 19.2789 8.18491 19.9339 10.1349 18.8299L14.5469 16.3299L14.6429 10.7339" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path id="Vector" d="M17.096 17.6299C17.7776 17.6035 18.4418 17.4071 19.0282 17.0585C19.6145 16.7099 20.1043 16.2202 20.453 15.6339C21.578 13.7209 20.91 11.2739 18.961 10.1699L14.548 7.66992L9.48901 10.4249" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
              <path id="Vector" d="M6.90504 6.37012C6.22325 6.39632 5.55885 6.59268 4.97234 6.9413C4.38583 7.28992 3.89586 7.77973 3.54704 8.36612C2.42104 10.2791 3.08904 12.7261 5.03904 13.8301L9.45204 16.3301L14.5 13.5801" fill-rule="nonzero" stroke="rgb(0,0,0)" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"></path>
            </g>
          </svg>
        </div>
        <div class="flex flex-col h-[50px] items-start -space-y-[2px]">
          <p class="text-[18px] font-semibold">GPT-5</p>
          <div class="flex gap-x-[2px]">
            <img class="w-4 h-4" alt="Шиба" :src="shibaBase64" />
            <img class="w-4 h-4" alt="Пепе" :src="pepeBase64" />
            <img class="w-4 h-4" alt="Доге" :src="dogeBase64" />
            <p class="text-[18px] opacity-50 -translate-y-1">...</p>
          </div>
        </div>
      </div>
      <div
        class="h-[41px] bg-[#35393F] rounded-[11px] w-[163px] flex items-center justify-between px-[5px]"
        :style="{ boxShadow: 'rgba(0, 0, 0, 0.25) 3px 4px 4px 0px' }"
      >
         <div
           class="w-[77px] h-[31px] rounded-[11px] flex flex-col items-center justify-center -space-y-1 transition-all duration-200"
           :class="buyBgClass"
           :style="buyShadowStyle"
         >
           <p class="text-[15px] font-semibold" :style="{ color: buyTextColor }">
             ₽ <span>{{ buyPrice.toLocaleString() }}</span>
           </p>
           <p class="text-[10px]" :style="{ color: buyTextColor }">{{ buyText }}</p>
         </div>
         <div
           class="w-[77px] h-[31px] rounded-[11px] flex flex-col items-center justify-center -space-y-1 transition-all duration-200"
           :style="sellShadowStyle"
         >
           <p class="text-[15px] font-semibold" :style="{ color: sellTextColor }">
             ₽ <span>{{ sellPrice.toLocaleString() }}</span>
           </p>
           <p class="text-[10px]" :style="{ color: sellTextColor }">{{ sellText }}</p>
         </div>
      </div>
    </div>
    <div class="mt-1 flex-1 flex flex-col">
      <div class="flex justify-between mb-2">
        <div class="flex gap-x-[18px]">
          <p class="text-[9.1px] text-[#828282]">1сек</p>
          <p class="text-[9.1px] text-[#828282]">1 мин</p>
          <p class="text-[9.1px] text-[#828282]">2 мин</p>
          <p class="text-[9.1px] text-[#828282]">3 мин</p>
          <p class="text-[9.1px] text-[#828282]">5 мин</p>
          <p class="text-[9.1px] text-[#828282]">15 мин</p>
          <p class="text-[9.1px] text-[#828282]">30 мин</p>
          <p class="text-[9.1px] text-[#828282]">1 час</p>
        </div>
      </div>
      <div ref="chartRef" class="relative flex flex-col gap-y-3 flex-1 overflow-hidden">
        <div class="flex items-end" v-for="(price, index) in yPrices" :key="index">
          <div class="h-px bg-[#494B4F] flex-1"></div>
          <p class="text-[8px] text-[#828282] ml-2 w-[40px] text-right">
            <span>{{ price.toLocaleString() }}</span>₽
          </p>
        </div>
        <div
          class="absolute left-0 flex-1 h-px z-10 transition-all duration-500 ease-out"
          :style="cursorLineStyle"
        ></div>
        <div class="absolute inset-0 z-20">
          <div
            v-for="(candle, index) in candles"
            :key="index"
            class="relative"
            :style="{ left: `${(index * 14)}px` }"
          >
            <!-- Upper wick -->
            <div
              v-if="candle.upperWick > 0"
              class="absolute w-[1px]"
              :style="{
                left: '5px',
                height: `${candle.upperWick}px`,
                top: `${candle.highTop}px`,
                backgroundColor: candle.color
              }"
            ></div>
            <!-- Candle body -->
            <div
              class="absolute rounded-[1px]"
              :style="{
                left: '0px',
                width: '11px',
                height: `${candle.bodyHeight}px`,
                top: `${candle.bodyTop}px`,
                backgroundColor: candle.color
              }"
            ></div>
            <!-- Lower wick -->
            <div
              v-if="candle.lowerWick > 0"
              class="absolute w-[1px]"
              :style="{
                left: '5px',
                height: `${candle.lowerWick}px`,
                top: `${candle.lowTop}px`,
                backgroundColor: candle.color
              }"
            ></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, nextTick } from 'vue'

const shibaBase64 = 'data:image/webp;base64,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'
const pepeBase64 = 'data:image/webp;base64,UklGRgwEAABXRUJQVlA4WAoAAAAQAAAAPwAAPwAAQUxQSJ0BAAARgFtr25vmJ0OXKmcNATVjUDIALYyAOtIgmZYOakoN4KBDCbaF4vd9zpb+lwEiwpHbRo4kTZ7ZPXUo9xNUXDNGy5ztbYfZsfczs2VklE6LzYEVhBExy5fMFIWBNWgWdXHXtbyQ5V859KzenQ6M/sEniSn5B9NISrnz6LMkkP3HTjkJqfrWIUkoOdt6Kjalth2IBgO7XYpJbXIk0SIdJ7VYXK3fWTTJ7+urOPvmLBo9b/7fauuzaPW8/u9lafIumn2f/P1nqfaRdcPHduov6jaJdslu/NXat4EADHbl33Qcgeh0fnfVR8JAj8ZPTF9A+v2f48yBUfDh7puuLzD9nlKqaBEOsopKNT0B6jWVGoRIwoHKWIyErYwRCNTAaIVYwpYZYYnMGWGh6Z6x8N5GYzsC1mE0hAd/g/8E/0f4dovvN/h+ix838OMWfNzEj9v4eQM9b3Xx8yZ83sbXDfC6BV03bcvouq2OrxsvqW5VqrbSXzfD63Z4boDnlsvMTUqlGjtNuS1hbvSS50Z0bkXn5kvM7YnWDaa/1w2mSdYNFABWUDggSAIAAPANAJ0BKkAAQAA+aTSaTSWkpBr5cCgGgAF8gKKWorGJyADbAeYDz//QB/tN8A3lX/C/8D9gPaZTyct7TSM+E4BdKv5Yg5+syNbsOTVhEyC4LRXQM/PopJTmJdPETB8nfNBPYDEBm6sTEtFlQXVyONVzHdcYkL4qAAD+/qAj4Szr9gAI/zNdH16bAmDbxslX8SCpg8j6gd+h2oQDKyqau042qZP6COhzxdXFemAUWjp/57nxsluY+5YeVt5ym7FacuRfMmbov2d7H+XeDkhdkOFIGVGQxQ6udxB/1FOcjMDwreTETWAoaZZE4JpYqmgeovlocPsRCxC295MOySQMo6j1IY3zW7M7tzejD7+O0R3PT/qxMs/Gus6/OliSBlexVpTfXCTLigChClsqoDDj5DwYfajMtlTsBn6y1s/Mb/lzozETrr1RLwEVn8K97tWbmHaOKWtzP82/aS2Cv/TOHxOz6F/XEbwoYSOgyIp2LqbhbqG4+WiNtykQqEKSYsZGNQGIyFVYH8Qxvvgp7NEWAal70Ach3JFOEt+uPK/O3Ocy1JJUH9NgAR+owzcgKt6/u4jzT2UDS1P721GtFf/j+Kwk8R0/BjuvP88dOGqAJN+eAGAU76p/3/S9QLjjF1uuj7hDlCL/E2B7ipKnD7zdt2nx1lKcNw5f8QnckKLu9JqUEXpcmgWrU5W7zbOC1Sj80wysW+Ej6YlrTziHbu7JRo5SGoPY4l1XZomlDqpqDUsYWt/e9+H5dL4TjYc20dsscTr+x/C4wAAA'
const dogeBase64 = 'data:image/webp;base64,UklGRjoFAABXRUJQVlA4WAoAAAAQAAAAPwAAPwAAQUxQSBQCAAARkKQAkCJJQZCnYlwTxvWoBTXyBXvBur/BXbpnzuvWzBcKmvmAvWD92BSM1KHIQxIE5EpLVcYHImICoEjVMRuuroazHQr8x6GtnepvImImot/Vna0h9AhHb+0ZYnZNMpPZuzWKfqjo7bFllyPb47eRKg4XdlNyuVO6u4AF6fsJuUIpua+LwLUj6wq3R2uYW3A5YechJ5eDnLpKKTsvOS115dJbMc5bU+nNoatinMem0tVSUDLOa1MKWsDLqfM8vYzNrSbsGyerTekjct7TkW4C7xsn0NzHRguJE5ksNFAVkkEVVS9KndA0qoNvSQq9xf9Gj53Y49H/blo59iYAYJXlcBUBtHGCjQbYIkm0BVBiSVwCiGXFoH440T9Um5Vl26ZIFk2F0sJIWiQvlBZOSZtqs7Jsm/oh64eCmCVxDFCSVQJYJ0m0DqAzSZkGwCrL4SoCwHUrx14HABg6lnM89B++Iin0Cv+DMJWShlBXfSYZ9FnVg7lERjIHDfG2kWBuYyPQ++Qf7WtoNqqxb1yLoGk8n/qWnsfmIHiS+ZU9CaDVrg/GJ/OhC1rv/ZD5k33ohTy7nqTsB6dPuiDf4FyNfKDauQDyxmjfFGf2I4QC9e2EiqHktoZice7zGeVHZ5/nEApX4avEch5sk1ehAi9x6HqcEXMzzJTF14cQ/EW9/jz+aqmu/Ro/X9cI/mPb+EIULYy3IRQJVlA4IAADAAAwEQCdASpAAEAAPmk0mk0lpyaqMBYMAFANAAKktoVkeZmZvfKUFe7Df7bbxXOqrvKvoAdKniQEU8xPGqk/b6QOAhlypxnlq8fuYXgAgiRyoDCG7LciLB8QSs5GvViDNN8NBITXFKYo3+MaLdnvjYKzy5tP4TwDXsTZEw2c7Hw85pfujPaKK7W+gGBzEdOGyQgkCAD++8Jh98uP3YVE9qwfpijgBpCINh7dOdWjDKN/yupTvSNvSudpCyAfpKmTnIYdjWV2H04u2GkE5pjy82ODPb6xIsuqoFthC5X4DDaYPTV4hYVWAM//BbNMZJRG29BNPYPLroAwSS0fKuhNgyVu5E4M8z2GDJlcqF/Ym72KWneP/idxeAtUjES5a8dmm6kvvkICalHs2Fd80Tbatm+vwFB9G71Yn0ysNDCtUW+6aifri0jaYNgKRecf8zWftPShTv1YfGHn5pPjee9E064j31IrujAqrhl9+3FuiMxlbibz5Yb6EeF+uzNtwB/PK7CnGvvKY5sNwkl4YuYmZEdiW0g59VhqArqKuvhCSiOzSvAGz6WEh+HRDLpetr8/za+KUUky5c23TrAQ1TBRMvArPweF68sEeZYBhbKnX4q8Vrf5ecTrBXADqE+CWxGB+8D25uxJwyWhsJxVjRKn9QFSXRVhqgCnwtxlY25p5bu1Cz7mB7GTTvgZn6AeMoOP6UUagGSZQbWr5V0i92DsSlaR4TQZTMLotpFk9PKbGpGCGml3ojB5KABk8gWJ2rovO0x5ZL2pe26ir6pOfcuwpB2gs8VFKH95EMxGxtyVsbc6HQCH8E5rKaJ49/+hNvtyirRObPyhrGa0IL6Id3k83l7uutcs5YS1mKDj6ir74WpAmQ+7HsGfV36SO/htlr7ELuySFa/y+a9MFb2dmXnuQqsGA/rDuNdrNDmw9+vTykwHQwpE5b2sSQKdvNKyTM7Wtalf85POmafmizBZdJY+AY0R/if4XdyAT7lGT5rPrlfq9JshsyQtzkqoSran+a4AAAA='

const chartRef = ref(null)
const buyPrice = ref(18003)
const sellPrice = ref(23804)
const yPrices = ref([22003, 20503, 19003, 17503, 16003])
const candles = ref([])
const cursorLineStyle = ref({
  top: '0px',
  width: 'calc(100% - 42px)',
  background: 'repeating-linear-gradient(to right, rgb(132, 236, 14) 0px, rgb(132, 236, 14) 4px, transparent 4px, transparent 8px)'
})

const CHART_HEIGHT = 120
const CANDLE_WIDTH = 14
const MAX_CANDLES = 20 // To fill the block approximately

const buyBgClass = ref('bg-[#1C1E21]')
const buyShadowStyle = ref({ boxShadow: 'rgba(0, 0, 0, 0.25) 3px 4px 4px 0px' })
const sellShadowStyle = ref({ boxShadow: 'none' })

// Динамические переменные для цветов и текста
const buyTextColor = ref('#86F802')  // Зеленый для активной покупки
const sellTextColor = ref('#828282') // Серый для неактивной продажи  
const buyText = ref('Покупка')
const sellText = ref('Продажа')

const getYPosition = (price, minPrice, maxPrice) => {
  const range = maxPrice - minPrice
  if (range === 0) return CHART_HEIGHT / 2
  return ((maxPrice - price) / range) * CHART_HEIGHT
}

 const generateRandomOHLC = (prevClose = 18000) => {
   // Значительно увеличиваем волатильность для более высоких свечей
   const volatility = 400 + Math.random() * 800 // Удвоенная волатильность для более высоких свечей
   const change = (Math.random() - 0.5) * volatility
   const open = prevClose + (Math.random() - 0.5) * 200
   const close = open + change
   
   // Увеличиваем размах для более высоких фитилей
   const wickRange = Math.abs(close - open) * 0.4 + 100
   const high = Math.max(open, close) + Math.random() * wickRange
   const low = Math.min(open, close) - Math.random() * wickRange
   
   const isBull = close > open
   const color = isBull ? '#8EF702' : '#F00'

   return {
     open,
     high,
     low,
     close,
     isBull,
     color
   }
 }

const updateCandlePositions = () => {
  if (candles.value.length === 0) return
  
  // Calculate the price range for all visible candles
  const allPrices = candles.value.flatMap(c => [c.open, c.high, c.low, c.close])
  const minPrice = Math.min(...allPrices)
  const maxPrice = Math.max(...allPrices)
  
  // Увеличиваем отступы для использования всей высоты блока
  const range = maxPrice - minPrice
  const padding = Math.max(range * 0.4, 500) // Минимум 500 единиц отступа
  const paddedMinPrice = minPrice - padding
  const paddedMaxPrice = maxPrice + padding

  candles.value.forEach((candle, index) => {
    // Calculate positions based on actual price range
    const highY = getYPosition(candle.high, paddedMinPrice, paddedMaxPrice)
    const openY = getYPosition(candle.open, paddedMinPrice, paddedMaxPrice)
    const closeY = getYPosition(candle.close, paddedMinPrice, paddedMaxPrice)
    const lowY = getYPosition(candle.low, paddedMinPrice, paddedMaxPrice)
    
     // Body positioning (from top of body to bottom)
     const bodyTop = Math.min(openY, closeY)
     const bodyBottom = Math.max(openY, closeY)
     const bodyHeight = Math.max(bodyBottom - bodyTop, 4) // Увеличена минимальная высота до 4px для более заметных свечей
    
    // Wick calculations
    const upperWickHeight = Math.max(bodyTop - highY, 0)
    const lowerWickHeight = Math.max(lowY - bodyBottom, 0)
    
    // Store calculated positions
    candle.highTop = highY
    candle.bodyTop = bodyTop
    candle.bodyHeight = bodyHeight
    candle.lowTop = bodyBottom
    candle.upperWick = upperWickHeight
    candle.lowerWick = lowerWickHeight
  })
}

const updateCursorLine = () => {
  if (candles.value.length > 0) {
    const lastCandle = candles.value[candles.value.length - 1]
    // Позиционируем линию на 1px выше самой высокой точки последней свечи
    const lineTop = Math.max(0, lastCandle.highTop - 1)
    cursorLineStyle.value.top = `${lineTop}px`
  }
}

const addNewCandle = () => {
  const prevClose = candles.value.length > 0 ? candles.value[candles.value.length - 1].close : 18000
  const newCandle = generateRandomOHLC(prevClose)
  candles.value.push(newCandle)
  
  if (candles.value.length > MAX_CANDLES) {
    candles.value.shift()
  }

  // Shift positions to simulate scrolling: subtract CANDLE_WIDTH from all lefts? But since left = index*12, recalculating does it.
  // For true scroll, could add offset, but with fixed left=index*12, it fills from left.

  nextTick(() => {
    updateCandlePositions()
    updateCursorLine()
  })
}

const updatePrices = () => {
  if (candles.value.length === 0) return
  const currentClose = candles.value[candles.value.length - 1].close
  const basePrice = Math.round(currentClose)
  buyPrice.value = Math.round(basePrice * (1 + Math.random() * 0.02 - 0.01))
  sellPrice.value = Math.round(buyPrice.value * 1.3)

  // Update y prices based on current candle range with same padding as positioning
  const allPrices = candles.value.flatMap(c => [c.open, c.high, c.low, c.close])
  const minPrice = Math.min(...allPrices)
  const maxPrice = Math.max(...allPrices)
  const range = maxPrice - minPrice
  const padding = Math.max(range * 0.4, 500) // Тот же отступ что и в updateCandlePositions
  const paddedMinPrice = minPrice - padding
  const paddedMaxPrice = maxPrice + padding
  const paddedRange = paddedMaxPrice - paddedMinPrice
  
  yPrices.value = [
    Math.round(paddedMaxPrice),
    Math.round(paddedMinPrice + paddedRange * 0.75),
    Math.round(paddedMinPrice + paddedRange * 0.5),
    Math.round(paddedMinPrice + paddedRange * 0.25),
    Math.round(paddedMinPrice)
  ]

   // Определяем активное состояние на основе последней свечи
   const lastCandle = candles.value[candles.value.length - 1]
   const shouldBuy = lastCandle.isBull // Если свеча зеленая (бычья) - покупка, если красная (медвежья) - продажа
   
   if (shouldBuy) {
     // Покупка активна (зеленая свеча) - зеленый цвет
     buyBgClass.value = 'bg-[#1C1E21]'
     buyShadowStyle.value = { boxShadow: 'rgba(0, 0, 0, 0.25) 3px 4px 4px 0px' }
     sellShadowStyle.value = { boxShadow: 'none' }
     buyTextColor.value = '#86F802'  // Зеленый для активной покупки
     sellTextColor.value = '#828282' // Серый для неактивной продажи
     buyText.value = 'Покупка'
     sellText.value = 'Продажа'
   } else {
     // Продажа активна (красная свеча) - красный цвет
     buyBgClass.value = 'bg-transparent'
     buyShadowStyle.value = { boxShadow: 'none' }
     sellShadowStyle.value = { boxShadow: 'rgba(0, 0, 0, 0.25) 3px 4px 4px 0px' }
     buyTextColor.value = '#828282' // Серый для неактивной покупки
     sellTextColor.value = '#F00'    // Красный для активной продажи
     buyText.value = 'Покупка'
     sellText.value = 'Продажа'
   }
}

onMounted(() => {
  // Initial candles to fill partially from center-ish
  for (let i = 0; i < 5; i++) { // Start with some
    addNewCandle()
  }
  updatePrices()

   // Add one every 1.5 seconds
   const interval = setInterval(() => {
     addNewCandle()
     updatePrices()
   }, 1500)

  // Cleanup on unmount if needed
  // onUnmounted(() => clearInterval(interval))
})
</script>