from flask_app.config.mysqlconnection import connectToMySQL
import requests
from flask_app import flash
from pprint import pprint
import re

DATABASE = 'ecommerce'

class Item:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.price = data['price']
        self.image = data['image']
        self.quanitity = 1
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


# ***------------------------Save item to Database--------------------------***

    @classmethod
    def save(cls, data):
        query = "INSERT INTO items (name, price, image, description, quanitity) VALUES (%(name)s, %(price)s, %(image)s, %(description)s, %(quanitity)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
# ***------------------------Read all items from Database--------------------------***
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM items;"
        results = connectToMySQL(DATABASE).query_db(query)
        items = []
        for item_dict in results:
            items.append(Item(item_dict))
        return items
    
    # ***------------------------Read ONE ITEM from Database--------------------------***
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM items WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @property
    def get_total(self):
        total = self.price * self.quanitity
        return total