from flask import Flask
from my_app.module1.views import module_1


app = Flask(__name__)
app.register_blueprint(module_1)
