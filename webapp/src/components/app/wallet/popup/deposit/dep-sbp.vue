<template>
    <div class="flex-1 min-h-0 overflow-y-auto pb-[90px]">
      <div class="flex flex-col pb-[400px]">
        <div class="rounded-[19px] bg-[#1A1B20] flex flex-col py-[13px] px-4">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-x-3">
              <svg viewBox="0 0 21 21" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="21" height="21" fill="none" customFrame="url(#clipPath_3)" class="h-[21px] w-[21px] -translate-y-1">
                <defs>
                  <linearGradient id="paint_linear_4" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                    <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                    <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                  </linearGradient>
                  <linearGradient id="paint_linear_5" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                    <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                    <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                  </linearGradient>
                  <linearGradient id="paint_linear_6" x1="10.5" x2="10.5" y1="-6.42939617e-16" y2="21" gradientUnits="userSpaceOnUse">
                    <stop stop-color="rgb(179,241,6)" offset="0" stop-opacity="1"></stop>
                    <stop stop-color="rgb(94,255,3)" offset="1" stop-opacity="1"></stop>
                  </linearGradient>
                  <clipPath id="clipPath_3">
                    <rect width="21" height="21" x="0" y="0" rx="10.5" fill="rgb(255,255,255)"></rect>
                  </clipPath>
                  <g id="pixso_custom_effect_8">
                    <effect x="0" y="3.861111" visibility="visible" fill="rgb(0,0,0)" fill-opacity="0.25" effectType="dropShadow" stdDeviation="24.0354156" radius="0"></effect>
                  </g>
                  <filter id="filter_8" width="7.722168" height="9" x="6.638916" y="6" filterUnits="userSpaceOnUse" customEffect="url(#pixso_custom_effect_8)" color-interpolation-filters="sRGB">
                    <feFlood flood-opacity="0" result="BackgroundImageFix"></feFlood>
                    <feOffset dx="0" dy="3.861111" in="SourceAlpha"></feOffset>
                    <feGaussianBlur stdDeviation="8.01180553"></feGaussianBlur>
                    <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.25 0 "></feColorMatrix>
                    <feBlend result="effect_dropShadow_1" in2="BackgroundImageFix" mode="normal"></feBlend>
                    <feBlend result="shape" in="SourceGraphic" in2="effect_dropShadow_1" mode="normal"></feBlend>
                  </filter>
                </defs>
                <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_4)"></rect>
                <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_5)"></rect>
                <rect id="Frame 2087325261" width="21" height="21" x="0" y="0" rx="10.5" fill="url(#paint_linear_6)"></rect>
                <g filter="url(#filter_8)">
                  <path id="\u20BD" d="M11.3475 10.2702C11.5596 10.2702 11.7599 10.2302 11.9484 10.15C12.1369 10.0652 12.2972 9.95443 12.4292 9.81775C12.5659 9.67635 12.6719 9.51374 12.7473 9.32993C12.8274 9.14611 12.8675 8.95286 12.8675 8.75019C12.8675 8.54752 12.8274 8.35428 12.7473 8.17046C12.6719 7.98664 12.5659 7.82639 12.4292 7.68971C12.2972 7.54831 12.1369 7.43755 11.9484 7.35742C11.7599 7.27258 11.5596 7.23016 11.3475 7.23016L9.45981 7.23016L9.45981 10.2702L11.3475 10.2702ZM14.2391 8.75019C14.2391 9.11783 14.166 9.46661 14.0199 9.79654C13.8785 10.1218 13.6758 10.414 13.4119 10.6732C13.1527 10.9277 12.8463 11.1304 12.4928 11.2812C12.144 11.4273 11.7622 11.5004 11.3475 11.5004L9.45981 11.5004L9.45981 12.4407L12.21 12.4407L12.21 13.6708L9.45981 13.6708L9.45981 15.1202L8.08825 15.1202L8.08825 13.6708L6.99948 13.6708L6.99948 12.4407L8.08825 12.4407L8.08825 11.5004L6.99948 11.5004L6.99948 10.2702L8.08825 10.2702L8.08825 6L11.3475 6C11.7622 6 12.144 6.07541 12.4928 6.22624C12.8463 6.37235 13.1527 6.57502 13.4119 6.83425C13.6758 7.08877 13.8785 7.38334 14.0199 7.71799C14.166 8.04792 14.2391 8.39198 14.2391 8.75019Z" fill="rgb(12,13,15)" fill-rule="nonzero"></path>
                </g>
              </svg>
              <div class="flex flex-col">
                <p class="text-[13px] text-white opacity-50">Сумма перевода</p>
                <p class="text-[19px] -mt-1 font-semibold text-white">{{ transferAmount }}</p>
              </div>
            </div>
            <button @click="copyToClipboard('1030')" class="rounded-[11px] bg-[#2C2D32] h-[36px] w-[36px] flex items-center justify-center transition-all duration-200 transform hover:scale-105 active:scale-95">
              <svg viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="22" height="22" fill="none">
                <rect id="solar:copy-bold" width="22" height="22" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <path id="Vector" d="M13.97 1.83325L10.4005 1.83325C8.7835 1.83325 7.502 1.83325 6.50008 1.96892C5.46792 2.10825 4.63283 2.40159 3.97467 3.0625C3.31558 3.72342 3.02317 4.56217 2.88475 5.598C2.75 6.6045 2.75 7.89058 2.75 9.514L2.75 14.8655C2.75 16.2478 3.59333 17.4322 4.79142 17.929C4.73 17.0948 4.73 15.9261 4.73 14.9526L4.73 10.3601C4.73 9.18583 4.73 8.17292 4.83817 7.36259C4.95458 6.49359 5.21675 5.66125 5.88958 4.98567C6.56242 4.31009 7.392 4.047 8.25733 3.92967C9.064 3.8215 10.0723 3.8215 11.2429 3.8215L14.0571 3.8215C15.2268 3.8215 16.2332 3.8215 17.0408 3.92967C16.7989 3.3121 16.3766 2.78176 15.8288 2.4078C15.281 2.03384 14.6333 1.83362 13.97 1.83325Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                <path id="Vector" d="M6.05029 10.4473C6.05029 7.94849 6.05029 6.69907 6.82396 5.92266C7.59671 5.14624 8.84063 5.14624 11.3303 5.14624L13.9703 5.14624C16.459 5.14624 17.7039 5.14624 18.4775 5.92266C19.2512 6.69907 19.2503 7.94849 19.2503 10.4473L19.2503 14.8657C19.2503 17.3645 19.2503 18.6139 18.4775 19.3903C17.7039 20.1667 16.459 20.1667 13.9703 20.1667L11.3303 20.1667C8.84154 20.1667 7.59671 20.1667 6.82396 19.3903C6.05029 18.6139 6.05029 17.3645 6.05029 14.8657L6.05029 10.4473Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
              </svg>
            </button>
          </div>
          <img alt="Мы изменили сумму вашего перевода, что бы убедиться, что это ваш платёж и зачислить его" class="mt-4" loading="eager" decoding="async" draggable="false" :src="imageSrc">
          <div class="flex items-center justify-between mt-5">
            <div class="flex items-center gap-x-3">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" fill="none" class="-translate-y-1">
                <defs>
                  <filter id="pixso_custom_mask_type_luminance">
                    <feColorMatrix type="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 "></feColorMatrix>
                  </filter>
                </defs>
                <mask id="mask_0" width="20.00025" height="16" x="1.999512" y="4" maskUnits="userSpaceOnUse">
                  <g filter="url(#pixso_custom_mask_type_luminance)">
                    <g id="Group">
                      <g id="Group">
                        <path id="Vector" d="M13.9998 4L9.99976 4C6.22876 4 4.34276 4 3.17176 5.172C2.32776 6.015 2.09176 7.229 2.02576 9.25L21.9738 9.25C21.9078 7.229 21.6718 6.015 20.8278 5.172C19.6568 4 17.7708 4 13.9998 4ZM9.99976 20L13.9998 20C17.7708 20 19.6568 20 20.8278 18.828C21.9988 17.656 21.9998 15.771 21.9998 12C21.9998 11.5587 21.9991 11.142 21.9978 10.75L2.00176 10.75C1.99976 11.142 1.9991 11.5587 1.99976 12C1.99976 15.771 1.99976 17.657 3.17176 18.828C4.34376 19.999 6.22876 20 9.99976 20Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                        <path id="Vector" d="M5.25 16C5.25 15.8011 5.32902 15.6103 5.46967 15.4697C5.61032 15.329 5.80109 15.25 6 15.25L10 15.25C10.1989 15.25 10.3897 15.329 10.5303 15.4697C10.671 15.6103 10.75 15.8011 10.75 16C10.75 16.1989 10.671 16.3897 10.5303 16.5303C10.3897 16.671 10.1989 16.75 10 16.75L6 16.75C5.80109 16.75 5.61032 16.671 5.46967 16.5303C5.32902 16.3897 5.25 16.1989 5.25 16ZM11.75 16C11.75 15.8011 11.829 15.6103 11.9697 15.4697C12.1103 15.329 12.3011 15.25 12.5 15.25L14 15.25C14.1989 15.25 14.3897 15.329 14.5303 15.4697C14.671 15.6103 14.75 15.8011 14.75 16C14.75 16.1989 14.671 16.3897 14.5303 16.5303C14.3897 16.671 14.1989 16.75 14 16.75L12.5 16.75C12.3011 16.75 12.1103 16.671 11.9697 16.5303C11.829 16.3897 11.75 16.1989 11.75 16Z" fill="rgb(0,0,0)" fill-rule="evenodd"></path>
                      </g>
                    </g>
                  </g>
                </mask>
                <rect id="solar:card-bold" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <g id="Mask group" mask="url(#mask_0)">
                  <path id="Vector" d="M0 0L24 0L24 24L0 24L0 0Z" fill="rgb(158,165,173)" fill-rule="nonzero"></path>
                </g>
              </svg>
              <div class="flex flex-col">
                <p class="text-[13px] text-white opacity-50">Номер для перевода</p>
                <p class="text-[19px] -mt-1 font-semibold text-white">{{ cardNumber }}</p>
              </div>
            </div>
            <button @click="copyToClipboard(cardNumber)" class="rounded-[11px] bg-[#2C2D32] h-[36px] w-[36px] flex items-center justify-center transition-all duration-200 transform hover:scale-105 active:scale-95">
              <svg viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="22" height="22" fill="none">
                <rect id="solar:copy-bold" width="22" height="22" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <path id="Vector" d="M13.97 1.83325L10.4005 1.83325C8.7835 1.83325 7.502 1.83325 6.50008 1.96892C5.46792 2.10825 4.63283 2.40159 3.97467 3.0625C3.31558 3.72342 3.02317 4.56217 2.88475 5.598C2.75 6.6045 2.75 7.89058 2.75 9.514L2.75 14.8655C2.75 16.2478 3.59333 17.4322 4.79142 17.929C4.73 17.0948 4.73 15.9261 4.73 14.9526L4.73 10.3601C4.73 9.18583 4.73 8.17292 4.83817 7.36259C4.95458 6.49359 5.21675 5.66125 5.88958 4.98567C6.56242 4.31009 7.392 4.047 8.25733 3.92967C9.064 3.8215 10.0723 3.8215 11.2429 3.8215L14.0571 3.8215C15.2268 3.8215 16.2332 3.8215 17.0408 3.92967C16.7989 3.3121 16.3766 2.78176 15.8288 2.4078C15.281 2.03384 14.6333 1.83362 13.97 1.83325Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                <path id="Vector" d="M6.05029 10.4473C6.05029 7.94849 6.05029 6.69907 6.82396 5.92266C7.59671 5.14624 8.84063 5.14624 11.3303 5.14624L13.9703 5.14624C16.459 5.14624 17.7039 5.14624 18.4775 5.92266C19.2512 6.69907 19.2503 7.94849 19.2503 10.4473L19.2503 14.8657C19.2503 17.3645 19.2503 18.6139 18.4775 19.3903C17.7039 20.1667 16.459 20.1667 13.9703 20.1667L11.3303 20.1667C8.84154 20.1667 7.59671 20.1667 6.82396 19.3903C6.05029 18.6139 6.05029 17.3645 6.05029 14.8657L6.05029 10.4473Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
              </svg>
            </button>
          </div>
          <div class="flex items-center justify-between mt-2 border-t border-b py-3 border-[#141517]">
            <div class="flex items-center gap-x-3">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" fill="none" class="-translate-y-1">
                <defs>
                  <filter id="pixso_custom_mask_type_luminance">
                    <feColorMatrix type="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0 "></feColorMatrix>
                  </filter>
                </defs>
                <mask id="mask_0" width="20.00025" height="16" x="1.999512" y="4" maskUnits="userSpaceOnUse">
                  <g filter="url(#pixso_custom_mask_type_luminance)">
                    <g id="Group">
                      <g id="Group">
                        <path id="Vector" d="M13.9998 4L9.99976 4C6.22876 4 4.34276 4 3.17176 5.172C2.32776 6.015 2.09176 7.229 2.02576 9.25L21.9738 9.25C21.9078 7.229 21.6718 6.015 20.8278 5.172C19.6568 4 17.7708 4 13.9998 4ZM9.99976 20L13.9998 20C17.7708 20 19.6568 20 20.8278 18.828C21.9988 17.656 21.9998 15.771 21.9998 12C21.9998 11.5587 21.9991 11.142 21.9978 10.75L2.00176 10.75C1.99976 11.142 1.9991 11.5587 1.99976 12C1.99976 15.771 1.99976 17.657 3.17176 18.828C4.34376 19.999 6.22876 20 9.99976 20Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                        <path id="Vector" d="M5.25 16C5.25 15.8011 5.32902 15.6103 5.46967 15.4697C5.61032 15.329 5.80109 15.25 6 15.25L10 15.25C10.1989 15.25 10.3897 15.329 10.5303 15.4697C10.671 15.6103 10.75 15.8011 10.75 16C10.75 16.1989 10.671 16.3897 10.5303 16.5303C10.3897 16.671 10.1989 16.75 10 16.75L6 16.75C5.80109 16.75 5.61032 16.671 5.46967 16.5303C5.32902 16.3897 5.25 16.1989 5.25 16ZM11.75 16C11.75 15.8011 11.829 15.6103 11.9697 15.4697C12.1103 15.329 12.3011 15.25 12.5 15.25L14 15.25C14.1989 15.25 14.3897 15.329 14.5303 15.4697C14.671 15.6103 14.75 15.8011 14.75 16C14.75 16.1989 14.671 16.3897 14.5303 16.5303C14.3897 16.671 14.1989 16.75 14 16.75L12.5 16.75C12.3011 16.75 12.1103 16.671 11.9697 16.5303C11.829 16.3897 11.75 16.1989 11.75 16Z" fill="rgb(0,0,0)" fill-rule="evenodd"></path>
                      </g>
                    </g>
                  </g>
                </mask>
                <rect id="solar:card-bold" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <g id="Mask group" mask="url(#mask_0)">
                  <path id="Vector" d="M0 0L24 0L24 24L0 24L0 0Z" fill="rgb(158,165,173)" fill-rule="nonzero"></path>
                </g>
              </svg>
              <div class="flex flex-col">
                <p class="text-[13px] text-white opacity-50">Банк</p>
                <p class="text-[19px] -mt-1 font-semibold text-white">{{ bankName }}</p>
              </div>
            </div>
            <button @click="copyToClipboard(bankName)" class="rounded-[11px] bg-[#2C2D32] h-[36px] w-[36px] flex items-center justify-center transition-all duration-200 transform hover:scale-105 active:scale-95">
              <svg viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="22" height="22" fill="none">
                <rect id="solar:copy-bold" width="22" height="22" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <path id="Vector" d="M13.97 1.83325L10.4005 1.83325C8.7835 1.83325 7.502 1.83325 6.50008 1.96892C5.46792 2.10825 4.63283 2.40159 3.97467 3.0625C3.31558 3.72342 3.02317 4.56217 2.88475 5.598C2.75 6.6045 2.75 7.89058 2.75 9.514L2.75 14.8655C2.75 16.2478 3.59333 17.4322 4.79142 17.929C4.73 17.0948 4.73 15.9261 4.73 14.9526L4.73 10.3601C4.73 9.18583 4.73 8.17292 4.83817 7.36259C4.95458 6.49359 5.21675 5.66125 5.88958 4.98567C6.56242 4.31009 7.392 4.047 8.25733 3.92967C9.064 3.8215 10.0723 3.8215 11.2429 3.8215L14.0571 3.8215C15.2268 3.8215 16.2332 3.8215 17.0408 3.92967C16.7989 3.3121 16.3766 2.78176 15.8288 2.4078C15.281 2.03384 14.6333 1.83362 13.97 1.83325Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                <path id="Vector" d="M6.05029 10.4473C6.05029 7.94849 6.05029 6.69907 6.82396 5.92266C7.59671 5.14624 8.84063 5.14624 11.3303 5.14624L13.9703 5.14624C16.459 5.14624 17.7039 5.14624 18.4775 5.92266C19.2512 6.69907 19.2503 7.94849 19.2503 10.4473L19.2503 14.8657C19.2503 17.3645 19.2503 18.6139 18.4775 19.3903C17.7039 20.1667 16.459 20.1667 13.9703 20.1667L11.3303 20.1667C8.84154 20.1667 7.59671 20.1667 6.82396 19.3903C6.05029 18.6139 6.05029 17.3645 6.05029 14.8657L6.05029 10.4473Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
              </svg>
            </button>
          </div>
          <div class="flex items-center justify-between mt-5">
            <div class="flex items-center gap-x-3">
              <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" fill="none" class="-translate-y-1">
                <rect id="basil:user-solid" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <path id="Vector" d="M12 3.75C11.0054 3.75 10.0516 4.14509 9.34835 4.84835C8.64509 5.55161 8.25 6.50544 8.25 7.5C8.25 8.49456 8.64509 9.44839 9.34835 10.1517C10.0516 10.8549 11.0054 11.25 12 11.25C12.9946 11.25 13.9484 10.8549 14.6517 10.1517C15.3549 9.44839 15.75 8.49456 15.75 7.5C15.75 6.50544 15.3549 5.55161 14.6517 4.84835C13.9484 4.14509 12.9946 3.75 12 3.75ZM8 13.25C7.00544 13.25 6.05161 13.6451 5.34835 14.3483C4.64509 15.0516 4.25 16.0054 4.25 17L4.25 18.188C4.25 18.942 4.796 19.584 5.54 19.705C9.818 20.404 14.182 20.404 18.46 19.705C18.8198 19.6458 19.147 19.4608 19.3832 19.1831C19.6194 18.9053 19.7494 18.5527 19.75 18.188L19.75 17C19.75 16.0054 19.3549 15.0516 18.6517 14.3483C17.9484 13.6451 16.9946 13.25 16 13.25L15.66 13.25C15.4733 13.2507 15.292 13.2793 15.116 13.336L14.25 13.619C12.788 14.0963 11.212 14.0963 9.75 13.619L8.884 13.336C8.70847 13.2797 8.52534 13.2507 8.341 13.25L8 13.25Z" fill="rgb(158,165,173)" fill-rule="nonzero"></path>
              </svg>
              <div class="flex flex-col">
                <p class="text-[13px] text-white opacity-50">Получатель</p>
                <p class="text-[19px] -mt-1 font-semibold text-white">{{ recipientName }}</p>
              </div>
            </div>
            <button @click="copyToClipboard(recipientName)" class="rounded-[11px] bg-[#2C2D32] h-[36px] w-[36px] flex items-center justify-center transition-all duration-200 transform hover:scale-105 active:scale-95">
              <svg viewBox="0 0 22 22" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="22" height="22" fill="none">
                <rect id="solar:copy-bold" width="22" height="22" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
                <path id="Vector" d="M13.97 1.83325L10.4005 1.83325C8.7835 1.83325 7.502 1.83325 6.50008 1.96892C5.46792 2.10825 4.63283 2.40159 3.97467 3.0625C3.31558 3.72342 3.02317 4.56217 2.88475 5.598C2.75 6.6045 2.75 7.89058 2.75 9.514L2.75 14.8655C2.75 16.2478 3.59333 17.4322 4.79142 17.929C4.73 17.0948 4.73 15.9261 4.73 14.9526L4.73 10.3601C4.73 9.18583 4.73 8.17292 4.83817 7.36259C4.95458 6.49359 5.21675 5.66125 5.88958 4.98567C6.56242 4.31009 7.392 4.047 8.25733 3.92967C9.064 3.8215 10.0723 3.8215 11.2429 3.8215L14.0571 3.8215C15.2268 3.8215 16.2332 3.8215 17.0408 3.92967C16.7989 3.3121 16.3766 2.78176 15.8288 2.4078C15.281 2.03384 14.6333 1.83362 13.97 1.83325Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
                <path id="Vector" d="M6.05029 10.4473C6.05029 7.94849 6.05029 6.69907 6.82396 5.92266C7.59671 5.14624 8.84063 5.14624 11.3303 5.14624L13.9703 5.14624C16.459 5.14624 17.7039 5.14624 18.4775 5.92266C19.2512 6.69907 19.2503 7.94849 19.2503 10.4473L19.2503 14.8657C19.2503 17.3645 19.2503 18.6139 18.4775 19.3903C17.7039 20.1667 16.459 20.1667 13.9703 20.1667L11.3303 20.1667C8.84154 20.1667 7.59671 20.1667 6.82396 19.3903C6.05029 18.6139 6.05029 17.3645 6.05029 14.8657L6.05029 10.4473Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
              </svg>
            </button>
          </div>
        </div>
        <div class="rounded-[19px] bg-[#1A1B20] h-[60px] mt-3 flex justify-between items-center py-3 px-3">
          <div class="flex items-center gap-x-3">
            <div class="animate-spin">
              <svg width="26" height="26" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
                <mask id="path-1-inside-1_1611_2575" fill="white">
                  <path d="M13 1.90735e-06C20.1797 1.90735e-06 26 5.8203 26 13C26 20.1797 20.1797 26 13 26C5.8203 26 0 20.1797 0 13C0 5.8203 5.8203 1.90735e-06 13 1.90735e-06Z"></path>
                </mask>
                <g clip-path="url(#paint0_angular_1611_2575_clip_path)" data-figma-skip-parse="true" mask="url(#path-1-inside-1_1611_2575)">
                  <g transform="matrix(-0.013 0 0 -0.013 13 13)">
                    <foreignObject x="-1291.67" y="-1291.67" width="2583.33" height="2583.33">
                      <div xmlns="http://www.w3.org/1999/xhtml" style="background: conic-gradient(from 90deg, rgba(255, 255, 255, 0) 0deg, rgb(255, 255, 255) 360deg); height: 100%; width: 100%; opacity: 1;"></div>
                    </foreignObject>
                  </g>
                </g>
                <path d="M13 1.90735e-06V3.79167C18.0856 3.79167 22.2083 7.91438 22.2083 13H26H29.7917C29.7917 3.72622 22.2738 -3.79166 13 -3.79166V1.90735e-06ZM26 13H22.2083C22.2083 18.0856 18.0856 22.2083 13 22.2083V26V29.7917C22.2738 29.7917 29.7917 22.2738 29.7917 13H26ZM13 26V22.2083C7.91438 22.2083 3.79167 18.0856 3.79167 13H0H-3.79167C-3.79167 22.2738 3.72622 29.7917 13 29.7917V26ZM0 13H3.79167C3.79167 7.91438 7.91438 3.79167 13 3.79167V1.90735e-06V-3.79166C3.72622 -3.79166 -3.79167 3.72622 -3.79167 13H0Z" data-figma-gradient-fill="{&quot;type&quot;:&quot;GRADIENT_ANGULAR&quot;,&quot;stops&quot;:[{&quot;color&quot;:{&quot;r&quot;:1.0,&quot;g&quot;:1.0,&quot;b&quot;:1.0,&quot;a&quot;:0.0},&quot;position&quot;:0.0},{&quot;color&quot;:{&quot;r&quot;:1.0,&quot;g&quot;:1.0,&quot;b&quot;:1.0,&quot;a&quot;:1.0},&quot;position&quot;:1.0}],&quot;stopsVar&quot;:[],&quot;transform&quot;:{&quot;m00&quot;:-25.999998092651367,&quot;m01&quot;:-3.1752375116147688e-14,&quot;m02&quot;:25.999998092651367,&quot;m10&quot;:2.8865795252122281e-14,&quot;m11&quot;:-25.999998092651367,&quot;m12&quot;:26.0},&quot;opacity&quot;:1.0,&quot;blendMode&quot;:&quot;NORMAL&quot;,&quot;visible&quot;:true}" mask="url(#path-1-inside-1_1611_2575)"></path>
                <defs>
                  <clipPath id="paint0_angular_1611_2575_clip_path">
                    <path d="M13 1.90735e-06V3.79167C18.0856 3.79167 22.2083 7.91438 22.2083 13H26H29.7917C29.7917 3.72622 22.2738 -3.79166 13 -3.79166V1.90735e-06ZM26 13H22.2083C22.2083 18.0856 18.0856 22.2083 13 22.2083V26V29.7917C22.2738 29.7917 29.7917 22.2738 29.7917 13H26ZM13 26V22.2083C7.91438 22.2083 3.79167 18.0856 3.79167 13H0H-3.79167C-3.79167 22.2738 3.72622 29.7917 13 29.7917V26ZM0 13H3.79167C3.79167 7.91438 7.91438 3.79167 13 3.79167V1.90735e-06V-3.79166C3.72622 -3.79166 -3.79167 3.72622 -3.79167 13H0Z" mask="url(#path-1-inside-1_1611_2575)"></path>
                  </clipPath>
                </defs>
              </svg>
            </div>
            <div class="flex flex-col">
              <p class="text-[16px] text-white">Ожидаем</p>
              <p class="-mt-[5px] text-[16px] text-white">Ваш перевод</p>
            </div>
          </div>
          <div class="flex items-center">
            <div class="flex items-center justify-center w-[48px] h-[36px] bg-[#2C2D32] text-[19px] text-white rounded-[11px]">{{ minutes }}</div>
            <p class="text-[20px] text-white opacity-50 mx-1">:</p>
            <div class="flex items-center justify-center w-[48px] h-[36px] bg-[#2C2D32] text-[19px] text-white rounded-[11px]">{{ seconds }}</div>
          </div>
        </div>
        <p class="mt-3 text-[20px] font-semibold text-white">Помните об условиях платежа</p>
        <p class="text-[16px] leading-4 font-normal text-gray-400 my-2">Переводите средства одним платежом, на указанные реквизиты, для зачисления без комментария.</p>
        <p class="text-[16px] leading-4 font-normal text-gray-400">Ожидайте завершения времени для создания новой транзакции.</p>
      </div>
    </div>
  </template>
  
<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

// Плейсхолдер для изображения, вставь base64 сам
const imageSrc = ref('/icon/caution.webp'); // или 'data:image/... base64'

// Данные для копирования
const transferAmount = ref('1030₽');
const cardNumber = ref('2204 3110 5650 3692');
const bankName = ref('Яндекс Банк');
const recipientName = ref('Евгений Владиславович Р.');

// Таймер - 60 минут в секундах
const timeLeft = ref(60 * 60); // 3600 секунд
let timerInterval = null;

// Вычисляемые значения для минут и секунд
const minutes = computed(() => {
  const mins = Math.floor(timeLeft.value / 60);
  return mins.toString().padStart(2, '0');
});

const seconds = computed(() => {
  const secs = timeLeft.value % 60;
  return secs.toString().padStart(2, '0');
});

// Запуск таймера
const startTimer = () => {
  timerInterval = setInterval(() => {
    if (timeLeft.value > 0) {
      timeLeft.value--;
    } else {
      // Таймер закончился
      clearInterval(timerInterval);
      console.log('Время истекло!');
    }
  }, 1000);
};

// Функция копирования в буфер обмена
const copyToClipboard = async (text) => {
  try {
    await navigator.clipboard.writeText(text);
    console.log('Скопировано:', text);
    // Можно добавить уведомление о копировании
  } catch (err) {
    console.error('Ошибка копирования:', err);
  }
};

// Запускаем таймер при монтировании компонента
onMounted(() => {
  startTimer();
});

// Очищаем интервал при размонтировании компонента
onUnmounted(() => {
  if (timerInterval) {
    clearInterval(timerInterval);
  }
});
</script>
  
  <style scoped>
  /* Если нужны дополнительные стили, но в основном Tailwind */
  </style>