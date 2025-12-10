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
        <router-link to="/" class="nav-item" active-class="active">{{ $t('menu.dashboard') }}</router-link>
        <router-link to="/items" class="nav-item" active-class="active">{{ $t('menu.items') }}</router-link>
        <router-link to="/warehouses" class="nav-item" active-class="active">{{ $t('menu.warehouses') }}</router-link>
        <router-link to="/inventory" class="nav-item" active-class="active">{{ $t('menu.inventory') }}</router-link>
        <router-link to="/stock" class="nav-item" active-class="active">{{ $t('menu.stock') }}</router-link>
        <router-link to="/finance" class="nav-item" active-class="active">{{ $t('menu.finance') }}</router-link>
      </nav>
    </aside>

    <main class="main-content">
      <header class="top-bar">
        <div><!-- Breadcrumbs or Title could go here --></div>
        <div class="user-menu flex items-center gap-4">
          <select v-model="locale" @change="changeLang" class="lang-select">
            <option value="zh">中文</option>
            <option value="en">English</option>
          </select>
          <button class="secondary" @click="handleLogout">{{ $t('common.logout') }}</button>
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
import { useI18n } from 'vue-i18n'

const route = useRoute()
const router = useRouter()
const { locale } = useI18n()

const isLoginPage = computed(() => {
  return route.path === '/login'
})

const changeLang = () => {
  localStorage.setItem('lang', locale.value)
}

const handleLogout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/login')
}
</script>

<style scoped>
.lang-select {
  padding: 4px 8px;
  border-radius: 4px;
  border: 1px solid #ccc;
  margin-right: 10px;
  width: auto;
}
</style>

<style scoped>
.login-wrapper {
  min-height: 100vh;
  background-color: var(--color-bg);
}
</style>
