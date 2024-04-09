#!/usr/bin/env python3
""" Doc doc doc
"""
from parameterized import parameterized

import unittest

from client import GithubOrgClient


@parameterized.expand(['google', 'abc'])
class TestGithubOrgClient(unittest.TestCase):
    """ Doc doc doc """
    def test_org(self):
        """ Doc doc doc """
        pass
