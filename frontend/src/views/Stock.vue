<template>
  <div>
    <h2>库存总览</h2>

    <div class="card">
      <h3>查询筛选</h3>
      <div class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>商品</label>
          <select v-model="filters.item_id">
            <option value="">全部商品</option>
            <option v-for="i in items" :key="i.id" :value="i.id">
              {{ i.sku }} - {{ i.name }}
            </option>
          </select>
        </div>

        <div style="flex: 1;">
          <label>仓库</label>
          <select v-model="filters.warehouse_id">
            <option value="">全部仓库</option>
            <option v-for="w in warehouses" :key="w.id" :value="w.id">
              {{ w.name }}
            </option>
          </select>
        </div>

        <button @click="loadStock">查询</button>
      </div>
    </div>

    <div class="card">
      <h3>库存结果</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>商品</th>
              <th>SKU</th>
              <th>仓库</th>
              <th>当前库存</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="row in stock" :key="row.item_id + '-' + row.warehouse_id">
              <td>{{ row.item_name }}</td>
              <td>{{ row.item_sku }}</td>
              <td>{{ row.warehouse_name }}</td>
              <td style="font-weight: bold;">{{ row.stock }}</td>
            </tr>
            <tr v-if="stock.length === 0">
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
import { fetchItems } from '../api/items'
import { fetchWarehouses } from '../api/warehouse'
import { fetchStock } from '../api/stock'

const items = ref([])
const warehouses = ref([])
const stock = ref([])

const filters = ref({
  item_id: '',
  warehouse_id: '',
})

const loadBaseData = async () => {
  const itemRes = await fetchItems()
  items.value = itemRes.data || []

  const warehouseRes = await fetchWarehouses()
  warehouses.value = warehouseRes.data || []
}

const loadStock = async () => {
  const res = await fetchStock(filters.value)
  stock.value = res.data || []
}

onMounted(async () => {
  await loadBaseData()
  await loadStock()
})
</script>
