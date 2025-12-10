<template>
  <div>
    <h2>{{ $t('inventory.title') }}</h2>

    <div class="card">
      <h3>{{ $t('inventory.addRecord') }}</h3>
      <form @submit.prevent="handleCreate">
        <div class="flex gap-4 mb-4">
          <div style="flex: 1;">
            <label>{{ $t('common.warehouse') }}</label>
            <select v-model="form.warehouse_id">
              <option value="">{{ $t('inventory.selectWarehouse') }}</option>
              <option v-for="w in warehouses" :key="w.id" :value="w.id">
                {{ w.name }}
              </option>
            </select>
          </div>
          <div style="flex: 1;">
            <label>{{ $t('common.item') }}</label>
            <select v-model="form.item_id">
              <option value="">{{ $t('inventory.selectItem') }}</option>
              <option v-for="item in items" :key="item.id" :value="item.id">
                {{ item.sku }} - {{ item.name }}
              </option>
            </select>
          </div>
          <div style="width: 120px;">
            <label>{{ $t('common.type') }}</label>
            <select v-model="form.type">
              <option value="in">{{ $t('inventory.type.in') }}</option>
              <option value="out">{{ $t('inventory.type.out') }}</option>
            </select>
          </div>
        </div>

        <div class="flex gap-4 items-end">
          <div style="flex: 1;">
            <label>{{ $t('common.quantity') }}</label>
            <input v-model.number="form.quantity" type="number" min="0.01" step="0.01" placeholder="0.00" />
          </div>
          <div style="flex: 2;">
            <label>{{ $t('common.remark') }}</label>
            <input v-model="form.remark" type="text" :placeholder="$t('common.optionalRemark')" />
          </div>
          <button type="submit" style="height: 34px; padding: 0 20px; align-self: flex-end;">{{ $t('common.saveRecord') }}</button>
        </div>
      </form>
    </div>

    <div class="card">
      <h3>{{ $t('inventory.recordList') }}</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>{{ $t('common.id') }}</th>
              <th>{{ $t('common.time') }}</th>
              <th>{{ $t('common.warehouse') }}</th>
              <th>{{ $t('common.item') }}</th>
              <th>{{ $t('common.type') }}</th>
              <th>{{ $t('common.quantity') }}</th>
              <th>{{ $t('common.remark') }}</th>
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
                  {{ $t('inventory.type.' + r.type) }}
                </span>
              </td>
              <td>{{ r.quantity }}</td>
              <td>{{ r.remark }}</td>
            </tr>
            <tr v-if="records.length === 0">
              <td colspan="7" style="text-align: center; color: #999;">{{ $t('common.noData') }}</td>
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
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
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
    alert(t('inventory.error.warehouseAndItemRequired'))
    return
  }
  if (!form.value.quantity || form.value.quantity <= 0) {
    alert(t('inventory.error.quantityMustBePositive'))
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
