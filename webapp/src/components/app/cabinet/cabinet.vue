<template>
  <div class="min-h-screen bg-[#0B0C0D] text-white">
    <HeaderApp />
    <!-- Светяшка -->
    <div class="absolute w-[27px] h-[54px] blur-[40px] opacity-[0.77] pointer-events-none will-change-auto" style="background: rgb(140, 246, 5); top: 60px; left: 0px; z-index: 30; transform: translateZ(0px); backface-visibility: hidden;"></div>
    <main class="pb-24" style="margin: 0px 8px 0 8px;">
      <Stake />
      <div class="mt-0 -ml-5 flex space-x-2 items-center"><svg viewBox="0 0 64.4001 60.3999" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="64.400146" height="60.399902" fill="none" customFrame="#000000" class="filter drop-shadow-[0_0_18px_rgba(94,255,3,0.7)]"><mask id="mask_0" width="20.00025" height="16" x="22.199951" y="22.199951" maskUnits="userSpaceOnUse"><g filter="url(#pixso_custom_mask_type_luminance)"><g id="Group" filter="url(#filter_1)"><g id="Group"><path id="Vector" d="M34.2002 22.2L30.2002 22.2C26.4292 22.2 24.5432 22.2 23.3722 23.372C22.5282 24.215 22.2922 25.429 22.2262 27.45L42.1742 27.45C42.1082 25.429 41.8722 24.215 41.0282 23.372C39.8572 22.2 37.9712 22.2 34.2002 22.2ZM30.2002 38.2L34.2002 38.2C37.9712 38.2 39.8572 38.2 41.0282 37.028C42.1992 35.8559 42.2002 33.971 42.2002 30.2C42.2002 29.7586 42.1995 29.342 42.1982 28.95L22.2022 28.95C22.2002 29.342 22.1995 29.7586 22.2002 30.2C22.2002 33.971 22.2002 35.8569 23.3722 37.028C24.5442 38.199 26.4292 38.2 30.2002 38.2Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path><path id="Vector" d="M25.4502 34.2C25.4502 34.001 25.5292 33.8103 25.6699 33.6696C25.8105 33.529 26.0013 33.45 26.2002 33.45L30.2002 33.45C30.3991 33.45 30.5899 33.529 30.7305 33.6696C30.8712 33.8103 30.9502 34.001 30.9502 34.2C30.9502 34.3989 30.8712 34.5896 30.7305 34.7303C30.5899 34.8709 30.3991 34.95 30.2002 34.95L26.2002 34.95C26.0013 34.95 25.8105 34.8709 25.6699 34.7303C25.5292 34.5896 25.4502 34.3989 25.4502 34.2ZM31.9502 34.2C31.9502 34.001 32.0292 33.8103 32.1699 33.6696C32.3105 33.529 32.5013 33.45 32.7002 33.45L34.2002 33.45C34.3991 33.45 34.5899 33.529 34.7305 33.6696C34.8712 33.8103 34.9502 34.001 34.9502 34.2C34.9502 34.3989 34.8712 34.5896 34.7305 34.7303C34.5899 34.8709 34.3991 34.95 34.2002 34.95L32.7002 34.95C32.5013 34.95 32.3105 34.8709 32.1699 34.7303C32.0292 34.5896 31.9502 34.3989 31.9502 34.2Z" fill="rgb(0,0,0)" fill-rule="evenodd"></path></g></g></g></mask><defs><g id="pixso_custom_effect_0"><effect x="0" y="0" visibility="visible" fill="rgb(94,255,3)" fill-opacity="0.400000006" effectType="dropShadow" stdDeviation="17.9759998" radius="0"></effect></g><filter id="filter_0" width="64.400146" height="60.399902" x="0" y="0" filterUnits="userSpaceOnUse" customEffect="url(#pixso_custom_effect_0)" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feOffset dx="0" dy="0" in="SourceAlpha"></feOffset><feGaussianBlur stdDeviation="5.9920001"></feGaussianBlur><feColorMatrix type="matrix" values="0 0 0 0 0.368627 0 0 0 0 1 0 0 0 0 0.0117647 0 0 0 0.4 0 "></feColorMatrix><feBlend result="effect_dropShadow_1" in2="BackgroundImageFix" mode="normal"></feBlend><feBlend result="shape" in="SourceGraphic" in2="effect_dropShadow_1" mode="normal"></feBlend></filter><g id="pixso_custom_effect_1"><effect x="0" y="0" visibility="visible" fill="rgb(94,255,3)" fill-opacity="0.400000006" effectType="dropShadow" stdDeviation="22.2000008" radius="0"></effect></g><filter id="filter_1" width="64.400146" height="60.399902" x="0" y="0" filterUnits="userSpaceOnUse" customEffect="url(#pixso_custom_effect_1)" color-interpolation-filters="sRGB"><feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood><feOffset dx="0" dy="0" in="SourceAlpha"></feOffset><feGaussianBlur stdDeviation="7.4000001"></feGaussianBlur><feColorMatrix type="matrix" values="0 0 0 0 0.368627 0 0 0 0 1 0 0 0 0 0.0117647 0 0 0 0.4 0 "></feColorMatrix><feBlend result="effect_dropShadow_1" in2="BackgroundImageFix" mode="normal"></feBlend><feBlend result="shape" in="SourceGraphic" in2="effect_dropShadow_1" mode="normal"></feBlend></filter><filter id="pixso_custom_mask_type_luminance"><feColorMatrix type="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 "></feColorMatrix></filter></defs><g id="Mask group" filter="url(#filter_0)"><g mask="url(#mask_0)"><path id="Vector" d="M20.2002 18.2L44.2002 18.2L44.2002 42.2L20.2002 42.2L20.2002 18.2Z" fill="rgb(144,247,5)" fill-rule="nonzero"></path></g></g></svg><p class="-ml-5 mt-[2px] text-[20px] font-semibold">Тарифные планы: </p></div>
      <TarifPlans />
      <div class="mt-3 flex space-x-2 items-center mb-2"><svg viewBox="0 0 20.0007 20.5" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20.000732" height="20.5" fill="none" customFrame="#000000" class="filter drop-shadow-[0_0_18px_rgba(94,255,3,0.7)]"><path id="Vector" d="M6.00036 15C3.17236 15 1.75736 15 0.879364 14.121C0.309364 13.552 0.109364 12.758 0.0393637 11.5L19.9624 11.5C19.8924 12.758 19.6914 13.552 19.1224 14.121C18.2414 15 16.8274 15 14.0004 15L10.7504 15L10.7504 19L14.0004 19C14.1993 19 14.39 19.079 14.5307 19.2197C14.6713 19.3603 14.7504 19.5511 14.7504 19.75C14.7504 19.9489 14.6713 20.1397 14.5307 20.2803C14.39 20.421 14.1993 20.5 14.0004 20.5L6.00036 20.5C5.80145 20.5 5.61069 20.421 5.47003 20.2803C5.32938 20.1397 5.25036 19.9489 5.25036 19.75C5.25036 19.5511 5.32938 19.3603 5.47003 19.2197C5.61069 19.079 5.80145 19 6.00036 19L9.25036 19L9.25036 15L6.00036 15ZM8.00036 2.22045e-16L12.0004 2.22045e-16C15.7714 2.22045e-16 17.6574 -1.19209e-07 18.8284 1.172C19.9994 2.344 20.0004 4.229 20.0004 8L20.0004 9C20.0017 9.55133 19.9997 10.0513 19.9944 10.5L0.00736361 10.5C0.00136361 10.0513 -0.000969694 9.55133 0.000363639 9L0.000363639 8C0.000363639 4.229 0.000363469 2.343 1.17236 1.172C2.34436 0.000999928 4.22936 2.22045e-16 8.00036 2.22045e-16Z" fill="rgb(144,247,5)" fill-rule="nonzero"></path></svg><p class="mt-[2px] font-semibold text-[20px]">Торговый терминал: </p></div>
      <Trading />
      <Terminal />
      <AI />
      <!-- Здесь будет контент кабинета -->
      <Footer />
    </main>


   
    <Menu />
  </div>
</template>

<script setup>
import HeaderApp from '../header-app.vue'
import Menu from '../menu.vue'
import Footer from '../footer.vue'
import AI from './AI.vue'
import Trading from './trading.vue'
import TarifPlans from './tarif-plans.vue'
import Terminal from './terminal.vue'
import Stake from './stake.vue'
</script>







