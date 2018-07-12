import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash
from create_db import *
import json
import sys

engine = create_engine('sqlite:///users.db', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

with open('users.secure.json') as jsondata:
    data = json.load(jsondata)
    for name in data:
        pw_hash = generate_password_hash(data[name]['password'])
        user = User(name, data[name]['email'], pw_hash )
        session.add(user)
 
# commit the record the database
session.commit()