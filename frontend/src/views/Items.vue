<template>
  <div>
    <div class="flex justify-between items-center mb-4">
      <h2>{{ $t('items.title') }}</h2>
    </div>

    <div class="card">
      <h3>{{ $t('items.addItem') }}</h3>
      <form @submit.prevent="handleCreate" class="flex gap-4 items-end">
        <div style="flex: 1;">
          <label>{{ $t('items.sku') }}</label>
          <input v-model="form.sku" :placeholder="$t('items.skuPlaceholder')" />
        </div>
        <div style="flex: 1;">
          <label>{{ $t('items.name') }}</label>
          <input v-model="form.name" :placeholder="$t('items.namePlaceholder')" />
        </div>
        <div style="width: 120px;">
          <label>{{ $t('items.unit') }}</label>
          <input v-model="form.unit" :placeholder="$t('items.unitPlaceholder')" />
        </div>
        <button type="submit" style="height: 34px; padding: 0 20px; align-self: flex-end;">{{ $t('common.add') }}</button>
      </form>
    </div>

    <div class="card">
      <h3>{{ $t('items.itemList') }}</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>{{ $t('common.id') }}</th>
              <th>{{ $t('items.sku') }}</th>
              <th>{{ $t('common.name') }}</th>
              <th>{{ $t('items.unit') }}</th>
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
import { fetchItems, createItem } from '../api/items'
import { useI18n } from 'vue-i18n'

const { t } = useI18n()
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
    alert(t('items.error.skuAndNameRequired'))
    return
  }
  await createItem(form.value)
  form.value = { sku: '', name: '', unit: 'pcs' }
  await loadItems()
}

onMounted(loadItems)
</script>
