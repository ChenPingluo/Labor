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
