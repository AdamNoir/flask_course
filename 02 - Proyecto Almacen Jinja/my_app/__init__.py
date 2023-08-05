from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('configuration.DevelopmentConfig')

data_base = SQLAlchemy(app)

from my_app.products.views import products

app.register_blueprint(products)


@app.template_filter('mydouble')
def mydouble_filter(number: int):
    return number * 2


with app.app_context():
    data_base.create_all()
