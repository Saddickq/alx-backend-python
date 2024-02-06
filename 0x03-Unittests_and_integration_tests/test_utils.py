#!/usr/bin/env python3
"""Module docs
"""


from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test case class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, ex_value):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), ex_value)
