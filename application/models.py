from application import db
from datetime import datetime

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(50), nullable=False)
    order = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default =datetime.utcnow)

    