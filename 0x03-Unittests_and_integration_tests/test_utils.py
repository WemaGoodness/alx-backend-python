#!/usr/bin/env python3
"""
Unit tests for the memoize decorator in utils module.
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
        A test class to demonstrate the memoize decorator.
        """

        def a_method(self):
            """
            A method that returns 42.
            """
            return 42

        @memoize
        def a_property(self):
            """
            A memoized property that calls a_method.
            """
            return self.a_method()

    def test_memoize(self):
        """
        Test that a_method is only called once when accessing a_property
        multiple times.
        """
        with patch.object(self.TestClass, 'a_method', return_value=42) as mock_method:
            test_obj = self.TestClass()
            # First call to a_property, should trigger a_method
            self.assertEqual(test_obj.a_property, 42)
            # Second call to a_property, should use memoized value,
            # not trigger a_method
            self.assertEqual(test_obj.a_property, 42)
            # Verify a_method was called only once
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()

