#!/usr/bin/python3

"""
    Script which creates a state with relating cities
    Args:
        @root: username for log in
        @root: password for log in
        @db: database to connect to
    Script implements alsqlchemy

"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    args = sys.argv
    Engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(args[1], args[2], args[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(Engine)

    Session = sessionmaker(bind=Engine)
    session = Session()

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)

    session.add(state)
    session.add(city)
    session.commit()
