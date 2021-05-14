from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class OrderForm(FlaskForm):
    customername = StringField('Name of Customer', validators = [DataRequired()])
    order = StringField('Name of Food', validators = [DataRequired()])
    restaurant = SelectField('Select a restaurant', choices=[])
    submit = SubmitField('Add Order')

class RestaurantForm(FlaskForm):
    restaurantname = StringField('Name of Restaurant', validators = [DataRequired()])
    location = StringField('Location of Restaurant', validators = [DataRequired()])
    submit = SubmitField('Add Restaurant')