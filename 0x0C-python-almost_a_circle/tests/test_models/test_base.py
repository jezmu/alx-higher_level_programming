#!/usr/bin/python3
"""Base class tests"""

import unittest
from models.base import Base


class BaseModelTest(unittest.TestCase):
    def test_none_id(self):
        x = Base()
        self.assertEqual(1, x.id)

    def test_provided_id(self):
        x = Base(5)
        self.assertEqual(5, x.id)

    def test_to_json_string_None_list(self):
        s = Base.to_json_string(None)
        self.assertEqual("[]", s)

    def test_to_json_string_empty_list(self):
        s = Base.to_json_string([])
        self.assertEqual("[]", s)

    def test_to_json_string_single_item(self):
        s = Base.to_json_string([{'id':2,'width': 4, 'height':3}])
        self.assertEqual('[{"id": 2, "width": 4, "height": 3}]', s)

    def test_to_json_string_multiple_items(self):
        s = Base.to_json_string(
            [{'id':2,'width': 4, 'height':3}, {'id':2,'width': 4, 'height':3}])
        self.assertEqual(
            '[{"id": 2, "width": 4, "height": 3}, {"id": 2, "width": 4, "height": 3}]', s)

    def test_from_json_string_empty_input(self):
        l = Base.from_json_string("")
        self.assertEqual([], l)
    
    def test_from_json_string_None_input(self):
        l = Base.from_json_string(None)
        self.assertEqual([], l)

    def test_from_json_string_ok_input(self):
        l = Base.from_json_string(
            '[{"id": 2, "width": 4, "height": 3}, {"id": 2, "width": 4, "height": 3}]')
        expected = [{'id':2,'width': 4, 'height':3}, {'id':2,'width': 4, 'height':3}]
        self.assertEqual(expected, l)
