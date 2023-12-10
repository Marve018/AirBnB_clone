#!/usr/bin/python3
"""Unittests for base_models"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """unittests for testing the BaseModel class"""

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """chekcing if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
    
    def setUp(self):
        self.base_model = BaseModel()

    def test_instance_creation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_id_generation(self):
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        self.assertIsNotNone(self.base_model.created_at)

    def test_updated_at(self):
        self.assertIsNotNone(self.base_model.updated_at)

if __name__ == '__main__':
    unittest.main()
