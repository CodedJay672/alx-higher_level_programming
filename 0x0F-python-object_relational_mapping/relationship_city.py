#!/usr/bin/python3

"""
   module which creates a class definition of a city object
   Base class is included. Finally, links to MySQL table
   "City"

"""

from sqlalchemy import Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
        City class inherits from declarative Base class
        class attributes:
            @id: state id
            @name: state name

    """

    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship("State", back_populates='cities')
