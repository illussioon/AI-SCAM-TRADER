<template>
    <div class="flex items-center gap-2">
      <img 
        alt="Lighting" 
        src="data:image/svg+xml,%3csvg%20width='50'%20height='56'%20viewBox='0%200%2050%2056'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M31.9423%2010.1169C33.1556%2010.4916%2033.6124%2011.8937%2032.9947%2012.9119L32.8558%2013.1108L27.4306%2019.9441L31.0519%2021.0622C32.473%2021.501%2032.7927%2023.2653%2031.8131%2024.2271L31.5993%2024.4076L16.3463%2035.5756C15.2443%2036.3811%2013.9078%2035.1767%2014.4127%2034.0225L18.6234%2024.4027L14.6009%2023.1607C13.2923%2022.7567%2012.8671%2021.1652%2013.7074%2020.143L13.7195%2020.1294L23.4211%208.6997C23.6592%208.4143%2023.9763%208.20555%2024.3326%208.09964C24.6888%207.99373%2025.0685%207.99538%2025.4238%208.10437L31.9423%2010.1169Z'%20fill='white'/%3e%3cg%20clip-path='url(%23clip0_0_1)'%3e%3cpath%20d='M36.4125%2040.0206L45.0994%2035.3904L44.2891%2034.1163L26.5126%2032.8958L30.1592%2038.6293L21.4722%2043.2594L22.2826%2044.5336L40.0591%2045.7541L36.4125%2040.0206Z'%20fill='white'/%3e%3c/g%3e%3cdefs%3e%3cclipPath%20id='clip0_0_1'%3e%3crect%20width='24.1596'%20height='24.1596'%20fill='white'%20transform='translate(36.9961%2022.6489)%20rotate(57.5435)'/%3e%3c/clipPath%3e%3c/defs%3e%3c/svg%3e"
      >
      <h2 class="text-[28px] font-bold text-white">
        Крипто стейкинг до
        <span class="ml-2 text-[#5EFF03]">81%</span>
      </h2>
    </div>
  
    <button 
      @click="openEducation"
      class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md font-medium transition-all disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg:not([class*='size-'])]:size-4 shrink-0 [&_svg]:shrink-0 outline-none focus-visible:border-ring focus-visible:ring-ring/50 focus-visible:ring-[3px] aria-invalid:ring-destructive/20 dark:aria-invalid:ring-destructive/40 aria-invalid:border-destructive bg-primary text-primary-foreground shadow-xs hover:bg-primary/90 px-4 py-2 has-[>svg]:px-3 w-full mt-2 text-[20px] h-[45px]"
      style="background: linear-gradient(rgb(179, 241, 6) 0%, rgb(94, 255, 3) 100%);"
      type="button"
    >
      <img 
        alt="Book" 
        src="data:image/svg+xml,%3csvg%20width='18'%20height='20'%20viewBox='0%200%2018%2020'%20fill='none'%20xmlns='http://www.w3.org/2000/svg'%3e%3cpath%20d='M4%200C2.93913%200%201.92172%200.421427%201.17157%201.17157C0.421427%201.92172%200%202.93913%200%204V16C0%2017.0609%200.421427%2018.0783%201.17157%2018.8284C1.92172%2019.5786%202.93913%2020%204%2020H18V0H4ZM8%203H15V5H8V3ZM2%2016C2%2015.4696%202.21071%2014.9609%202.58579%2014.5858C2.96086%2014.2107%203.46957%2014%204%2014H16V18H4C3.46957%2018%202.96086%2017.7893%202.58579%2017.4142C2.21071%2017.0391%202%2016.5304%202%2016Z'%20fill='black'/%3e%3c/svg%3e"
      >
      <p class="mt-1 text-black">Читать обучение</p>
    </button>
  </template>
  
  <script setup>
  const openEducation = () => {
    window.open('https://telegra.ph/Obuchenie-Royal-09-27', '_blank')
  }
  </script>