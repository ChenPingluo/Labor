<template>
  <div>
    <h2>{{ $t('stock.title') }}</h2>

    <div class="card">
      <h3>{{ $t('stock.filter') }}</h3>
      <div class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>{{ $t('common.item') }}</label>
          <select v-model="filters.item_id">
            <option value="">{{ $t('stock.allItems') }}</option>
            <option v-for="i in items" :key="i.id" :value="i.id">
              {{ i.sku }} - {{ i.name }}
            </option>
          </select>
        </div>

        <div style="flex: 1;">
          <label>{{ $t('common.warehouse') }}</label>
          <select v-model="filters.warehouse_id">
            <option value="">{{ $t('stock.allWarehouses') }}</option>
            <option v-for="w in warehouses" :key="w.id" :value="w.id">
              {{ w.name }}
            </option>
          </select>
        </div>

        <button @click="loadStock" style="height: 34px; padding: 0 20px; align-self: flex-end;">{{ $t('common.query') }}</button>
      </div>
    </div>

    <div class="card">
      <h3>{{ $t('stock.result') }}</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>{{ $t('common.item') }}</th>
              <th>{{ $t('items.sku') }}</th>
              <th>{{ $t('common.warehouse') }}</th>
              <th>{{ $t('stock.currentStock') }}</th>
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
              <td colspan="4" style="text-align: center; color: #999;">{{ $t('common.noData') }}</td>
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
