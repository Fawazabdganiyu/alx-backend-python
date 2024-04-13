#!/usr/bin/env python3
""" Doc doc doc
"""
from parameterized import parameterized

import unittest
from unittest.mock import patch, PropertyMock

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

    def test_public_repos_url(self) -> None:
        """Test _public_repos_url property of GithubOrgClient class"""
        payload = {'repos_url': 'https://api.github.com/orgs/google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = mock_payload

            client = GithubOrgClient('google')

            self.assertEqual(
                client._public_repos_url,
                'https://api.github.com/orgs/google/repos'
            )
