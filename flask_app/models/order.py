from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash
from flask_app.models.item import Item
import re
from pprint import pprint

DATABASE = 'ecommerce'

class Order:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.user_id = data['user_id']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.order_items = []

    
    @property
    def get_cart_total(self):
        order_items = self.order_items
        total = sum([item.get_total for item in order_items])
        return total
    
    @property
    def get_cart_items(self):
        order_items = self.order_items
        total = sum([item.quanitity for item in order_items])
        return total


# ***------------------------Save order to Database--------------------------***

    @classmethod
    def add(cls, data):
        query = "INSERT INTO orders (user_id, status) VALUES (%(user_id)s, %(status)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    

    @classmethod
    def get_process_order(cls, data):
        query = "SELECT id FROM orders WHERE status = 'process';"
        result = connectToMySQL(DATABASE).query_db(query, data)
        # Didn't find an order in process
        if not result:
            return False
        return result[0]['id']
    
    # ***------------------------ADD items to orders_items table --------------------------***
    @classmethod
    def order_add_items(cls, data):
        query = "INSERT INTO orders_items (order_id, item_id) VALUES (%(order_id)s, %(item_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    # ***------------------------Get ALL items BY order id --------------------------***
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM orders LEFT JOIN orders_items ON orders.id = orders_items.order_id LEFT JOIN items ON items.id = orders_items.item_id WHERE orders.id = %(order_id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        # Creates instance of author object from row one
        order = Order(results[0])
        # append all item objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['items.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['items.id'],
                "name": row['name'],
                "price": row['price'],
                "image": row['image'], 
                "quanitity": row['quanitity'],
                "description": row['description'], 
                "created_at": row['items.created_at'],
                "updated_at": row['items.updated_at']
            }
            order.order_items.append(Item(data))
        return order
    

        #! DELETE

    @classmethod
    def delete_order(cls, id):
        query = "DELETE FROM orders WHERE id=%(id)s;"
        data = {'id': id}
        return connectToMySQL(DATABASE).query_db(query, data)