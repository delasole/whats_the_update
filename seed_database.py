""" Script to seed the database """
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import models
import server


#Creates the whole database for this project
os.system('dropdb messages')
os.system('createdb messages')

#This will be the commands to connect to the db and
#add the new tables we created so far in the project

models.connect_to_db(server.app)
models.db.create_all()