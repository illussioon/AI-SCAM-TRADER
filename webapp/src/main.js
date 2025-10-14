import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import { pinia } from './stores/index.js'
import { API_CONFIG, API_URLS, buildApiUrl } from './config/api.js'

const app = createApp(App)

// Добавляем глобальные переменные для API
app.config.globalProperties.$api = {
  domain: API_CONFIG.DOMAIN,
  urls: API_URLS,
  buildUrl: buildApiUrl,
  config: API_CONFIG
}

// Для удобного доступа в консоли браузера
window.API_DOMAIN = API_CONFIG.DOMAIN
window.API_URLS = API_URLS

app.use(pinia)
app.use(router)

app.mount('#app')

// Логируем конфигурацию для отладки
console.log('🌐 API Domain:', API_CONFIG.DOMAIN)
console.log('📋 Available API URLs:', API_URLS)
