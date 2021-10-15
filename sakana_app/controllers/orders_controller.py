from flask import render_template, request, redirect, session, flash
from sakana_app import app
from sakana_app.models import Order, User


sushi = 0
side = 0
beverage = 0
print (sushi,side,beverage)

@app.route("/add/product/sushi", methods=['POST'])
def get_sushi_id():
    sushi_id = int(request.form['sushi_id'])
    global sushi
    sushi = sushi_id
    print (sushi,side,beverage)

    if sushi_id ==1:
        flash("Rainbow roll successfully added to the order", "sushi")
    if sushi_id==2:
        flash("California roll successfully added to the order", "sushi")
    if sushi_id==3:
        flash("Salmon skin roll successfully added to the order", "sushi")

    return redirect("/menu")

@app.route("/add/product/beverage", methods=['POST'])
def get_beverage_id():
    beverage_id = int(request.form['beverage_id'])
    global beverage
    beverage = beverage_id
    print (sushi,side,beverage)

    if beverage_id ==1:
        flash("Beer successfully added to the order", "beverage")
    if beverage_id==2:
        flash("Soda successfully added to the order", "beverage")
    if beverage_id==3:
        flash("Water successfully added to the order", "beverage")

    return redirect("/menu")

@app.route("/add/product/side", methods=['POST'])
def get_side_id():
    side_id = int(request.form['side_id'])
    global side
    side = side_id
    print (sushi,side,beverage)

    if side_id ==1:
        flash("Miso soup successfully added to the order", "side")
    if side_id==2:
        flash("Edamame successfully added to the order", "side")

    return redirect("/menu")

@app.route("/cart")
def place_order():
    if 'id' not in session:
        return redirect('/')
    elif sushi==0 or beverage == 0 or side ==0:
        cart_empty = 0
        user_id = session['id']
        order_info = Order.Order.get_order_info(user_id)
        return render_template("cart.html", cart_empty = cart_empty, order_info=order_info)
    else:
        user_info = User.User.get_one(session['id'])
        print("This is the user info:",user_info)
        user_data = {
            "id": session['id'],
            "first_name": user_info[0]['first_name']
        }
        data=(side, beverage, sushi, session['id'])
        print("data info",data)
        user_id = session['id']
        Order.Order.add_new_order(data)
        order_info = Order.Order.get_order_info(user_id)
        print("order info",order_info)
        if order_info != ():
            total = order_info[0]['sushi_price'] + order_info[0]['beverage_price'] + order_info[0]['side_price']
        return render_template("cart.html", user_data = user_data, order_info = order_info, total = total)

@app.route("/purchase")
def add_order_to_past_purchases():
    if 'id' not in session:
        return redirect('/')
    else:
        user_info = User.User.get_one(session['id'])
        user_id = session['id']
        order_info = Order.Order.get_order_info(user_id)
        print(order_info)

        purchase ={
            "user_id": user_id,
            "sushi_id":order_info[0]['sushi_id'],
            "beverage_id": order_info[0]['beverage_id'],
            "side_id": order_info[0]['side_id'],
            "favorite": 0
        }

        user = {
            "user": user_id
        }

        Order.Order.add_order_to_past_orders(purchase)
        global sushi
        sushi = 0
        global beverage
        beverage = 0 
        global side
        side = 0
        return redirect("/profile")

@app.route("/add_favorite", methods=['POST'])
def update_favorite():
    if 'id' not in session:
        return redirect('/')
    else:
        favorite = int(request.form['order'])
        print("Favorite", favorite)
        Order.Order.update_favorite(favorite)
        return redirect("/home")


@app.route("/delete/order")
def delete_current_order():
    if 'id' not in session:
        return redirect('/')
    else:
        user_id = session['id']
        order_info = Order.Order.get_order_info(user_id)
        print("order info", order_info)
        user_order_info = {
            "user_id":int(order_info[0]['user_id'])
        }
        print("user_order info:", user_order_info)
        Order.Order.delete_order(user_order_info)
        global sushi
        sushi = 0
        global beverage
        beverage = 0 
        global side
        side = 0
        return redirect("/menu")
