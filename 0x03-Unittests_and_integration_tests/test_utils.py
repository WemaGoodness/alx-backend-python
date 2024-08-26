#!/usr/bin/env python3
"""
Unit tests for memoization decorator.
"""

import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    Test cases for the memoize decorator.
    """

    class TestClass:
        """
        Test class with memoized property.
        """
        def a_method(self):
            return 42

        @memoize
        def a_property(self):
            return self.a_method()

    def test_memoize(self):
        """
        Test that a_method is only called once when accessing a_property.
        """
        with patch.object(self.TestClass, 'a_method', return_value=42) as mock_method:
            test_obj = self.TestClass()
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
