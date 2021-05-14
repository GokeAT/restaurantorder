from application import db
from datetime import datetime

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customername = db.Column(db.String(50), nullable=False)
    order = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default =datetime.utcnow)
    restaurantid = db.Column(db.Integer, db.ForeignKey("restaurants.id"))

class Restaurants(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    restaurantname = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    orders = db.relationship("Orders",backref="restaurant")

