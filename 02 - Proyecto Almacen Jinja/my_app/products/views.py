from flask import Blueprint, render_template, request, redirect, url_for, flash, get_flashed_messages
from sqlalchemy.sql.expression import not_, or_

from my_app.products.model.products import PRODUCTS
from my_app.products.model.products_database import ProductDatabase
from my_app.products.model.products_database import ProductForm
from my_app import data_base

products = Blueprint('products', __name__)


@products.route('/')
def index():
    return render_template('products/index.html')


@products.route('/products')
@products.route('/products/<int:page>')
def products_list(page=1):
    products = ProductDatabase.query.paginate(page=page,per_page=5)
    return render_template('products/products_list.html', products=products)


@products.route('/product/<int:product_id>')
def product_by_id(product_id):
    product_details = ProductDatabase.query.get_or_404(product_id)
    return render_template('products/product_details.html', product_details=product_details)


@products.route('/filter/<int:product_id>')
def filter(product_id):
    product_details = PRODUCTS.get(product_id)
    return render_template('products/filter.html', product_details=product_details, products=PRODUCTS)


@products.route('/create-product', methods=['GET', 'POST'])
def create_product():
    product_form = ProductForm(meta={'csrf':False})
    if product_form.validate_on_submit():
        create_product = ProductDatabase(request.form['product_name'], request.form['product_price'])
        data_base.session.add(create_product)
        data_base.session.commit()
        flash('Producto Creado con Exito!')
        return redirect(url_for('products.create_product'))
    
    if product_form.errors:
        flash(product_form.errors, 'danger')
    return render_template('products/create_product.html', product_form=product_form)


@products.route('/update-product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    product_form = ProductForm(meta={'csrf':False})
    product_update = ProductDatabase.query.get_or_404(product_id)
    if request.method == 'GET':
        product_form.product_name.data = product_update.product_name
        product_form.product_price.data = product_update.product_price

    if product_form.validate_on_submit():
        product_update.product_name = product_form.product_name.data
        product_update.product_price = product_form.product_price.data
        data_base.session.add(product_update)
        data_base.session.commit()
        flash('Producto Actualizado con Exito!')
        return redirect(url_for('products.update_product', product_id=product_update.product_id))
    
    if product_form.errors:
        flash(product_form.errors, 'danger')
    return render_template('products/update_product.html', product_update=product_update, product_form=product_form)


@products.route('/delete-product/<int:product_id>')
def delete_product(product_id):
    delete_product = ProductDatabase.query.get_or_404(product_id)
    data_base.session.delete(delete_product)
    data_base.session.commit()
    return redirect(url_for('products.products_list'))

@products.route('/test')
def test():
    # ALL, FIRST son imporantes, muchos no funcinan si no indicamos cuantos registros queremos.
    print(f'Consultar todos: {ProductDatabase.query.all()}')
    print(f'Consultar con limite 2: {ProductDatabase.query.limit(2).all()}')
    print(f'Consultar el primer elemento: {ProductDatabase.query.limit(2).first()}')
    print(f'Consultar por orden: {ProductDatabase.query.order_by(ProductDatabase.product_id).limit(2).all()}')
    print(
        f'Consultar por orden desendente: {ProductDatabase.query.order_by(ProductDatabase.product_id.desc()).limit(2).all()}')
    # Hay que indicar cuantos queremos, el primero, todo, etc.
    print(f'Consultar por alguna columna: {ProductDatabase.query.filter_by(product_name="Pixel").all()}')
    print(f'Consultar por varias columnas: {ProductDatabase.query.filter_by(product_name="Pixel", product_id=3).all()}')
    print(
        f'Consultar todos los mayores a una columna: {ProductDatabase.query.filter(ProductDatabase.product_id > 1).all()}')
    print(f'Consultar con Like: {ProductDatabase.query.filter(ProductDatabase.product_name.like("P%")).all()}')
    print(f'Consultar con not: {ProductDatabase.query.filter(not_(ProductDatabase.product_id > 1)).all()}') # type: ignore
    print(
        f'Consultar con or: {ProductDatabase.query.filter(or_(ProductDatabase.product_id > 1, ProductDatabase.product_name == "Pixel")).all()}')

    # create_product = ProductDatabase('iPad', 3999.99)
    # data_base.session.add(create_product)
    # Commit es importante porque sino no se guardan los cambios en la BD
    # data_base.session.commit()

    # update_product = ProductDatabase.query.filter_by(product_name = "Mx Master 1", product_id = 4).first()
    # update_product.product_name = "Mx Master 3 Pro Max"
    # data_base.session.add(update_product)
    # Commit es importante porque sino no se guardan los cambios en la BD
    # data_base.session.commit()

    delete_product = ProductDatabase.query.filter_by(product_id=5).first()
    data_base.session.delete(delete_product)
    data_base.session.commit()
    return 'Flask'


# Filtro
@products.app_template_filter('iva')
def iva_filter(product):
    if product['price']:
        return product['price'] * 0.20 + product['price']
    return 'Sin precio'
