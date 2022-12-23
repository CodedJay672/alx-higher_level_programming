#!/usr/bin/python3

"""
    Script that lists all states and their correspondin
    cities.

"""

import sys
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    args = sys.argv
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(Engine)

    Session = sessionmaker(bind=Engine)
    session = Session()

    tup_st = session.query(State).outerjoin(
            City).order_by(State.id, City.id).all()

    for state in tup_st:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
