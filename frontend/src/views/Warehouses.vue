<template>
  <div>
    <h2>{{ $t('warehouses.title') }}</h2>

    <div class="card">
      <h3>{{ $t('warehouses.addWarehouse') }}</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>{{ $t('warehouses.name') }}</label>
          <input v-model="form.name" :placeholder="$t('warehouses.namePlaceholder')" />
        </div>
        <div style="flex: 1;">
          <label>{{ $t('warehouses.location') }}</label>
          <input v-model="form.location" :placeholder="$t('warehouses.locationPlaceholder')" />
        </div>
        <button type="submit" style="height: 34px; padding: 0 20px; align-self: flex-end;">{{ $t('common.add') }}</button>
      </form>
    </div>

    <div class="card">
      <h3>{{ $t('warehouses.warehouseList') }}</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>{{ $t('common.id') }}</th>
              <th>{{ $t('common.name') }}</th>
              <th>{{ $t('warehouses.location') }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="w in warehouses" :key="w.id">
              <td>{{ w.id }}</td>
              <td>{{ w.name }}</td>
              <td>{{ w.location }}</td>
            </tr>
            <tr v-if="warehouses.length === 0">
              <td colspan="3" style="text-align: center; color: #999;">{{ $t('common.noData') }}</td>
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
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
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
    alert(t('warehouses.error.nameRequired'))
    return
  }
  await createWarehouse(form.value)
  form.value = { name: '', location: '' }
  await loadWarehouses()
}

onMounted(loadWarehouses)
</script>
