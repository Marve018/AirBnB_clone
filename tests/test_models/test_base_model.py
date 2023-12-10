#!/usr/bin/python3
"""Unittests for base_models"""
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """unittests for testing the BaseModel class"""

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
