from flask import flash, session
from sakana_app.config.MySQLConnection import connectToMySQL

class Order:
    def __init__(self, side_id, beverage_id, sushi_id):
        self.side_id = side_id
        self.beverage_id = beverage_id
        self.sushi_id = sushi_id

    @classmethod
    def add_new_order(cls, data):
        query = "INSERT INTO orders(side_id, beverage_id, sushi_id, user_id) VALUES(%(side_id)s,%(beverage_id)s,%(sushi_id)s, %(user_id)s);"
        data={
            "side_id": data[0],
            "beverage_id": data[1],
            "sushi_id":data[2],
            "user_id":data[3]
        }

        result = connectToMySQL("sakana_db").query_db(query, data)
        return result

    @classmethod
    def get_order_info(cls, user_id):
        query = "SELECT orders.id as order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price,beverages.id as beverage_id, beverages.name as beverage_name, beverages.price as beverage_price,sides.id as side_id, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name FROM orders JOIN sushi ON sushi.id = orders.sushi_id JOIN beverages ON beverages.id = orders.beverage_id JOIN sides ON sides.id = orders.side_id JOIN users ON users.id = orders.user_id WHERE users.id =%(user_id)s ORDER BY order_id DESC LIMIT 1;"
        data={
            "user_id": user_id
        }
        result = connectToMySQL("sakana_db").query_db(query, data)
        print(result)

        return result

    @classmethod
    def add_order_to_past_orders(cls, data):
        query = "INSERT INTO past_orders(user_id, sushi_id, beverage_id, side_id, favorite) VALUES(%(user_id)s,%(sushi_id)s,%(beverage_id)s,%(side_id)s,%(favorite)s);"
        data={
            "user_id": data['user_id'],
            "sushi_id": data['sushi_id'],
            "beverage_id": data['beverage_id'],
            "side_id": data['side_id'],
            "favorite": data['favorite']
        }

        result = connectToMySQL("sakana_db").query_db(query, data)

        print("Will delete")
        query2= "delete from orders WHERE user_id = %(user_id)s;"
        data2={
            "user_id": data['user_id']
        }

        result2=  connectToMySQL("sakana_db").query_db(query2, data2)
        return result, result2

    @classmethod
    def get_past_orders(cls, user):
        query = "SELECT DISTINCT past_orders.id as past_order_id, sushi.id as sushi_id, sushi.name as sushi_name, sushi.price as sushi_price, beverages.name as beverage_name, beverages.price as beverage_price, sides.name as side_name, sides.price as side_price, users.id as user_id, users.first_name as user_name FROM past_orders JOIN users ON past_orders.user_id = users.id  JOIN sushi ON past_orders.sushi_id = sushi.id JOIN beverages ON past_orders.beverage_id = beverages.id JOIN sides ON past_orders.side_id = sides.id WHERE users.id = %(user_id)s ORDER BY past_orders.id DESC LIMIT 3;"

        data ={
            "user_id": user['user']
        }

        result = connectToMySQL("sakana_db").query_db(query, data)
        print(result)
        return result

    @classmethod
    def update_favorite(cls, favorite):
        query = "UPDATE past_orders SET favorite = 1 WHERE id =%(favorite)s"
        data={
            "favorite": favorite
        }
        result = connectToMySQL("sakana_db").query_db(query, data)
        print(result)
        return result

    @classmethod
    def delete_order(cls, user_order_info):
        query = "delete from orders WHERE user_id = %(user_id)s;"
        data={
            "user_id": user_order_info['user_id']
        }
        print("Delete info:", user_order_info)
        result = connectToMySQL("sakana_db").query_db(query, data)
        return result