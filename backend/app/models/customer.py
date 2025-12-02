from . import db
from datetime import datetime

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    contact = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
