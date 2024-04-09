#!/usr/bin/env python3
"""
Test module for `utils` module
"""
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict
)
import unittest
from unittest.mock import patch, Mock

from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping, path: Sequence, expected_msg: str
    ) -> None:
        """
        Test that KeyError is raised when a nested_map
        does not have a given key
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)

        self.assertEqual(str(err.exception), expected_msg)


class TestGetJson(unittest.TestCase):
    """ Test get_json function class
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(
            self,
            test_url: str, test_payload: Dict[str, bool], mock_get: Mock
    ) -> None:
        """ Test that the expected result is returned
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        output = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(output, test_payload)
