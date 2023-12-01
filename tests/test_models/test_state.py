#!/usr/bin/python3
"""Test initialization. """


from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ Test initialization."""

    def __init__(self, *args, **kwargs):
        """Test initialization. """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test initialization."""
        new = State(name="Albania")
        self.assertEqual(type(new.name), str)
