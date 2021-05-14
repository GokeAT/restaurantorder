from application import app, db
from application.models import Orders, Restaurants
from application.forms import OrderForm, RestaurantForm
from flask import render_template, request, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    all_orders = Orders.query.all()
    all_restaurants = Restaurants.query.all()
    return render_template("index.html", title="Home", all_orders=all_orders, all_restaurants=all_restaurants)


@app.route("/create", methods = ["GET", "POST"])
def create():
    form = OrderForm()
    form.restaurant.choices = [(restaurant.id, restaurant.restaurantname) for restaurant in Restaurants.query.all()]
    if request.method == "POST":
        if form.validate_on_submit():
            new_order = Orders(order=form.order.data,customername=form.customername.data,restaurantid=form.restaurant.data)
            db.session.add(new_order)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("add.html", title="Create an Order", form=form)


@app.route("/update/<int:id>", methods = ["GET", "POST"])
def update(id):
    form = OrderForm()
    order = Orders.query.filter_by(id=id).first()
    if request.method == "POST":
        order.customername = form.customername.data
        order.order = form.order.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Order", order=order)

@app.route("/delete/<int:id>")
def delete(id):
    order = Orders.query.filter_by(id=id).first()
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/createrestaurant", methods = ["GET", "POST"])
def createrestaurant():
    form = RestaurantForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_restaurant = Restaurants(restaurantname=form.restaurantname.data,location=form.location.data)
            db.session.add(new_restaurant)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template("addrestaurant.html", title="Create a restaurant", form=form)
