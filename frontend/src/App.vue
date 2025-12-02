<template>
  <div v-if="isLoginPage" class="login-wrapper">
    <router-view />
  </div>
  
  <div v-else class="app-layout">
    <aside class="sidebar">
      <div class="sidebar-header">
        Labor Admin
      </div>
      <nav class="sidebar-nav">
        <router-link to="/" class="nav-item" active-class="active">仪表盘</router-link>
        <router-link to="/items" class="nav-item" active-class="active">商品管理</router-link>
        <router-link to="/warehouses" class="nav-item" active-class="active">仓库管理</router-link>
        <router-link to="/inventory" class="nav-item" active-class="active">库存流水</router-link>
        <router-link to="/stock" class="nav-item" active-class="active">库存总览</router-link>
        <router-link to="/finance" class="nav-item" active-class="active">财务管理</router-link>
      </nav>
    </aside>

    <main class="main-content">
      <header class="top-bar">
        <div><!-- Breadcrumbs or Title could go here --></div>
        <div class="user-menu">
          <button class="secondary" @click="handleLogout">退出登录</button>
        </div>
      </header>
      
      <div class="page-content">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const route = useRoute()
const router = useRouter()

const isLoginPage = computed(() => {
  return route.path === '/login'
})

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/login')
}
</script>

<style scoped>
.login-wrapper {
  min-height: 100vh;
  background-color: var(--color-bg);
}
</style>
