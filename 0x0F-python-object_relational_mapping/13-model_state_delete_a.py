#!/usr/bin/python3

"""
    Script that creates a new state

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    args = sys.argv
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=Engine)
    session = Session()

    state = session.query(State).filter(State.name.like('%a%')).all()

    for row in state:
        session.delete(row)

    session.commit()
