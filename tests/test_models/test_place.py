#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = Place(city_id="id")
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = Place(user_id="id")
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = Place(name="id")
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = Place(description="id")
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = Place(number_rooms=3)
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = Place(number_bathrooms=3)
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = Place(max_guest=3)
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = Place(price_by_night=3)
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = Place(latitude=3.1)
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = Place(longitude=3.1)
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """ """
        new = Place(amenity_ids=['kot'])
        self.assertEqual(type(new.amenity_ids), list)
