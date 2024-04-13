#!/usr/bin/env python3
""" Doc doc doc
"""
from parameterized import parameterized

import unittest
from unittest.mock import patch

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test GithubOrgClient class """
    @parameterized.expand(['google', 'abc'])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Test org method of GithubOrgClient"""
        client = GithubOrgClient(org_name)
        client.org()

        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)
