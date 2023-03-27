#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):

    storageType = getenv("HBNB_TYPE_STORAGE")
    __tablename__ = 'states'
    """ State class """
    name = Column(String(128), nullable=False)

    if storageType == 'db':
        cities = relationship('City', backref='state', cascade='delete')

    else:
        @property
        def cities(self):
            """returns list of cities with matching state ids"""
            from models import storage

            citylist = []
            for val in storage.all(City).values():
                if val.state_id == self.id:
                    citylist.append(val)
            return citylist
