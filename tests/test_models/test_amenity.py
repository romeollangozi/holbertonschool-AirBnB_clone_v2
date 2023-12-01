#!/usr/bin/python3
"""Test initialization."""


from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Test initialization."""

    def __init__(self, *args, **kwargs):
        """Test initialization. """

        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Test initialization. """

        new = Amenity(name="name")
        self.assertEqual(type(new.name), str)
