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



journal = []

for user in users:

    journal = crud.create_journal(user.user_id, content, date_time)
    journal.append(new_journal)

model.db.session.add_all(journal)
model.db.session.commit()




travel_journal = []

for user in users:
    
    travel_journal = crud.create_travel_journal(user.user_id, content, date_time, address)
    travel_journal.append(new_travel_journal)

model.db.session.add_all(travel_journal)
model.db.session.commit()


# for journal in journals:
#     new_journal = choice([])

# img_url = result['secure_url']

# model.db.session.commit()