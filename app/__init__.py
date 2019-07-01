from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

from .views import debug_view
from .views import show_view
from .views import flow_view

