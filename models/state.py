#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import Base
from sqlalchemy import Column, Integer,\
    String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128),
                  nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            from models.city import City
            from models import storage

            return [value for key, value in storage.all(City).items()
                    if value.to_dict()['state_id'] == self.id]
