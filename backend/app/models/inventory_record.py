from . import db
from datetime import datetime

class InventoryRecord(db.Model):
    __tablename__ = "inventory_records"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey('warehouses.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(32), nullable=False)
    remarks = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    item = db.relationship('Item', backref="inventory_records")
    warehouse = db.relationship('Warehouse', backref="inventory_records")