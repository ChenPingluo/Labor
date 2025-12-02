import http from './http'

export function fetchItems() {
    return http.get('/items');
}

export function createItem(payload) {
    return http.post('/items', payload);
}