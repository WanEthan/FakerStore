from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
import re

DATABASE = 'ecommerce'

class Item:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.digital = data['digital']
        self.image = data['image']
        self.quanitity = data['rating'][1]
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# ***------------------------Save item to Database--------------------------***

    @classmethod
    def save(cls, data):
        query = "INSERT INTO items (name, price, image, description) VALUES (%(name)s, %(price)s, %(image)s, %(description)s);"
        return connectToMySQL(DATABASE).query_db(query, data)