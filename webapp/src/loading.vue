<template>
  <div class="loading-container">
    <!-- Пульсирующее сияние на заднем плане -->
    <div class="glow-pulse"></div>
    <div class="glow-pulse-secondary"></div>
    
    <!-- Центрированный логотип -->
    <div class="logo-container">
      <div class="mini-logo">
        <svg width="139" height="164" viewBox="0 0 139 164" fill="none" xmlns="http://www.w3.org/2000/svg">
          <g filter="url(#filter0_i_1670_1321)">
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="#FEFEFE"/>
            <path d="M88.1523 86.2574L88.266 86.1434C105.138 69.2498 111.053 63.4413 111.372 63.4839C111.797 63.5476 111.798 63.7388 111.904 115.213L111.904 115.356L111.415 115.463C111.032 115.548 110.053 114.654 105.628 110.165C102.692 107.186 100.096 104.654 99.8192 104.526C99.5639 104.399 99.117 104.292 98.8192 104.292C98.5213 104.292 98.0745 104.399 97.7979 104.548C97.5426 104.675 89.9255 112.186 80.883 121.25C71.8404 130.292 64.3298 137.697 64.1809 137.697C64.0319 137.697 63.7979 137.59 63.649 137.441C63.4362 137.229 63.3936 134.76 63.3936 126.101C63.3936 117.207 63.4575 114.739 63.7128 113.548C63.883 112.718 64.3724 111.335 64.7979 110.463C65.5413 108.912 66.2635 108.188 88.1523 86.2574Z" fill="#FEFEFE"/>
          </g>
          <g opacity="0.05" filter="url(#filter1_i_1670_1321)">
            <path d="M55.3421 75.7155L75.374 55.6423C86.3979 44.5956 95.4314 35.5691 95.4825 35.5691C95.508 35.5691 95.7632 35.6969 96.0439 35.8248C96.5542 36.0805 96.5542 36.3362 96.5542 49.3774C96.5542 60.5008 96.4777 63.0067 96.1459 64.6433C95.9163 65.7428 95.3293 67.4305 94.8445 68.4278C93.9769 70.0899 91.8333 72.3146 66.7233 97.5275C46.4872 117.831 39.3931 124.812 39.0104 124.761C38.5 124.684 38.5 124.479 38.5 93.6152C38.5 62.751 38.5 62.5464 39.0104 62.4697C39.3931 62.393 41.2049 64.0807 52.7903 75.7155C53.6325 75.8843 54.4999 75.8843 55.3421 75.7155Z" fill="#FEFEFE"/>
            <path d="M90.0127 85.237L90.1491 85.1C110.385 64.7967 117.479 57.8158 117.862 57.867C118.372 57.9436 118.372 58.1734 118.5 120.037L118.5 120.209L117.913 120.337C117.454 120.439 116.28 119.365 110.972 113.97C107.451 110.39 104.337 107.347 104.006 107.193C103.699 107.04 103.163 106.912 102.806 106.912C102.449 106.912 101.913 107.04 101.581 107.219C101.275 107.372 92.1395 116.399 81.2943 127.292C70.449 138.16 61.441 147.058 61.2624 147.058C61.0837 147.058 60.803 146.931 60.6244 146.752C60.3692 146.496 60.3182 143.53 60.3182 133.122C60.3182 122.434 60.3947 119.467 60.701 118.035C60.9051 117.038 61.492 115.376 62.0024 114.328C62.894 112.464 63.7602 111.595 90.0127 85.237Z" fill="#FEFEFE"/>
          </g>
          <g filter="url(#filter2_ii_1670_1321)">
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="#FEFEFE"/>
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="url(#paint0_linear_1670_1321)"/>
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="url(#paint1_linear_1670_1321)"/>
          </g>
          <g opacity="0.4" filter="url(#filter3_if_1670_1321)">
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="#FEFEFE"/>
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="url(#paint2_linear_1670_1321)"/>
            <path d="M59.2447 78.3349L75.9468 61.6328C85.1383 52.4413 92.6702 44.9307 92.7128 44.9307C92.7341 44.9307 92.9468 45.037 93.1809 45.1434C93.6064 45.3562 93.6064 45.569 93.6064 56.42C93.6064 65.6753 93.5426 67.7605 93.266 69.1222C93.0745 70.037 92.5851 71.4413 92.1809 72.2711C91.4575 73.6541 89.6702 75.5051 68.7341 96.4839C51.8617 113.377 45.9468 119.186 45.6277 119.143C45.2021 119.08 45.2021 118.909 45.2021 93.2285C45.2021 67.5477 45.2021 67.3775 45.6277 67.3136C45.9468 67.2498 47.4575 68.6541 57.117 78.3349C57.8193 78.4754 58.5424 78.4754 59.2447 78.3349Z" fill="url(#paint3_linear_1670_1321)"/>
          </g>
          <defs>
            <filter id="filter0_i_1670_1321" x="45.2021" y="44.9307" width="66.7021" height="93.6169" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
              <feFlood flood-opacity="0" result="BackgroundImageFix"/>
              <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
              <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
              <feOffset dy="0.851064"/>
              <feGaussianBlur stdDeviation="1.26596"/>
              <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
              <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.4 0"/>
              <feBlend mode="normal" in2="shape" result="effect1_innerShadow_1670_1321"/>
            </filter>
            <filter id="filter1_i_1670_1321" x="38.5" y="35.5691" width="80" height="112.34" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
              <feFlood flood-opacity="0" result="BackgroundImageFix"/>
              <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
              <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
              <feOffset dy="0.851064"/>
              <feGaussianBlur stdDeviation="1.26596"/>
              <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
              <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.4 0"/>
              <feBlend mode="normal" in2="shape" result="effect1_innerShadow_1670_1321"/>
            </filter>
            <filter id="filter2_ii_1670_1321" x="45.2021" y="44.9307" width="48.4043" height="75.064" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
              <feFlood flood-opacity="0" result="BackgroundImageFix"/>
              <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
              <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
              <feOffset dy="0.851064"/>
              <feGaussianBlur stdDeviation="1.26596"/>
              <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
              <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.4 0"/>
              <feBlend mode="normal" in2="shape" result="effect1_innerShadow_1670_1321"/>
              <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
              <feOffset dy="0.851064"/>
              <feGaussianBlur stdDeviation="1.55319"/>
              <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
              <feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.7 0"/>
              <feBlend mode="normal" in2="effect1_innerShadow_1670_1321" result="effect2_innerShadow_1670_1321"/>
            </filter>
            <filter id="filter3_if_1670_1321" x="0.393639" y="0.122154" width="138.021" height="163.83" filterUnits="userSpaceOnUse" color-interpolation-filters="sRGB">
              <feFlood flood-opacity="0" result="BackgroundImageFix"/>
              <feBlend mode="normal" in="SourceGraphic" in2="BackgroundImageFix" result="shape"/>
              <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0" result="hardAlpha"/>
              <feOffset dy="0.851064"/>
              <feGaussianBlur stdDeviation="1.26596"/>
              <feComposite in2="hardAlpha" operator="arithmetic" k2="-1" k3="1"/>
              <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.4 0"/>
              <feBlend mode="normal" in2="shape" result="effect1_innerShadow_1670_1321"/>
              <feGaussianBlur stdDeviation="22.4043" result="effect2_foregroundBlur_1670_1321"/>
            </filter>
            <linearGradient id="paint0_linear_1670_1321" x1="84.6517" y1="44.9307" x2="84.6517" y2="137.697" gradientUnits="userSpaceOnUse">
              <stop stop-color="#DBFE01"/>
              <stop offset="1" stop-color="#E8FF56"/>
            </linearGradient>
            <linearGradient id="paint1_linear_1670_1321" x1="78.2873" y1="44.9307" x2="78.2873" y2="137.697" gradientUnits="userSpaceOnUse">
              <stop stop-color="#B3F106"/>
              <stop offset="1" stop-color="#5EFF03"/>
            </linearGradient>
            <linearGradient id="paint2_linear_1670_1321" x1="84.6517" y1="44.9307" x2="84.6517" y2="137.697" gradientUnits="userSpaceOnUse">
              <stop stop-color="#DBFE01"/>
              <stop offset="1" stop-color="#E8FF56"/>
            </linearGradient>
            <linearGradient id="paint3_linear_1670_1321" x1="78.2873" y1="44.9307" x2="78.2873" y2="137.697" gradientUnits="userSpaceOnUse">
              <stop stop-color="#B3F106"/>
              <stop offset="1" stop-color="#5EFF03"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
    </div>
  </div>
</template>

<script setup>
// Компонент загрузки с пульсирующим эффектом
</script>

<style scoped>
.loading-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #0b0c0d;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
  overflow: hidden;
}

/* Основное пульсирующее сияние */
.glow-pulse {
  position: absolute;
  width: 400px;
  height: 550px;
  background: radial-gradient(
    ellipse,
    rgba(219, 254, 1, 0.2) 0%,
    rgba(179, 241, 6, 0.15) 25%,
    rgba(94, 255, 3, 0.1) 50%,
    rgba(94, 255, 3, 0.05) 75%,
    transparent 100%
  );
  border-radius: 50%;
  animation: pulse-primary 2s ease-in-out infinite alternate;
  filter: blur(20px);
}

/* Вторичное пульсирующее сияние */
.glow-pulse-secondary {
  position: absolute;
  width: 280px;
  height: 400px;
  background: radial-gradient(
    ellipse,
    rgba(219, 254, 1, 0.3) 0%,
    rgba(179, 241, 6, 0.2) 30%,
    rgba(94, 255, 3, 0.15) 60%,
    transparent 100%
  );
  border-radius: 50%;
  animation: pulse-secondary 1.5s ease-in-out infinite alternate;
  filter: blur(15px);
}

.logo-container {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: center;
}

.mini-logo {
  width: 150px;
  height: auto;
  filter: drop-shadow(0 0 30px rgba(219, 254, 1, 0.5));
}

.mini-logo svg {
  width: 100%;
  height: auto;
}

/* Анимации */
@keyframes pulse-primary {
  0% {
    transform: scale(0.8);
    opacity: 0.6;
  }
  100% {
    transform: scale(1.2);
    opacity: 0.2;
  }
}

@keyframes pulse-secondary {
  0% {
    transform: scale(1.1);
    opacity: 0.4;
  }
  100% {
    transform: scale(0.9);
    opacity: 0.8;
  }
}

/* Медиа запросы для мобильных устройств */
@media (max-width: 768px) {
  .glow-pulse {
    width: 250px;
    height: 350px;
  }
  
  .glow-pulse-secondary {
    width: 180px;
    height: 250px;
  }
  
  .mini-logo {
    width: 140px;
  }
}

@media (max-width: 480px) {
  .glow-pulse {
    width: 200px;
    height: 280px;
  }
  
  .glow-pulse-secondary {
    width: 140px;
    height: 200px;
  }
  
  .mini-logo {
    width: 120px;
  }
}</style>
