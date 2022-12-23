#!/usr/bin/python3

"""
    script which fetches the first state from a database
    script args:
        @host: localhost
        @u.name: root
        @passwd: root

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()
    rows = session.query(State).order_by(State.id).first()
    if rows:
        print('{}: {}'.format(rows.id, rows.name))
