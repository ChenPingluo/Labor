<template>
  <div class="login-container">
    <div class="login-card">
      <h2 class="login-title">{{ $t('login.title') }}</h2>

      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>{{ $t('common.username') }}</label>
          <input v-model="form.username" :placeholder="$t('login.usernamePlaceholder')" required />
        </div>
        
        <div class="form-group">
          <label>{{ $t('common.password') }}</label>
          <input v-model="form.password" type="password" :placeholder="$t('login.passwordPlaceholder')" required />
        </div>

        <button type="submit" class="w-full" style="margin-top: 16px;">{{ $t('login.loginButton') }}</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { login } from '../api/auth'
import { useRouter } from 'vue-router'
import { useI18n } from 'vue-i18n'

const router = useRouter()
const { t } = useI18n()

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
    alert(t('login.loginFailed'))
  }
}
</script>
