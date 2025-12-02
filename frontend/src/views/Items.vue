<template>
  <div>
    <div class="flex justify-between items-center mb-4">
      <h2>商品管理</h2>
    </div>

    <div class="card">
      <h3>新增商品</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>SKU</label>
          <input v-model="form.sku" placeholder="例如: ITEM-001" />
        </div>
        <div style="flex: 1;">
          <label>商品名称</label>
          <input v-model="form.name" placeholder="例如: 螺丝刀" />
        </div>
        <div style="width: 120px;">
          <label>单位</label>
          <input v-model="form.unit" placeholder="pcs" />
        </div>
        <button type="submit">添加</button>
      </form>
    </div>

    <div class="card">
      <h3>商品列表</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>SKU</th>
              <th>名称</th>
              <th>单位</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in items" :key="item.id">
              <td>{{ item.id }}</td>
              <td>{{ item.sku }}</td>
              <td>{{ item.name }}</td>
              <td>{{ item.unit }}</td>
            </tr>
            <tr v-if="items.length === 0">
              <td colspan="4" style="text-align: center; color: #999;">暂无数据</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchItems, createItem } from '../api/items'

const items = ref([])
const form = ref({
  sku: '',
  name: '',
  unit: 'pcs',
})

const loadItems = async () => {
  const res = await fetchItems()
  items.value = res.data || []
}

const handleCreate = async () => {
  if (!form.value.sku || !form.value.name) {
    alert('sku 和 名称 必填')
    return
  }
  await createItem(form.value)
  form.value = { sku: '', name: '', unit: 'pcs' }
  await loadItems()
}

onMounted(loadItems)
</script>
