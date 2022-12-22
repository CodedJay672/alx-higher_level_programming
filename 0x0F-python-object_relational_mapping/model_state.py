#!/usr/bin/python3

"""
   module which creates a class definition of a state object
   Base class is included. Finally, links to MySQL table
   "states"

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        State class inherits from declarative Base class
        class attributes:
            @id: state id
            @name: state name

    """

    __tablename__ = 'states'
    id = Column(Integer(11), unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
