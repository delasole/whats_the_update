from flask import Flask, render_template, jsonify, request, redirect
from models import connect_to_db, Order, Message
import crud

app = Flask(__name__)

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
    order_list.append({"order_id":order.order_id, "phone":order.phone, "first name": order.first_name, "last name": order.last_name, "order date": order.order_date, "item":order.item})
    time.sleep(2)

    return jsonify({"orders": order_list})

@app.route("/upload", methods=['POST'])
def file_upload():
  return render_template("upload_data.html")



if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')