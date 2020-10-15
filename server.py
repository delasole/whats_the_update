from flask import Flask, render_template, jsonify, request, redirect
from models import connect_to_db
import crud

app = Flask(__name__)

@app.route("/")
def redirect_homepage():
  return redirect("/home")

@app.route("/home")
def load_homepage():
  return render_template("index.html")

@app.route("/upload", methods=['POST'])
def file_upload():
  return render_template("upload_data.html")



if __name__ == "__main__":
  connect_to_db(app)
  app.run(debug=True, host='0.0.0.0')