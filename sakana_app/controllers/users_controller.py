from flask import render_template, request, redirect, session, flash
from sakana_app import app
from sakana_app.models import User, Order
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route("/", methods=['GET'])
def load_main_page():
    return render_template("index.html")

@app.route("/create/account")
def load_signup_page():
    return render_template("signup.html")

@app.route("/signup", methods=['POST'])
def add_new_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zipcode = int(request.form['zipcode'])
    password = request.form['password']
    encrypted_password = bcrypt.generate_password_hash(password)
    password_confirmation = request.form['confirm_password']

    print(state)

    print("Information ok")

    if User.User.validate_registry(first_name, last_name, email, address, city, state, zipcode, encrypted_password, password, password_confirmation):
        print("Validation Ok")
        new_user = User.User(first_name, last_name, email, address, city, state, zipcode, encrypted_password)
        User.User.add_new_user(new_user)
        return redirect("/")
    else:
        print("something went wrong 1")
        return redirect("/")

@app.route("/update/<id>", methods=['POST'])
def update_user_info(id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    zipcode = int(request.form['zipcode'])
    password = request.form['password']
    encrypted_password = bcrypt.generate_password_hash(password)
    password_confirmation = request.form['confirm_password']
    if User.User.validate_update(first_name, last_name, email, address, city, state, zipcode, encrypted_password, password, password_confirmation):
        update_user = User.User(first_name, last_name, email, address, city, state, zipcode, encrypted_password)
        User.User.update(update_user, id)
        return redirect("/profile")
    else:
        print("something went wrong 2")
        return redirect("/home")

@app.route("/login", methods=['POST'])
def login_validation():
    email = request.form['email']
    password = request.form['password']

    result = User.User.validate_login(email)
    if result == ():
        flash("email not registered")
        return redirect("/")
    else:
        database_password = result[0]['password']
        if result[0]['email'] == email:

            if bcrypt.check_password_hash(database_password, password):
                session.clear()
                data={
                    'id':result[0]['id'],
                    'first_name': result[0]['first_name']
                }
                session['id'] = result[0]['id']
                print(session['id'])
                return redirect("/home")
            else:
                flash("Wrong password, try again")

    return redirect("/")


@app.route("/home", methods=['GET'])
def load_home_page():
    print(session)
    if 'id' not in session:
        return redirect('/')
    user_info = User.User.get_one(session['id'])
    user_id = session['id']
    order_info = Order.Order.get_order_info(user_id)
    print("This is the user info:",user_info)
    print("order info:", order_info)
    data = {
        "id": session['id'],
        "first_name": user_info[0]['first_name']
    }
    return render_template("home.html", data=data, order_info=order_info)


@app.route("/profile")
def load_profile():
    print("loading")
    if 'id' not in session:
        return redirect('/')
    else:
        user_info = User.User.get_one(session['id'])
        user_id = session['id']
        user = {
            "user": user_id
        }
        print("First print",user_id)
        print(user)
        past_orders = Order.Order.get_past_orders(user)
        print(past_orders)
        user_id = session['id']
        order_info = Order.Order.get_order_info(user_id)
        return render_template("profile.html", user_info=user_info, past_orders=past_orders, user_id=user_id, order_info=order_info)

@app.route("/menu")
def load_menu():
    if 'id' not in session:
        return redirect('/')
    
    user_info = User.User.get_one(session['id'])
    print("This is the user info:",user_info)
    data = {
        "id": session['id'],
        "first_name": user_info[0]['first_name']
    }
    user_id = session['id']
    order_info = Order.Order.get_order_info(user_id)
    return render_template("menu.html", data=data, order_info=order_info)

@app.route("/logout", methods=['GET'])
def logout_session():
    session.clear()
    return redirect("/")