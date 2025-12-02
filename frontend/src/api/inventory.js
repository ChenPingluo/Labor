import http from './http'

export function fetchInventoryRecords(params = {}) {
  return http.get('/inventory_records', { params })
}

export function createInventoryRecord(payload) {
  return http.post('/inventory_records', payload)
}
