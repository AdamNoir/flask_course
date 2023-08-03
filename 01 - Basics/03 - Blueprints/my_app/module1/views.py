from flask import Blueprint


module_1 = Blueprint('module_1', __name__)


@module_1.route('/')
@module_1.route('/module-1')
def module_one():
    return 'Module 1'
