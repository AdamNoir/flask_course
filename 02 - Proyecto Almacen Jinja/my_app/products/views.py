from flask import Blueprint, render_template, abort

from my_app.products.model.products import PRODUCTS

products = Blueprint('products', __name__)


@products.route('/')
def index():
    return render_template('products/index.html')


@products.route('/products')
def products_list():
    return render_template('products/products_list.html', products=PRODUCTS)


@products.route('/home')
@products.route('/product/<int:product_id>')
def product_by_id(product_id):
    product_details = PRODUCTS.get(product_id)
    if not product_details:
        abort(404)
    return render_template('products/product_details.html', product_details=product_details)


@products.route('/filter/<int:product_id>')
def filter(product_id):
    product_details = PRODUCTS.get(product_id)
    return render_template('products/filter.html', product_details=product_details, products=PRODUCTS)

# Filtro
@products.app_template_filter('iva')
def iva_filter(product):
    if product['price']:
        return product['price'] * 0.20 + product['price']
    return 'Sin precio'