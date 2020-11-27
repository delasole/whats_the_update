from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import PasswordType, force_auto_coercion
from flask import Flask
from datetime import date, datetime
import os

db = SQLAlchemy()
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True, nullable = False, unique=True, autoincrement = True)
    username = db.Column(db.String(100), nullable = False)
    user_password=db.Column(PasswordType(onload=lambda **kwargs: dict(
                schemes=['pbkdf2_sha512','md5_crypt'],
                **kwargs)), unique=False, nullable=False)
    user_first_name = db.Column(db.String(100), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)

    def __repr__(self):
        return(f"< User ID = {self.id} Username = {self.username}> Name = {self.user_first_name}>")
class Order(db.Model):

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key = True, nullable = False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    phone = db.Column(db.String(15), nullable = False)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    order_date = db.Column(db.DateTime, nullable = False)
    item = db.Column(db.String(200), nullable = False)

    users = db.relationship('User', backref='orders')

    def __repr__(self):
        return(f"< Order ID = {self.order_id} First Name={self.first_name} Last Name={self.last_name}Item={self.item} Phone Number={self.phone} Order Date={self.order_date} User={self.user_id}>")

class Message(db.Model):

    __tablename__ = "message_history"

    message_id = db.Column(db.Integer, primary_key= True, autoincrement=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    phone = db.Column(db.String(15))
    message = db.Column(db.String(250))
    message_sid = db.Column(db.String(250))
    message_date = db.Column(db.String(100))

    orders = db.relationship('Order', backref='message_history')

    def __repr__(self):
        return(f"<Message ID = {self.message_id} Order ID = {self.order_id} Phone = {self.phone} Message={self.message} Message SID = {self.message_sid}>")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///messages'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    from server import app

    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    connect_to_db(app)
    print('Connected to db!')
