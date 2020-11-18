from flask import Flask, render_template, jsonify, request, redirect, flash
from models import connect_to_db, Order, Message
import sendsms
import os
import crud
import time
UPLOAD_FOLDER = '/data'
ALLOWED_EXTENSIONS = {'xls','xlsx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = os.environ['SECRET_KEY']

@app.route("/")
def redirect_homepage():
  return redirect("/home")

@app.route("/home")
def load_homepage():
  return render_template("index.html")

@app.route("/api/orders.json")
def get_orders():
  orders = Order.query.all()
  order_list = []

  for order in orders:
    order_list.append({"order_id":order.order_id, "phone":order.phone, "first_name": order.first_name, "last_name": order.last_name, "order_date": order.order_date, "item":order.item})

  return jsonify({"orders": order_list})

@app.route("/upload")
def file_upload():
  return render_template("upload_data.html")


@app.route("/messagecenter/<order_id>")
def get_details(order_id):

  order = crud.get_order_by_id(order_id)
  return render_template("message_center.html",order=order)

@app.route("/sendmessage/")
def send_msg():

  order_id = request.args.get('order')
  message = request.args.get('message')
  to = request.args.get('phone')

  messages = sendsms.send_message(to=to, message=message)


  flash("Your message has been sent.")
  return redirect("/home")


if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')