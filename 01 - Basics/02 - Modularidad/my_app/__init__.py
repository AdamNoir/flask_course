from flask import Flask

app = Flask(__name__)

import my_app.module1.views
import my_app.module2.views
