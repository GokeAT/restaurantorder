import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Orders, Restaurants


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        test_restaurant= Restaurants(restaurantname="pizzahut", location="london")
        test_order = Orders(customername="Goke", order="spaghetti",restaurantid=1)
        db.session.add(test_restaurant)
        db.session.add(test_order)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_create_get(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 200)

    def test_createrestaurant_get(self):
        response = self.client.get(url_for('createrestaurant'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
     
class TestRead(TestBase):
    def test_read_orders(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"spaghetti", response.data)

class TestCreate(TestBase):
    def test_create_task(self):
        response = self.client.post(
            url_for("create"),
            data=dict(customername="Harry",order="wings", restaurant=1),
            follow_redirects=True
        )
        self.assertIn(b"wings", response.data)

    def test_createrestaurant_task(self):
        response = self.client.post(
            url_for("createrestaurant"),
            data=dict(restaurantname="pizzahut",location="london"),
            follow_redirects=True
        )
        self.assertIn(b"pizzahut", response.data)


class TestUpdate(TestBase):
    def test_create_task(self):
        response = self.client.post(
            url_for("update", id=1),
            data=dict(customername="John",order="pizza"),
            follow_redirects=True
        )
        self.assertIn(b"pizza", response.data)

class TestDelete(TestBase):
    def test_create_task(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"spaghetti", response.data)
