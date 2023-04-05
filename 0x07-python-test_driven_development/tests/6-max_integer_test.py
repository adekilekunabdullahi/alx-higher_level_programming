#!/usr/bin/python3
import unittest
import sys
test = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    """
    class TestMaxInteger
    """
    def testMax(self):
        """
        function testMax
        """
        self.assertTrue(test([2,3,4,5]), 5)
    def testNone(self):
        """
        function testNone
        """
        self.assertEqual(test([]), None)
    def test_for_strings(self):
        """
        test_for_strings
        """
        self.assertTrue(test(['ab','e']), 'e')
