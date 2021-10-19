#!/usr/bin/python3
"""Test of Rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class to test"""

    def test_id(self):
        """id test"""
        r1 = Rectangle(10, 2)
        id = r1.id
        self.assertEqual(id, 2)
        r2 = Rectangle(10, 2, 0, 0, 10)
        id = r2.id
        self.assertEqual(id, 10)

    def test_validate(self):
        """Validate integer"""
        self.assertRaises(TypeError, Rectangle, 20, "4")
        self.assertRaises(TypeError, Rectangle, "a", 2)
        self.assertRaises(ValueError, Rectangle, 5, 0)
        self.assertRaises(ValueError, Rectangle, 3, -1)
        self.assertRaises(ValueError, Rectangle, 4, 6, 1, -1)
