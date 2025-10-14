import { createRouter, createWebHistory } from 'vue-router'
import MainApp from './components/app/main-app.vue'
import MainTutorial from './components/main/main.vue'
import Wallet from './components/app/wallet/wallet.vue'
import Profile from './components/app/profile/profile.vue'
import Friends from './components/app/friends/friends.vue'
import Cabinet from './components/app/cabinet/cabinet.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: MainApp
  },
  {
    path: '/tutorial',
    name: 'Tutorial', 
    component: MainTutorial
  },
  {
    path: '/wallet',
    name: 'Wallet',
    component: Wallet
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/friends',
    name: 'Friends',
    component: Friends
  },
  {
    path: '/cabinet',
    name: 'Cabinet',
    component: Cabinet
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router


