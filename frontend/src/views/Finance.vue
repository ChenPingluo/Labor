<template>
  <div>
    <h2>{{ $t('finance.title') }}</h2>

    <div class="card">
      <h3>{{ $t('finance.addRecord') }}</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="width: 150px;">
          <label>{{ $t('common.type') }}</label>
          <select v-model="form.type">
            <option value="rent">{{ $t('finance.type.rent') }}</option>
            <option value="pay">{{ $t('finance.type.pay') }}</option>
            <option value="collect">{{ $t('finance.type.collect') }}</option>
            <option value="payment">{{ $t('finance.type.payment') }}</option>
          </select>
        </div>

        <div style="width: 150px;">
          <label>{{ $t('common.amount') }}</label>
          <input v-model.number="form.amount" type="number" placeholder="0.00" />
        </div>

        <div style="flex: 1;">
          <label>{{ $t('common.remark') }}</label>
          <input v-model="form.remark" :placeholder="$t('common.remarkPlaceholder')" />
        </div>

        <button type="submit" style="height: 34px; padding: 0 20px; align-self: flex-end;">{{ $t('common.add') }}</button>
      </form>
    </div>

    <div class="card">
      <h3>{{ $t('finance.rustCalc') }}</h3>
      <div class="flex gap-4 items-center">
        <button @click="handleCalc" class="secondary">{{ $t('finance.calcButton') }}</button>
        <div v-if="calcResult" class="flex gap-4" style="background: #f0f9ff; padding: 8px 16px; border-radius: 4px; border: 1px solid #bae6fd;">
          <span><strong>{{ $t('finance.engine') }}:</strong> {{ calcResult.engine }}</span>
          <span><strong>{{ $t('finance.itemCount') }}:</strong> {{ calcResult.item_count }}</span>
          <span><strong>{{ $t('finance.totalValue') }}:</strong> {{ calcResult.total_value }}</span>
        </div>
      </div>
    </div>

    <div class="card">
      <h3>{{ $t('finance.recordList') }}</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>{{ $t('common.id') }}</th>
              <th>{{ $t('common.type') }}</th>
              <th>{{ $t('common.amount') }}</th>
              <th>{{ $t('common.remark') }}</th>
              <th>{{ $t('common.time') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in records" :key="r.id">
              <td>{{ r.id }}</td>
              <td>
                <span :class="'badge-' + r.type">{{ $t('finance.type.' + r.type) }}</span>
              </td>
              <td style="font-family: monospace;">{{ r.amount }}</td>
              <td>{{ r.remark }}</td>
              <td>{{ r.created_at }}</td>
            </tr>
            <tr v-if="records.length === 0">
              <td colspan="5" style="text-align: center; color: #999;">{{ $t('common.noData') }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { createFinanceRecord, fetchFinanceRecords, fetchInventoryValue } from '../api/finance'

const records = ref([])
const calcResult = ref(null)

const form = ref({
  type: 'rent',
  amount: '',
  remark: ''
})

const loadRecords = async () => {
  const res = await fetchFinanceRecords()
  records.value = res.data || []
}

const handleCalc = async () => {
  const res = await fetchInventoryValue()
  if (res.data) {
    calcResult.value = res.data
  } else {
    alert(res.error || 'Calculation failed')
  }
}

const handleCreate = async () => {
  await createFinanceRecord(form.value)
  form.value.amount = ''
  form.value.remark = ''
  await loadRecords()
}

onMounted(loadRecords)
</script>

<style scoped>
/* Simple badges for finance types */
.badge-rent { color: #2563eb; font-weight: bold; }
.badge-pay { color: #dc2626; font-weight: bold; }
.badge-collect { color: #059669; font-weight: bold; }
.badge-payment { color: #d97706; font-weight: bold; }
</style>
