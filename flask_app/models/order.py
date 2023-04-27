from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re

DATABASE = 'ecommerce'

class Order:
    def __init__(self, data) -> None:
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']