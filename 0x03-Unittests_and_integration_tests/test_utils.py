#!/usr/bin/env python3
"""
Test module for `utils` module
"""
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any
)
import unittest

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Definition of test class for `utils.access_nested_map`
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Any
    ) -> None:
        """ Test that the method returns the expected output
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
