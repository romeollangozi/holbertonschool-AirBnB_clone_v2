#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer,\
    String, DateTime, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os


association_table = Table('place_amenity',
                          Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False),
                          )


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'

    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128),
                  nullable=False)
    description = Column(String(1024),
                         nullable=True)
    number_rooms = Column(Integer,
                          nullable=False,
                          default=0)
    number_bathrooms = Column(Integer,
                              nullable=False,
                              default=0)
    max_guest = Column(Integer,
                       nullable=False,
                       default=0)
    price_by_night = Column(Integer,
                            nullable=False,
                            default=0)
    latitude = Column(Float,
                      nullable=True)
    longitude = Column(Float,
                       nullable=True)
    reviews = relationship('Review',
                           cascade='delete',
                           backref='place')
    amenities = relationship('Amenity',
                             secondary='place_amenity',
                             back_populates='place_amenities',
                             viewonly=False)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            from models.review import Review
            from models import storage

            return [review for review in storage.all(Review).values()
                    if review["place_id"] == self.id]

        @property
        def amenities(self):
            '''
            Amenities getter
            '''
            from models.amenity import Amenity
            from models import storage
            amenities_list = []

            for amenity in list(storage.all(Amenity).values()):
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, obj):
            '''Amenities id setter'''

            from models.amenity import Amenity
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
