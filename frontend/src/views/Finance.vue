<template>
  <div>
    <h2>财务管理</h2>

    <div class="card">
      <h3>新增财务记录</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="width: 150px;">
          <label>类型</label>
          <select v-model="form.type">
            <option value="rent">应收</option>
            <option value="pay">应付</option>
            <option value="collect">收款</option>
            <option value="payment">付款</option>
          </select>
        </div>

        <div style="width: 150px;">
          <label>金额</label>
          <input v-model.number="form.amount" type="number" placeholder="0.00" />
        </div>

        <div style="flex: 1;">
          <label>备注</label>
          <input v-model="form.remark" placeholder="说明..." />
        </div>

        <button type="submit">新增</button>
      </form>
    </div>

    <div class="card">
      <h3>财务记录列表</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>类型</th>
              <th>金额</th>
              <th>备注</th>
              <th>时间</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="r in records" :key="r.id">
              <td>{{ r.id }}</td>
              <td>
                <span :class="'badge-' + r.type">{{ typeLabel(r.type) }}</span>
              </td>
              <td style="font-family: monospace;">{{ r.amount }}</td>
              <td>{{ r.remark }}</td>
              <td>{{ r.created_at }}</td>
            </tr>
            <tr v-if="records.length === 0">
              <td colspan="5" style="text-align: center; color: #999;">暂无数据</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { createFinanceRecord, fetchFinanceRecords } from '../api/finance'

const records = ref([])

const form = ref({
  type: 'rent',
  amount: '',
  remark: ''
})

const loadRecords = async () => {
  const res = await fetchFinanceRecords()
  records.value = res.data || []
}

const handleCreate = async () => {
  await createFinanceRecord(form.value)
  form.value.amount = ''
  form.value.remark = ''
  await loadRecords()
}

const typeLabel = (t) => {
  return {
    rent: '应收',
    pay: '应付',
    collect: '收款',
    payment: '付款'
  }[t]
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
