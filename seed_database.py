""" Script to seed the database """
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import models
import server

#Create Order

models.connect_to_db(server.app)

def add_orders():
    """ Adding orders to our orders database. Data is split by a semicolon"""

    for row in open("data/orders.txt"):
        row = row.rstrip()
        order_id, user_id, phone, first_name, last_name, order_date, item = row.split(";")

        order = models.Order(order_id=order_id,
                         user_id=user_id,
                         phone=phone,
                         first_name=first_name,
                         last_name=last_name,
                         order_date=order_date,
                         item=item)
    
        models.db.session.add(order)
    models.db.session.commit()

#Create User
def add_users():
    for row in open("data/users.txt"):
        row = row.rstrip()
        username,  user_password, user_first_name = row.split(";")

        user = models.User(username=username,
                       user_password=user_password,
                       user_first_name=user_first_name)
    
        models.db.session.add(user)
    models.db.session.commit()
#This will be the commands to connect to the db and
#add the new tables we created so far in the project"""



#models.db.create_all()