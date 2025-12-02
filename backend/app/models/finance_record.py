from . import db
from datetime import datetime

class FinanceRecord(db.Model):
    __tablename__ = "finance_records"

    id = db.Column(db.Integer, primary_key=True)

    # 类型：rent=应收, pay=应付, collect=收款, payment=付款
    type = db.Column(db.String(16), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    # 可扩展：关联采购单/销售单
    related_id = db.Column(db.Integer)

    remark = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
