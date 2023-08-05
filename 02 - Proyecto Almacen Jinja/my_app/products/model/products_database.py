from decimal import Decimal

from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from wtforms.validators import InputRequired, NumberRange

from my_app import data_base

class ProductDatabase(data_base.Model):
    __tablename__ = 'products'
    product_id = data_base.Column(data_base.Integer, primary_key=True)
    product_name = data_base.Column(data_base.String(255))
    product_price = data_base.Column(data_base.Float)

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

    def __repr__(self):
        return '<User %r>' % self.product_name

class ProductForm(FlaskForm):
    product_name = StringField('Producto', validators=[InputRequired()])
    product_price = DecimalField('Precio', validators=[InputRequired(), NumberRange(min=Decimal('0.0'))])