# -*- coding: utf-8 -*-

from .context import unit22

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        unit22.hmm()


if __name__ == '__main__':
    unittest.main()
