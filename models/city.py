#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    The city class, contains state ID and name

    Attr:
    __tablename__ (str); name of table where instances will be stored
    name (str): 128 char name of city, cannot be null
    state_id (str); 60 char id of state, foreign key to states table
    """
    __tablename__ = 'cities'

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
