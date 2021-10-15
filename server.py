from flask import Flask
from sakana_app import app
from sakana_app.controllers import users_controller, orders_controller

if __name__ == "__main__":
    app.run( debug = True )