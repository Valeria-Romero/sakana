from flask import flash, session
from sakana_app.config.MySQLConnection import connectToMySQL
import re

class User:
    def __init__(self, first_name, last_name, email, address, city, state, zipcode, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.password = password

    @classmethod
    def add_new_user(cls, new_user):
        print(1)
        query = "INSERT INTO users(first_name, last_name, email, address, city, state, zipcode, password) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(address)s,%(city)s, %(state)s, %(zipcode)s,%(password)s);"
        data={
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "email": new_user.email,
            "address": new_user.address,
            "city": new_user.city,
            "state": new_user.state,
            "zipcode": new_user.zipcode,
            "password": new_user.password
        }

        result = connectToMySQL("sakana_db").query_db(query,data)
        return result

    @classmethod
    def update(cls, update_user, id):
        query="UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, address = %(address)s, city = %(city)s, state  = %(state)s, zipcode = %(zipcode)s, password = %(password)s WHERE id = %(id)s;"
        data={
            "first_name": update_user.first_name,
            "last_name": update_user.last_name,
            "email": update_user.email,
            "address": update_user.address,
            "city": update_user.city,
            "state": update_user.state,
            "zipcode": update_user.zipcode,
            "password": update_user.password,
            "id": id
        }

        result = connectToMySQL("sakana_db").query_db(query,data)
        return result

    @staticmethod
    def validate_registry( first_name, last_name, email, address, city, state, zipcode, encrypted_password, password, password_confirmation ):
        isValid = True
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        query = "SELECT email FROM users WHERE email = %(email)s;"
        email_data = {
                "email" : email,
            }
        results = connectToMySQL("sakana_db").query_db(query,email_data)

        print(len(results))

        if not EMAIL_REGEX.match(email):
            flash("Invalid email, please write email in valid format")
            isValid = False
            print("email regex")

        elif results != False and results != ():
            flash("Email already registered")
            isValid = False
            print("email")

        if len( first_name ) < 3:
            flash( "First name must be at least 3 characters long" )
            isValid = False 
            print("name")

        if len( last_name ) < 3:
            flash( "Last name must be at least 3 characters long")
            isValid = False
            print("name")

        if len(password) < 8:
            flash("Password must be at least 8 characters long")
            isValid = False
            print("password")

        if password != password_confirmation:
            flash("Passwords must match, try again")
            isValid = False
            print("pass confirmation")

        if len(address)<0:
            flash("Address can't be empty") 
            isValid = False
            print("address")

        if zipcode<9999:
            flash("Invalid zipcode")
            isValid = False
            print("zipcode")

        print("validation completed")

        return isValid

    @staticmethod
    def validate_update( first_name, last_name, email, address, city, state, zipcode, encrypted_password, password, password_confirmation ):
        isValid = True
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        query = "SELECT email FROM users WHERE email = %(email)s;"
        email_data = {
                "email" : email,
            }
        results = connectToMySQL("sakana_db").query_db(query,email_data)

        print(len(results))

        if not EMAIL_REGEX.match(email):
            flash("Invalid email, please write email in valid format")
            isValid = False
            print("email regex")

        if len( first_name ) < 3:
            flash( "First name must be at least 3 characters long" )
            isValid = False 
            print("name")

        if len( last_name ) < 3:
            flash( "Last name must be at least 3 characters long")
            isValid = False
            print("name")

        if len(password) < 8:
            flash("Password must be at least 8 characters long")
            isValid = False
            print("password")

        if password != password_confirmation:
            flash("Passwords must match, try again")
            isValid = False
            print("pass confirmation")

        if len(address)<0:
            flash("Address can't be empty") 
            isValid = False
            print("address")

        if zipcode<9999:
            flash("Invalid zipcode")
            isValid = False
            print("zipcode")

        print("validation completed 2")

        return isValid

    @classmethod
    def validate_login(cls, login_information):
        isValid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"

        email={
            "email": login_information
        }

        result = connectToMySQL("sakana_db").query_db(query,email)
        
        return result

    @classmethod
    def get_one(cls,data):
        query = "SELECT first_name FROM users WHERE id = %(id)s;"
        data = {
            "id": session['id'],
        }
        results = connectToMySQL("sakana_db").query_db(query,data)
        return results