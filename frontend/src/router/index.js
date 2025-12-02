import { createRouter, createWebHistory } from 'vue-router'
import Items from '../views/Items.vue'
import Inventory from '../views/Inventory.vue'
import Warehouses from '../views/Warehouses.vue'
import Stock from '../views/Stock.vue'
import Login from '../views/Login.vue'
import Finance from '../views/Finance.vue'



const routes = [
  { path: '/', redirect: '/items' },  // 默认跳转到商品页面
  { path: '/items', name: 'Items', component: Items },
  { path: '/inventory', name: 'Inventory', component: Inventory },
  { path: '/warehouses', name: 'Warehouses', component: Warehouses },
  { path: '/stock', name: 'Stock', component: Stock },
  { path: '/login', name: 'Login', component: Login },
  { path: '/finance', name: 'Finance', component: Finance }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  if (!token && to.path !== '/login') {
    return next('/login')
  }
  next()
})


export default router
