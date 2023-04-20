#!/usr/bin/python3
""" tests for models/rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base

class test_Rectangle(unittest.TestCase):
    def test_doc(self):
        self.assertTrue(Rectangle.__doc__, "rectangle class implementation")
    def test_instance(self):
        self.assertIsInstance(Rectangle(2,3), Base)
    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()
    def test_for_1_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)
    def test_for_id(self):
        self.assertEqual(Rectangle(2,4).id, Rectangle(2,5).id - 1)
    def test_for_predefined_id(self):
        self.assertEqual(Rectangle(2,4,6,8,9).id, 9)
    def test_for_more_than_allowed_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2,3,4,6,7,8)
    def test_for_private_attribute(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2,4).__height)
        with self.assertRaises(AttributeError):
            print(Rectangle(2,6).__width)
        with self.assertRaises(AttributeError):
            print(Rectangle(5,8).__x)
        with self.assertRaises(AttributeError):
            print(Rectangle(8,9).__y)
    def test_for_getters(self):
        a = Rectangle(2,3,4,5)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 3)
        self.assertEqual(a.x, 4)
        self.assertEqual(a.y, 5)

