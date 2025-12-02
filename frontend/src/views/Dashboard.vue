<template>
  <div>
    <h2>仪表盘</h2>
    
    <div class="grid-dashboard">
      <div class="card">
        <h3>欢迎回来</h3>
        <p>这里是系统概览。请从左侧菜单选择功能。</p>
      </div>
      
      <!-- Placeholder for future stats -->
      <div class="card">
        <h3>快速入口</h3>
        <div class="flex gap-4">
          <button @click="$router.push('/items')">管理商品</button>
          <button @click="$router.push('/inventory')" class="secondary">查看库存</button>
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
