from flask import request, jsonify
from . import api_v1
from ..models.inventory_record import InventoryRecord
from ..models.item import Item
from ..models.warehouse import Warehouse
from sqlalchemy import func, case

@api_v1.route("/stock", methods=["GET"])
def get_stock_summary():
    item_id = request.args.get("item_id")
    warehouse_id = request.args.get("warehouse_id")

    query = (
        InventoryRecord.query
        .join(Item, InventoryRecord.item_id == Item.id)
        .join(Warehouse, InventoryRecord.warehouse_id == Warehouse.id)
        .with_entities(
            Item.id.label("item_id"),
            Item.sku.label("item_sku"),
            Item.name.label("item_name"),
            Warehouse.id.label("warehouse_id"),
            Warehouse.name.label("warehouse_name"),
            func.sum(
                case(
                    (InventoryRecord.type == "in", InventoryRecord.quantity),
                    else_=-InventoryRecord.quantity
                )
            ).label("stock")
        )
        .group_by(Item.id, Warehouse.id)
    )

    if item_id:
        query = query.filter(InventoryRecord.item_id == item_id)
    if warehouse_id:
        query = query.filter(InventoryRecord.warehouse_id == warehouse_id)

    rows = query.all()

    data = [
        {
            "item_id": r.item_id,
            "item_sku": r.item_sku,
            "item_name": r.item_name,
            "warehouse_id": r.warehouse_id,
            "warehouse_name": r.warehouse_name,
            "stock": r.stock or 0,
        }
        for r in rows
    ]

    return jsonify({"data": data, "error": None})
