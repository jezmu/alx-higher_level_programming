#!/usr/bin/python3
"""Square class tests"""

import unittest
from models.square import Square


class SquareTest(unittest.TestCase):
    def test_square_str(self):
        s = Square(2, 3, 4, 9)
        self.assertEqual(str(s), "[Square] (9) 3/4 - 2")

    def test_size_setter(self):
        s = Square(1)
        s.size = 4
        self.assertEqual(s.width, 4)
        self.assertEqual(s.height, 4)

    def test_size_getter(self):
        s = Square(3)
        self.assertEqual(s.size, 3)

    def test_update_with_args_and_kwargs(self):
        s = Square(3)
        s.update(4, 5, 6, 7, id=2, size=9, x=10, y=11)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

    def test_update_with_only_kwargs(self):
        s = Square(3)
        s.update(id=4, size=5, x=6, y=7)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 6)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        s = Square(3, 4, 5, 6)
        d = s.to_dictionary()
        self.assertIn("id", d)
        self.assertIn("size", d)
        self.assertIn("x", d)
        self.assertIn("y", d)
        self.assertEqual(d["id"], 6)
        self.assertEqual(d["size"], 3)
        self.assertEqual(d["x"], 4)
        self.assertEqual(d["y"], 5)

    def test_create_square(self):
        s = Square.create(id=1, x=2,y=3, size=4)
        self.assertEqual(1, s.id)
        self.assertEqual(4, s.size)
        self.assertEqual(2, s.x)
        self.assertEqual(3, s.y)
