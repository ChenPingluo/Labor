<template>
  <div>
    <h2>库存流水</h2>

    <div class="card">
      <h3>新增记录</h3>
      <form @submit.prevent="handleCreate">
        <div class="flex gap-4 mb-4">
          <div style="flex: 1;">
            <label>仓库</label>
            <select v-model="form.warehouse_id">
              <option value="">请选择仓库</option>
              <option v-for="w in warehouses" :key="w.id" :value="w.id">
                {{ w.name }}
              </option>
            </select>
          </div>
          <div style="flex: 1;">
            <label>商品</label>
            <select v-model="form.item_id">
              <option value="">请选择商品</option>
              <option v-for="item in items" :key="item.id" :value="item.id">
                {{ item.sku }} - {{ item.name }}
              </option>
            </select>
          </div>
          <div style="width: 120px;">
            <label>类型</label>
            <select v-model="form.type">
              <option value="in">入库</option>
              <option value="out">出库</option>
            </select>
          </div>
        </div>

        <div class="flex gap-4 items-end">
          <div style="flex: 1;">
            <label>数量</label>
            <input v-model.number="form.quantity" type="number" min="0.01" step="0.01" placeholder="0.00" />
          </div>
          <div style="flex: 2;">
            <label>备注</label>
            <input v-model="form.remark" type="text" placeholder="可选备注" />
          </div>
          <button type="submit" style="height: 34px; padding: 0 20px; align-self: flex-end;">保存记录</button>
        </div>
      </form>
    </div>

    <div class="card">
      <h3>流水记录</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>时间</th>
              <th>仓库</th>
              <th>商品</th>
              <th>类型</th>
              <th>数量</th>
              <th>备注</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in records" :key="r.id">
              <td>{{ r.id }}</td>
              <td>{{ r.created_at }}</td>
              <td>{{ r.warehouse_name }}</td>
              <td>{{ r.item_sku }} - {{ r.item_name }}</td>
              <td>
                <span :style="{ color: r.type === 'in' ? 'green' : 'orange', fontWeight: 'bold' }">
                  {{ r.type === 'in' ? '入库' : '出库' }}
                </span>
              </td>
              <td>{{ r.quantity }}</td>
              <td>{{ r.remark }}</td>
            </tr>
            <tr v-if="records.length === 0">
              <td colspan="7" style="text-align: center; color: #999;">暂无数据</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchWarehouses } from '../api/warehouse'
import { fetchItems } from '../api/items'
import { fetchInventoryRecords, createInventoryRecord } from '../api/inventory'

const warehouses = ref([])
const items = ref([])
const records = ref([])

const form = ref({
  warehouse_id: '',
  item_id: '',
  type: 'in',
  quantity: 0,
  remark: '',
})

const loadBaseData = async () => {
  const wRes = await fetchWarehouses()
  warehouses.value = wRes.data || []

  const iRes = await fetchItems()
  items.value = iRes.data || []
}

const loadRecords = async () => {
  const rRes = await fetchInventoryRecords()
  records.value = rRes.data || []
}

const handleCreate = async () => {
  if (!form.value.warehouse_id || !form.value.item_id) {
    alert('仓库 和 商品 必须选择')
    return
  }
  if (!form.value.quantity || form.value.quantity <= 0) {
    alert('数量必须大于 0')
    return
  }

  await createInventoryRecord(form.value)
  // 重置部分字段
  form.value.quantity = 0
  form.value.remark = ''

  await loadRecords()
}

onMounted(async () => {
  await loadBaseData()
  await loadRecords()
})
</script>
