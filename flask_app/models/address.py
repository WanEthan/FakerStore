from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re

DATABASE = 'ecommerce'


class Address:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.address = data['address']
        self.city = data['city']
        self.state = data['state']
        self.zipcode = data['zipcode']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.order_id = data['order_id']
