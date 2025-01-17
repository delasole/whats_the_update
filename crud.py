from models import db, Order, Message, connect_to_db
from datetime import date
from sqlalchemy import desc

def store_message(order_id, message, message_sid):
    
    sent_message = Message(order_id = order_id, message=message, message_sid=message_sid)
    
    db.session.add(sent_message)
    db.session.commit()

    return sent_message

def message_history(message_date, message_sid,message_status):
    return []

def create_order(order_id, phone, first_name, last_name, order_date, item):
    
    order = Order(order_id=order_id, phone=phone, first_name=first_name, last_name=last_name, order_date=order_date, item=item)

    db.session.add(order)
    db.session.commit()

    return order

def get_orders():
    return Order.query.all()

def get_messages():
    return Message.query.all()

def get_messages_by_id(order_id):
    return Message.query.filter(Message.order_id == order_id).order_by(desc(Message.message_date)).all()

def get_order_by_id(order_id):
    return Order.query.filter(Order.order_id == order_id).all()

def create_user(username, user_password, user_first_name):
    
    user = User(username=username, user_password=user_password, user_first_name=user_first_name)

    db.session.add(user)
    db.session.commit()

    return user

def find_user_id(username):
    return User.query.filter(User.username == username).first()

    
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print("Connected to db")