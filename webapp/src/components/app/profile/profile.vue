<template>
  <div class="min-h-screen bg-[#0B0C0D] text-white">
    <!-- Header -->
    <HeaderApp />
    <!-- Светяшка -->
    <div class="absolute w-[27px] h-[54px] blur-[40px] opacity-[0.77] pointer-events-none will-change-auto" style="background: rgb(140, 246, 5); top: 60px; left: 0px; z-index: 30; transform: translateZ(0px); backface-visibility: hidden;"></div>
    <!-- Main Content -->
    <main class="pb-20">
      <!-- User Component -->
      <div style="margin: -4px 8px 0 8px;">
        <User />
        <Bonus />
        <Stats />
        <Settings />
        <Footer />
      </div>
    </main>
    
    <!-- Bottom Menu -->
    <div style="padding-top: 50px;">
      <Menu />
    </div>
  </div>
</template>

<script setup>
import HeaderApp from '../header-app.vue'
import Menu from '../menu.vue'
import User from './user.vue'
import Bonus from './bonus.vue'
import Stats from './stats.vue'
import Settings from './settings.vue'
import Footer from '../footer.vue'
</script>

<style scoped>
@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Regular-ClstCj-k.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Medium-DHgsE3TE.ttf') format('truetype');
  font-weight: 500;
  font-style: normal;
}

@font-face {
  font-family: 'TTCommons';
  src: url('/font/TTCommons-Bold-DVcClD20.ttf') format('truetype');
  font-weight: 700;
  font-style: normal;
}

/* Применяем шрифт TTCommons */
* {
  font-family: 'TTCommons', system-ui, -apple-system, sans-serif;
}
</style>
