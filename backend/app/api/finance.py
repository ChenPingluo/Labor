from flask import request, jsonify
from . import api_v1
from ..extensions import db
from ..models.finance_record import FinanceRecord
from flask_jwt_extended import jwt_required


@api_v1.route("/finance_records", methods=["POST"])
@jwt_required()
def create_finance_record():
    payload = request.get_json() or {}

    record_type = payload.get("type")
    amount = payload.get("amount")
    remark = payload.get("remark")
    related_id = payload.get("related_id")

    if record_type not in ("rent", "pay", "collect", "payment"):
        return jsonify({"error": "无效类型", "data": None}), 400

    if not amount or amount <= 0:
        return jsonify({"error": "金额必须大于 0", "data": None}), 400

    record = FinanceRecord(
        type=record_type,
        amount=amount,
        remark=remark,
        related_id=related_id
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({"data": {"id": record.id}, "error": None})


@api_v1.route("/finance_records", methods=["GET"])
@jwt_required()
def list_finance_records():
    record_type = request.args.get("type")

    query = FinanceRecord.query
    if record_type:
        query = query.filter_by(type=record_type)

    records = query.order_by(FinanceRecord.created_at.desc()).all()

    data = [
        {
            "id": r.id,
            "type": r.type,
            "amount": r.amount,
            "remark": r.remark,
            "related_id": r.related_id,
            "created_at": r.created_at.isoformat()
        }
        for r in records
    ]

    return jsonify({"data": data, "error": None})


@api_v1.route("/finance/inventory-value", methods=["GET"])
@jwt_required()
def get_inventory_value():
    try:
        from labor_core import calculate_total_value
    except ImportError:
        return jsonify({"error": "Rust module 'labor_core' not found. Please compile it first.", "data": None}), 500

    from ..models.inventory_record import InventoryRecord
    
    records = InventoryRecord.query.all()
    
    # Mock price logic: price = item_id * 10.0 + 5.0
    items_for_rust = []
    for r in records:
        items_for_rust.append(
            (float(r.item_id * 10.0 + 5.0), r.quantity)
        )
        
    try:
        total_value = calculate_total_value(items_for_rust)
    except Exception as e:
        return jsonify({"error": str(e), "data": None}), 500
        
    return jsonify({
        "data": {
            "total_value": total_value,
            "item_count": len(items_for_rust),
            "engine": "Rust"
        },
        "error": None
    })
