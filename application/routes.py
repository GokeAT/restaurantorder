from application import app, db
from application.models import Orders

@app.route("/")
@app.route("/home")
def home():
    all_orders = Orders.query.all()
    output = ""
    for order in all_orders:
        output += order.order + "<br>"
    return output

@app.route("/create")
def create():
    new_order = Orders(order = "New Order", customername = "New Customer")
    db.session.add(new_order)
    db.session.commit()
    return "New Order added"

@app.route("/update/<new_order>")
def update(new_order):
    order = Orders.query.order_by(Orders.id.desc()).first()
    order.order = new_order
    db.session.commit()
    return f"Most recent Order updated with the order: {new_order}"

@app.route("/delete/<int:id>")
def delete(id):
    order = Orders.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    return f"Order {id} was deleted"