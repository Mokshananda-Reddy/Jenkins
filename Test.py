#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from length import length

class Testlength(unittest.TestCase):
    def test_list_int(self):
        """
        Test case to add two numbers
        """
        data = "1234567890"
        result = length(data)
        self.assertEqual(result, 10)

if __name__ == '__main__':
    unittest.main()