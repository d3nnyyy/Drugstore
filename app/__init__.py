from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.controllers import drug_controller, manufacturer_controller, order_controller, category_controller, \
    address_controller, review_controller, customer_controller
