#!/usr/bin/python3
"""Test initialization. """


from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test initialization. """

    def __init__(self, *args, **kwargs):
        """ Test initialization."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Test initialization. """
        new = self.value(first_name="holb")
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Test initialization. """
        new = self.value(last_name="hbnb")
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Test initialization. """
        new = self.value(email="hbnb@holbertonstudents.com")
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ Test initialization."""
        new = self.value(password="hbnb123")
        self.assertEqual(type(new.password), str)
