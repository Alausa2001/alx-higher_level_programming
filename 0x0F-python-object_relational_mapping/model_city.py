#!/usr/bin/python3
"""contains the class definition of a City"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """attributes
    table_name: cities
    id: auto-generated, unique integer, can’t be null and is a primary key
    name:  column of a string of 128 characters and can’t be null
    state_id: state_id that represents a column of an integer,
                can’t be null and is a foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True,
                unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
