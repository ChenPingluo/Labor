import http from './http'

export function fetchStock(params = {}) {
  return http.get('/stock', { params })
}
