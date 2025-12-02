<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="login-title">系统登录</h2>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>用户名</label>
          <input v-model="form.username" placeholder="请输入用户名" required />
        </div>
        
        <div class="form-group">
          <label>密码</label>
          <input v-model="form.password" type="password" placeholder="请输入密码" required />
        </div>

        <button type="submit" class="w-full" style="margin-top: 16px;">登录</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { login } from '../api/auth'
import { useRouter } from 'vue-router'

const router = useRouter()

const form = ref({
  username: '',
  password: ''
})

const handleLogin = async () => {
  try {
    const res = await login(form.value)
    if (res.error) {
      alert(res.error)
      return
    }
    localStorage.setItem('token', res.data.token)
    localStorage.setItem('user', JSON.stringify(res.data.user))
    router.push('/')
  } catch (e) {
    alert('登录失败，请检查网络或联系管理员')
  }
}
</script>
