#!/usr/bin/python3
"""Test initialization. """


from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test initialization. """

    def __init__(self, *args, **kwargs):
        """Test initialization. """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Test initialization. """
        new = Review(place_id="id")
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """Test initialization. """
        new = Review(user_id="id")
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """Test initialization. """
        new = Review(text="id")
        self.assertEqual(type(new.text), str)
