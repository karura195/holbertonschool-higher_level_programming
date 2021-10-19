#!/usr/bin/python3
"""Test of class Base"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """class to test"""

    def test_id(self):
        b1 = Base()
        id = b1.id
        self.assertEqual(id, 1)

        b2 = Base(12)
        id = b2.id
        self.assertEqual(id, 12)
