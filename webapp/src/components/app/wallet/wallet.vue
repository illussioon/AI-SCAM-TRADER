<template>
  <div class="wallet-page">
    <HeaderApp />
     <!-- Светяшка -->
     <div class="absolute w-[27px] h-[54px] blur-[40px] opacity-[0.77] pointer-events-none will-change-auto" style="background: rgb(140, 246, 5); top: 60px; left: 0px; z-index: 30; transform: translateZ(0px); backface-visibility: hidden;"></div>
    <div style="margin: 0px 8px 0 8px;">
        <Card />
        <Banks />
        <Banks2 />
        <Transaction />
        <TransactionMenu />
    </div>
     
    <div class="wallet-content">
    </div>
    <Menu />
  </div>
</template>

<script setup>
import HeaderApp from '../header-app.vue'
import Menu from '../menu.vue'
import Banks from './banks.vue'
import Card from './card.vue'
import Transaction from './transaction.vue'
import Banks2 from './banks2.vue'
import TransactionMenu from './transaction-menu.vue'
</script>

<style scoped>
.wallet-page {
  min-height: 100vh;
  background: #0B0C0D;
  color: white;
}

.wallet-content {
  padding: 20px;
  padding-bottom: 100px; /* Отступ для меню снизу */
}
</style>
