<template>
  <div>
    <h2>仓库管理</h2>

    <div class="card">
      <h3>新增仓库</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>仓库名称</label>
          <input v-model="form.name" placeholder="例如: 主仓库" />
        </div>
        <div style="flex: 1;">
          <label>位置</label>
          <input v-model="form.location" placeholder="例如: A区" />
        </div>
        <button type="submit">添加</button>
      </form>
    </div>

    <div class="card">
      <h3>仓库列表</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>名称</th>
              <th>位置</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="w in warehouses" :key="w.id">
              <td>{{ w.id }}</td>
              <td>{{ w.name }}</td>
              <td>{{ w.location }}</td>
            </tr>
            <tr v-if="warehouses.length === 0">
              <td colspan="3" style="text-align: center; color: #999;">暂无数据</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchWarehouses, createWarehouse } from '../api/warehouse'

const warehouses = ref([])
const form = ref({
  name: '',
  location: ''
})

const loadWarehouses = async () => {
  const res = await fetchWarehouses()
  warehouses.value = res.data || []
}

const handleCreate = async () => {
  if (!form.value.name) {
    alert('仓库名称必填')
    return
  }
  await createWarehouse(form.value)
  form.value = { name: '', location: '' }
  await loadWarehouses()
}

onMounted(loadWarehouses)
</script>
