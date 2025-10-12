<template>
    <div class="mt-5 flex space-x-2 items-center">
      <svg viewBox="0 0 21.873 22" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="21.873047" height="22" fill="none" customFrame="#000000" class="filter drop-shadow-[0_0_12px_rgba(94,255,3,0.7)]">
        <path id="Vector" d="M13.756 0L8.116 0L7.469 3.237C6.93331 3.47706 6.42392 3.77197 5.949 4.117L2.819 3.058L0 7.942L2.481 10.122C2.42108 10.7058 2.42108 11.2942 2.481 11.878L0 14.058L2.82 18.942L5.949 17.884C6.421 18.226 6.929 18.522 7.469 18.763L8.116 22L13.756 22L14.403 18.763C14.9387 18.5229 15.4481 18.228 15.923 17.883L19.053 18.942L21.873 14.058L19.391 11.878C19.4509 11.2942 19.4509 10.7058 19.391 10.122L21.872 7.942L19.052 3.058L15.924 4.116C15.449 3.77131 14.9397 3.47674 14.404 3.237L13.756 0ZM10.936 15C9.87513 15 8.85772 14.5786 8.10757 13.8284C7.35743 13.0783 6.936 12.0609 6.936 11C6.936 9.93913 7.35743 8.92172 8.10757 8.17157C8.85772 7.42143 9.87513 7 10.936 7C11.9969 7 13.0143 7.42143 13.7644 8.17157C14.5146 8.92172 14.936 9.93913 14.936 11C14.936 12.0609 14.5146 13.0783 13.7644 13.8284C13.0143 14.5786 11.9969 15 10.936 15Z" fill="rgb(144,247,5)" fill-rule="nonzero"></path>
      </svg>
      <p class="text-[20px]">Настройки</p>
    </div>
  
    <div class="flex flex-col space-y-2 mt-2">
      <div class="h-[50px] rounded-[20px] border border-[#2A2B2D] flex items-center justify-between pl-5 pr-3" style="background: linear-gradient(178.77deg, rgb(20, 21, 24) 0%, rgb(30, 32, 37) 100%);">
        <div class="flex items-center space-x-3">
          <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" fill="none" class="-translate-y-[2px]">
            <rect id="subway:sound-1" width="20" height="20" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
            <path id="Vector" d="M15.2734 10C15.2734 8.61328 14.4258 7.42578 13.2227 6.92578L12.582 8.46484C13.1836 8.71484 13.6055 9.30859 13.6055 10.0039C13.6055 10.6953 13.1836 11.2891 12.582 11.543L13.2227 13.082C14.4258 12.5742 15.2734 11.3867 15.2734 10ZM14.5039 3.84766L13.8633 5.38672C15.6719 6.14062 16.9414 7.92188 16.9414 10C16.9414 12.082 15.6719 13.8594 13.8633 14.6133L14.5039 16.1523C16.9141 15.1484 18.6055 12.7734 18.6055 10C18.6055 7.22656 16.9141 4.85156 14.5039 3.84766ZM1.94141 5.83203L1.94141 14.1641L5.27344 14.1641L11.1055 20L11.1055 0L5.27344 5.83203L1.94141 5.83203Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
          </svg>
          <p class="text-[20px]">Вибрации</p>
        </div>
        <button type="button" role="switch" aria-checked="true" data-state="checked" value="on" data-slot="switch" class="peer bg-black data-[state=checked]:bg-[#76FB04]/50 data-[state=unchecked]:bg-black focus-visible:border-ring focus-visible:ring-ring/50 inline-flex h-[24px] w-11 shrink-0 items-center rounded-full border border-[#55575990] shadow-xs transition-all outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50">
          <span data-state="checked" data-slot="switch-thumb" class="pointer-events-none block w-[24px] h-[24px] rounded-full ring-0 transition-transform data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=unchecked]:translate-x-0 box-border border-[1.45px] border-white/10" style="background: linear-gradient(rgb(186, 243, 30) 0%, rgb(110, 253, 31) 100%);"></span>
        </button>
      </div>
      <div class="h-[50px] rounded-[20px] border border-[#2A2B2D] flex items-center justify-between pl-5 pr-3" style="background: linear-gradient(178.77deg, rgb(20, 21, 24) 0%, rgb(30, 32, 37) 100%);">
        <div class="flex items-center space-x-3">
          <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" fill="none" class="-translate-y-[2px]">
            <rect id="ant-design:sound-filled" width="20" height="20" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
            <path id="Vector" d="M17.4238 14.4102L15.2695 13.166C15.2341 13.1458 15.1951 13.1327 15.1546 13.1275C15.1142 13.1223 15.0731 13.1251 15.0337 13.1358C14.9944 13.1465 14.9575 13.1649 14.9253 13.1898C14.893 13.2148 14.866 13.2459 14.8457 13.2812L14.457 13.9551C14.3711 14.1035 14.4219 14.2949 14.5703 14.3809L16.7246 15.625C16.76 15.6453 16.799 15.6584 16.8395 15.6635C16.88 15.6687 16.921 15.6659 16.9604 15.6552C16.9997 15.6445 17.0366 15.6261 17.0689 15.6012C17.1011 15.5762 17.1282 15.5452 17.1484 15.5098L17.5371 14.8359C17.623 14.6875 17.5703 14.4961 17.4238 14.4102ZM14.8438 6.71875C14.864 6.75415 14.891 6.78521 14.9233 6.81016C14.9556 6.83511 14.9924 6.85345 15.0318 6.86415C15.0712 6.87486 15.1122 6.8777 15.1527 6.87252C15.1931 6.86735 15.2322 6.85425 15.2676 6.83398L17.4219 5.58984C17.5703 5.50391 17.6211 5.3125 17.5352 5.16406L17.1484 4.49219C17.1282 4.45679 17.1011 4.42573 17.0689 4.40078C17.0366 4.37583 16.9997 4.35748 16.9604 4.34678C16.921 4.33608 16.88 4.33324 16.8395 4.33842C16.799 4.34359 16.76 4.35669 16.7246 4.37695L14.5703 5.62109C14.499 5.66268 14.447 5.73081 14.4258 5.8106C14.4046 5.89039 14.4158 5.97534 14.457 6.04688L14.8438 6.71875ZM18.2422 9.29688L15.7422 9.29688C15.5703 9.29688 15.4297 9.4375 15.4297 9.60938L15.4297 10.3906C15.4297 10.5625 15.5703 10.7031 15.7422 10.7031L18.2422 10.7031C18.4141 10.7031 18.5547 10.5625 18.5547 10.3906L18.5547 9.60938C18.5547 9.4375 18.4141 9.29688 18.2422 9.29688ZM12.2246 2.24609C12.1094 2.24609 11.9922 2.27734 11.8848 2.34961L4.96094 6.875L1.75781 6.875C1.58594 6.875 1.44531 7.01562 1.44531 7.1875L1.44531 12.8125C1.44531 12.9844 1.58594 13.125 1.75781 13.125L4.96094 13.125L11.8848 17.6504C11.9922 17.7207 12.1113 17.7539 12.2246 17.7539C12.5508 17.7539 12.8516 17.4941 12.8516 17.127L12.8516 2.87305C12.8516 2.50586 12.5508 2.24609 12.2246 2.24609Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
          </svg>
          <p class="text-[20px]">Звук</p>
        </div>
        <button type="button" role="switch" aria-checked="true" data-state="checked" value="on" data-slot="switch" class="peer bg-black data-[state=checked]:bg-[#76FB04]/50 data-[state=unchecked]:bg-black focus-visible:border-ring focus-visible:ring-ring/50 inline-flex h-[24px] w-11 shrink-0 items-center rounded-full border border-[#55575990] shadow-xs transition-all outline-none focus-visible:ring-[3px] disabled:cursor-not-allowed disabled:opacity-50">
          <span data-state="checked" data-slot="switch-thumb" class="pointer-events-none block w-[24px] h-[24px] rounded-full ring-0 transition-transform data-[state=checked]:translate-x-[calc(100%-2px)] data-[state=unchecked]:translate-x-0 box-border border-[1.45px] border-white/10" style="background: linear-gradient(rgb(186, 243, 30) 0%, rgb(110, 253, 31) 100%);"></span>
        </button>
      </div>
      <div class="h-[50px] rounded-[20px] border border-[#2A2B2D] flex items-center justify-between pl-5 pr-3" style="background: linear-gradient(178.77deg, rgb(20, 21, 24) 0%, rgb(30, 32, 37) 100%);">
        <div class="flex items-center space-x-3">
          <svg viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="20" height="20" fill="none" class="-translate-y-[2px]">
            <rect id="fluent:person-support-20-filled" width="20" height="20" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
            <path id="Vector" d="M10 14.5C9.49719 14.5001 9.01279 14.3108 8.64327 13.9698C8.27375 13.6289 8.04622 13.1612 8.006 12.66C6.67219 12.1879 5.54805 11.2597 4.83202 10.0394C4.116 8.81901 3.85412 7.38493 4.09263 5.99027C4.33113 4.59561 5.05468 3.33005 6.13554 2.41698C7.21641 1.50392 8.5851 1.00206 10 1C11.5049 0.999782 12.9549 1.56509 14.0626 2.58383C15.1702 3.60256 15.8546 5.00034 15.98 6.5C15.9842 6.56505 15.9748 6.63026 15.9524 6.69148C15.93 6.7527 15.8952 6.8086 15.85 6.85562C15.8049 6.90264 15.7504 6.93976 15.6902 6.96461C15.6299 6.98947 15.5652 7.00152 15.5 7C15.3661 6.99664 15.2381 6.94361 15.1411 6.8512C15.0441 6.7588 14.9849 6.63362 14.975 6.5C14.8859 5.61584 14.5628 4.77138 14.039 4.05357C13.5151 3.33576 12.8094 2.77054 11.9945 2.41609C11.1796 2.06163 10.285 1.93076 9.40274 2.03694C8.52046 2.14313 7.68243 2.48252 6.97491 3.0202C6.26739 3.55787 5.71594 4.27439 5.37735 5.096C5.03876 5.9176 4.92525 6.8146 5.04851 7.69465C5.17177 8.5747 5.52734 9.406 6.07863 10.103C6.62991 10.7999 7.35699 11.3374 8.185 11.66C8.33566 11.3345 8.57111 11.0554 8.86667 10.8521C9.16224 10.6489 9.50703 10.5288 9.86493 10.5046C10.2228 10.4803 10.5807 10.5528 10.9009 10.7144C11.2212 10.876 11.4921 11.1207 11.6853 11.423C11.8785 11.7253 11.9868 12.0739 11.9989 12.4324C12.011 12.7909 11.9265 13.1461 11.7542 13.4607C11.5819 13.7754 11.3281 14.0379 11.0195 14.2207C10.7108 14.4035 10.3587 14.5 10 14.5ZM5.009 12L5.1 12C5.69036 12.5791 6.37866 13.0491 7.133 13.388C7.35469 14.1194 7.84719 14.7387 8.50997 15.1193C9.17274 15.5 9.95581 15.6133 10.6993 15.4362C11.4428 15.259 12.0906 14.8048 12.5106 14.1662C12.9305 13.5276 13.0909 12.7528 12.959 12L15 12C15.5304 12 16.0391 12.2107 16.4142 12.5858C16.7893 12.9609 17 13.4696 17 14C17 15.691 16.167 16.966 14.865 17.797C13.583 18.614 11.855 19 10 19C8.145 19 6.417 18.614 5.135 17.797C3.833 16.967 3 15.69 3 14C3 12.887 3.903 12 5.009 12ZM14 7C14.0002 7.67664 13.8288 8.34227 13.5017 8.93463C13.1747 9.52698 12.7027 10.0267 12.13 10.387C11.8511 10.1059 11.5193 9.88278 11.1537 9.73054C10.7881 9.5783 10.396 9.49995 10 9.5C9.60399 9.49995 9.21189 9.5783 8.84632 9.73054C8.48074 9.88278 8.14892 10.1059 7.87 10.387C7.11042 9.90932 6.53351 9.19012 6.232 8.345C6.07818 7.91327 5.99971 7.45831 6 7C6 5.93913 6.42143 4.92172 7.17157 4.17157C7.92172 3.42143 8.93913 3 10 3C11.0609 3 12.0783 3.42143 12.8284 4.17157C13.5786 4.92172 14 5.93913 14 7Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
          </svg>
          <p class="text-[20px]">Поддержка</p>
        </div>
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" opacity="0.300000012" fill="none">
          <rect id="chevron-left" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0" transform="matrix(-1,-8.32667e-17,8.32667e-17,-1,24,24)"></rect>
          <path id="vector" d="M6 12L0 6L6 0" fill-rule="nonzero" stroke="rgb(255,255,255)" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" transform="matrix(-1,-8.32667e-17,8.32667e-17,-1,15,18)"></path>
        </svg>
      </div>
      <div class="h-[50px] rounded-[20px] border border-[#2A2B2D] flex items-center justify-between pl-5 pr-3" style="background: linear-gradient(178.77deg, rgb(20, 21, 24) 0%, rgb(30, 32, 37) 100%);">
        <div class="flex items-center space-x-3">
          <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" fill="none" class="-translate-y-[2px]">
            <rect id="mdi:heart" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0"></rect>
            <path id="Vector" d="M12 21.35L10.55 20.03C5.4 15.36 2 12.27 2 8.5C2 5.41 4.42 3 7.5 3C9.24 3 10.91 3.81 12 5.08C13.09 3.81 14.76 3 16.5 3C19.58 3 22 5.41 22 8.5C22 12.27 18.6 15.36 13.45 20.03L12 21.35Z" fill="rgb(255,255,255)" fill-rule="nonzero"></path>
          </svg>
          <p class="text-[20px]">Подписаться на канал</p>
        </div>
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24" opacity="0.300000012" fill="none">
          <rect id="chevron-left" width="24" height="24" x="0" y="0" fill="rgb(255,255,255)" fill-opacity="0" transform="matrix(-1,-8.32667e-17,8.32667e-17,-1,24,24)"></rect>
          <path id="vector" d="M6 12L0 6L6 0" fill-rule="nonzero" stroke="rgb(255,255,255)" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" transform="matrix(-1,-8.32667e-17,8.32667e-17,-1,15,18)"></path>
        </svg>
      </div>
    </div>
  </template>
  
  <script setup>
  // No script needed for static content, but if you want to make switches interactive, you can add logic here.
  </script>