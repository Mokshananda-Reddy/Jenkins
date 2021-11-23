#!/usr/bin/python3
# Test case for adding two numbers
import unittest

from length import length

class Testlength(unittest.TestCase):
    def test_list_int1(self):
        data = "1234567890"
        result = length(data)
        self.assertEqual(result, 10)

    def test_list_int2(self):
        data = "Mokshananda"
        result = length(data)
        self.assertEqual(result, 20)

    def test_list_int3(self):
        data = "Moksha14102001"
        result = length(data)
        self.assertEqual(result, 14)
        
if __name__ == '__main__':
    unittest.main()
