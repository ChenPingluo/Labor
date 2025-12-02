from flask import request, jsonify
from . import api_v1
from ..models.item import Item
from ..extensions import db

@api_v1.route('/items', methods=['GET'])
def list_items():
    items = Item.query.all()
    data = [
        {"id": i.id, "sku": i.sku, "name": i.name, "unit": i.unit}
        for i in items
    ]
    return jsonify({"data": data, "error": None})

@api_v1.route("/items", methods=['POST'])
def create_item():
    payload = request.get_json() or {}
    sku = payload.get("sku")
    name = payload.get("name")
    if not sku or not name:
        return jsonify({
            "data": None,
            "error": {"code": "INVALID_INPUT", "message": "sku和name必填"}
        }), 400
    item = Item(sku=sku, name=name, unit=payload.get("unit", "pcs"))
    db.session.add(item)
    db.seaasion.commit()
    return jsonify({"data": {"id": item.id}, "error": None}), 201