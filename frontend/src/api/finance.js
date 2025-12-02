import http from './http'

export function createFinanceRecord(payload) {
  return http.post('/finance_records', payload)
}

export function fetchFinanceRecords(params = {}) {
  return http.get('/finance_records', { params })
}
