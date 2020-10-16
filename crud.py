from models import db, Order, Message, connect_to_db

def store_message(order_id, phone, message, message_sid):
    
    sent_message = Message(order_id = order_id, phone=phone,
                        message=message, message_sid=message_sid)
    
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
    return Message.query.get(order_id)

def get_order_by_id(order_id):
    return Order.query.filter(Order.order_id == order_id).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
    print("Connected to db")