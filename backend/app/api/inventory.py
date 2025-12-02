from flask import request, jsonify
from . import api_v1
from ..extensions import db
from ..models.warehouse import Warehouse
from ..models.inventory_record import InventoryRecord
from ..models.item import Item

@api_v1.route('/warehouses', methods=['GET'])
def list_warehouses():
    warehouses = Warehouse.query.all()
    data = [
        {"id": w.id, "name": w.name, "location": w.location}
        for w in warehouses
    ]
    return jsonify({"data": data, "error": None})

@api_v1.route('/warehouses', methods=['POST'])
def create_warehouse():
    payload = request.get_json() or {}
    name = payload.get("name")
    if not name:
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "name必填"}
        }), 400
    warehouse = Warehouse(name=name, location=payload.get("location", ""))
    db.session.add(warehouse)
    db.session.commit()
    return jsonify({"data": {"id": warehouse.id}, "error": None}), 201

@api_v1.route('/inventory_records', methods=['POST'])
def create_inventory_record():
    payload = request.get_json() or {}
    item_id = payload.get("item_id")
    warehouse_id = payload.get("warehouse_id")
    quantity = payload.get("quantity")
    record_type = payload.get("type")
    remarks = payload.get("remarks")

    if not all([item_id, warehouse_id, quantity, record_type]):
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "item_id, warehouse_id, quantity和type必填"}
        }), 400
    
    if record_type not in ['in', 'out']:
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "type必须是'in'或'out'"}
        }), 400
    
    item = Item.query.get(item_id)
    warehouse = Warehouse.query.get(warehouse_id)
    if not item or not warehouse:
        return jsonify({
            "data": None,
            "error": {"code": "NOT_FOUND", "message": "item或warehouse不存在"}
        }), 404
    
    try:
        quantity_value = float(quantity)
    except ValueError:
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "quantity必须是数字"}
        }), 400
    
    if quantity_value <= 0:
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "quantity必须大于0"}
        }), 400
    
    record = InventoryRecord(
        item_id=item_id,
        warehouse_id=warehouse_id,
        quantity=quantity_value,
        type=record_type,
        remarks=remarks
    )
    db.session.add(record)
    db.session.commit()
    return jsonify({"data": {"id": record.id}, "error": None}), 201

@api_v1.route('/inventory_records', methods=['GET'])
def list_inventory_records():
    query = InventoryRecord.query
    item_id = request.args.get('item_id')
    warehouse_id = request.args.get('warehouse_id')
    record_type = request.args.get('type')

    if item_id:
        query = query.filter_by(item_id=item_id)
    if warehouse_id:
        query = query.filter_by(warehouse_id=warehouse_id)
    if record_type:
        query = query.filter_by(type=record_type)
    
    records = query.order_by(InventoryRecord.created_at.desc()).all()
    data = [
        {
            "id": r.id,
            "item_id": r.item_id,
            "item_sku": r.item.sku,
            "item_name": r.item.name,
            "warehouse_id": r.warehouse_id,
            "warehouse_name": r.warehouse.name,
            "quantity": r.quantity,
            "type": r.type,
            "remark": r.remark,
            "created_at": r.created_at.isoformat()
        }
        for r in records
    ]
    return jsonify({"data": data, "error": None})
