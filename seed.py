"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb journals")
os.system("createdb journals")

model.connect_to_db(server.app)
model.db.create_all()



users = []
names = ["June", "Francisco", "Frederico", "Nelly", "Maria", "Michelle", "David", "Gus", "Izzy", "Owen", "Chris"]

for n in range(10):
    email = f'{names[n]}@test.com'
    password = 'password'
    user_name = f'{names[n]}'
    
    user = crud.create_user(user_name, email, password)
    users.append(user)

model.db.session.add_all(users)
model.db.session.commit()

# journal = []

# for journal in journals:
#     new_journal = choice([])

# img_url = result['secure_url']

model.db.session.commit()