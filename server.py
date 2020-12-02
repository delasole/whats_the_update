from flask import Flask, render_template, jsonify, request, redirect,session, flash
from models import connect_to_db, Order, Message, User,db
import sendsms
import os
import crud
import time


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

@app.route("/")
def go_homepage():
  return render_template("index.html")

@app.route("/join")
def go_join():

  return render_template("registration.html")

@app.route("/login")
def go_login():
  return render_template("login.html")

@app.route("/about")
def about_me():
  return render_template("about.html")


### Registration and Authentication##

@app.route("/join", methods=["POST"])
def process_reg():
    """Adds user to our database"""

    current_username = request.form.get('username')
    current_password = request.form.get('password')
    current_firstname = request.form.get('name')

    # Check for user username in db
    sign_up_username = User.query.filter(User.username == current_username).first()

    if not sign_up_username:
        user = User(username=current_username,
                 user_password=current_password,
                 user_first_name=current_firstname)

        db.session.add(user)
        db.session.commit()
    else:
        flash('Uh oh! Either your username or password is incorrect. Please try again.')

    time.sleep(3)
    return redirect("/")

@app.route("/login", methods=["POST"])
def login_user():
    """After logging in we want to personalize our website for the user."""

    current_username = request.form.get('username')
    current_password = request.form.get('password')

    user = User.query.filter(User.username == current_username).first()


    if user:
        if user.user_password == current_password:
            # add user info to our session
            session['user_id'] = user.id
            session['name'] = user.user_first_name
            time.sleep(3)
            return redirect("/orders")
        else:
            flash('Uh oh! Either your username or password is incorrect. Please try again.')
    else:
        flash('Uh oh! Either your username or password is incorrect. Please try again.')

    return redirect("/login")

@app.route("/resetpassword", methods=['GET'])
def load_page():
  return render_template("reset_password.html")

@app.route("/resetpassword", methods=['POST'])
def reset_password():
  """Handles password reset for the users"""

  username = request.form.get('username')
  password = request.form.get('password')

  user = User.query.filter(User.username == username).first()

  if user:
      user.user_password = password
      db.session.commit()
      
      flash('Your password has been updated. Please login.')
      time.sleep(3)
  return redirect("/login")


@app.route("/logout")
def log_out():
    """Logs user out of session."""

    session.clear()

    time.sleep(2)
    return redirect("/")


### Returning Order Information###
@app.route("/orders")
def load_orders():
  return render_template("order.html")

@app.route("/api/orders.json")
def get_orders():

  user = session['user_id']
  orders = Order.query.filter(Order.user_id==user).all()
  order_list = []

  for order in orders:
    order_list.append({"order_id":order.order_id, "phone":order.phone, "first_name": order.first_name, "last_name": order.last_name, "order_date": order.order_date, "item":order.item})

  return jsonify({"orders": order_list})


@app.route("/messagecenter/<order_id>")
def get_details(order_id):

  order = crud.get_order_by_id(order_id)
  return render_template("message_center.html",order=order)

@app.route("/history/<order_id>")
def get_history(order_id):

  msg_history = crud.get_messages_by_id(order_id)
  return render_template("message_history.html",msg_history=msg_history)

### Sending a Text Message ####
@app.route("/sendmessage/")
def send_msg():

  order_id = request.args.get('order')
  message = request.args.get('message')
  to = request.args.get('phone')

  messages = sendsms.send_message(order_id=order_id,to=to, message=message)


  flash('Your message has been sent.')
  time.sleep(2)
  return redirect("/orders")


if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')