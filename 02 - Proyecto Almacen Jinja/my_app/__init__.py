from flask import Flask
from my_app.products.views import products


app = Flask(__name__)
app.register_blueprint(products)


@app.template_filter('mydouble')
def mydouble_filter(number:int):
    return number * 2