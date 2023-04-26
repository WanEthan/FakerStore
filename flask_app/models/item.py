from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re
# the regex module
# create a regular expression object that we'll use later

DATABASE = 'ecommerce'

class Item:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.digital = data['digital']
        self.image = data['image']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']