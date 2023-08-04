#!/usr/bin/python3
"""This module contains tests for Amenity"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Defines the tests"""

    def __init__(self, *args, **kwargs):
        """Initializes a test"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity
        self.amenity = Amenity()
        self.amenity.name = "an amenity"

    def test_name2(self):
        """Tests the attribute name"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))

    def test_AmenityTypes(self):
        """tests attribute type for Amenity"""
        self.assertEqual(type(self.amenity.name), str)


if __name__ == "__main__":
    unittest.main()
