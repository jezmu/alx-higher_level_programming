#!/usr/bin/python3
"""Rectangle tests"""

import unittest
from models.rectangle import Rectangle


class RectangleTest(unittest.TestCase):
    def test_ok_width(self):
        o = Rectangle(1,1)
        self.assertEqual(1, o.width)
    
    def test_ok_height(self):
        o = Rectangle(1,1)
        self.assertEqual(1, o.height)

    def test_ok_x(self):
        o = Rectangle(1,1,1,1)
        self.assertEqual(1, o.x)
    
    def test_ok_y(self):
        o = Rectangle(1,1,1,1)
        self.assertEqual(1, o.y)

    def test_exception_for_height_lte_zero(self):
        with self.assertRaises(ValueError) as ctxt:
            o = Rectangle(1, 0)
        self.assertEqual(str(ctxt.exception), "height must be > 0")

    def test_exception_for_width_lte_zero(self):
        with self.assertRaises(ValueError, msg="width must be > 0") as ctxt:
            o = Rectangle(0, 1)
        self.assertEqual(str(ctxt.exception), "width must be > 0")

    def test_exception_for_non_int_height(self):
        with self.assertRaises(TypeError, msg="height must be an integer") as ctxt:
            o = Rectangle(1, '')
        self.assertEqual(str(ctxt.exception), "height must be an integer")

    def test_exception_for_non_int_width(self):
        with self.assertRaises(TypeError, msg="width must be an integer") as ctxt:
            o = Rectangle('', 1)
        self.assertEqual(str(ctxt.exception), "width must be an integer")

    def test_exception_for_non_int_x(self):
        with self.assertRaises(TypeError, msg="x must be an integer") as ctxt:
            o = Rectangle(1, 1,'')
        self.assertEqual(str(ctxt.exception), "x must be an integer")

    def test_exception_for_non_int_y(self):
        with self.assertRaises(TypeError, msg="y must be an integer") as ctxt:
            o = Rectangle(1, 1,1,'')
        self.assertEqual(str(ctxt.exception), "y must be an integer")

    def test_exception_for_x_lt_zero(self):
        with self.assertRaises(ValueError, msg="x must be >= 0") as ctxt:
            o = Rectangle(1, 1, -1)
        self.assertEqual(str(ctxt.exception), "x must be >= 0")

    def test_exception_for_y_lt_zero(self):
        with self.assertRaises(ValueError, msg="y must be >= 0") as ctxt:
            o = Rectangle(1, 1, 1, -1)
        self.assertEqual(str(ctxt.exception), "y must be >= 0")

    def test_area(self):
        o = Rectangle(2,3)
        self.assertEqual(6, o.area())

    def test_rect_display_no_offsets(self):
        o = Rectangle(1,1)
        o2 = Rectangle(2,3)
        self.assertEqual("#", o.convert_to_str())
        self.assertEqual("##\n##\n##", o2.convert_to_str())

    def test_rect_display_with_offsets(self):
        o = Rectangle(2,2, 1, 2)
        o2 = Rectangle(2,2, 0, 2)
        o3 = Rectangle(2,2, 1, 0)
        self.assertEqual("\n\n ##\n ##", o.convert_to_str())
        self.assertEqual("\n\n##\n##", o2.convert_to_str())
        self.assertEqual(" ##\n ##", o3.convert_to_str())

    def test_rect_str(self):
        o = Rectangle(1,2,3,4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(o))

    def test_update_with_no_args(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update()
        self.assertEqual(5, o.id)
        self.assertEqual(1, o.width)
        self.assertEqual(2, o.height)
        self.assertEqual(3, o.x)
        self.assertEqual(4, o.y)

    def test_update_with_exact_args(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update(6, 7, 8, 9, 10)
        self.assertEqual(o.id, 6)
        self.assertEqual(o.width, 7)
        self.assertEqual(o.height, 8)
        self.assertEqual(o.x, 9)
        self.assertEqual(o.y, 10)

    def test_update_with_excess_args(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update(6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(o.id, 6)
        self.assertEqual(o.width, 7)
        self.assertEqual(o.height, 8)
        self.assertEqual(o.x, 9)
        self.assertEqual(o.y, 10)

    def test_update_with_valid_kwargs(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update(id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(o.id, 6)
        self.assertEqual(o.width, 7)
        self.assertEqual(o.height, 8)
        self.assertEqual(o.x, 9)
        self.assertEqual(o.y, 10)
    
    def test_update_with_invalid_kwargs(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update(id=6, width=7, height=8, x=9, y=10, z=3)
        self.assertEqual(o.id, 6)
        self.assertEqual(o.width, 7)
        self.assertEqual(o.height, 8)
        self.assertEqual(o.x, 9)
        self.assertEqual(o.y, 10)

    def test_update_with_non_empty_args_and_non_empty_kwargs(self):
        o = Rectangle(1,2, 3, 4, 5)
        o.update(11, 12, 13, 14, 15, id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(o.id, 11)
        self.assertEqual(o.width, 12)
        self.assertEqual(o.height, 13)
        self.assertEqual(o.x, 14)
        self.assertEqual(o.y, 15)

    def test_to_dictionary(self):
        o = Rectangle(1,2,3,4,5)
        d = o.to_dictionary()
        self.assertTrue("id" in d)
        self.assertTrue("x" in d)
        self.assertTrue("y" in d)
        self.assertTrue("width" in d)
        self.assertTrue("height" in d)
        self.assertEqual(d["id"], 5)
        self.assertEqual(d["x"], 3)
        self.assertEqual(d["y"], 4)
        self.assertEqual(d["width"], 1)
        self.assertEqual(d["height"], 2)

    def test_create_rectangle(self):
        r = Rectangle.create(id=1, x=2,y=3, width=4, height=5)
        self.assertEqual(1, r.id)
        self.assertEqual(4, r.width)
        self.assertEqual(5, r.height)
        self.assertEqual(2, r.x)
        self.assertEqual(3, r.y)
