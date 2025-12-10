<template>
  <div>
    <h2>{{ $t('dashboard.title') }}</h2>
    
    <div class="grid-dashboard">
      <div class="card">
        <h3>{{ $t('dashboard.welcome') }}</h3>
        <p>{{ $t('dashboard.intro') }}</p>
      </div>
      
      <!-- Placeholder for future stats -->
      <div class="card">
        <h3>{{ $t('dashboard.quickAccess') }}</h3>
        <div class="flex gap-4">
          <button @click="$router.push('/items')">{{ $t('dashboard.manageItems') }}</button>
          <button @click="$router.push('/inventory')" class="secondary">{{ $t('dashboard.viewInventory') }}</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.grid-dashboard {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 24px;
}
</style>
