from . import db
from datetime import datetime

class Warehouse(db.Model):
    __tablename__ = "warehouses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    location = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)