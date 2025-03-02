from coe_number.fizzbuzz import fizzbuzz

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_give_1_should_return_empty(self):
        num = 1
        result = fizzbuzz(num)
        self.assertEqual(result, "")

    def test_give_3_should_return_fizz(self):
        num = 3
        result = fizzbuzz(num)
        self.assertEqual(result, "Fizz")

    def test_give_5_should_return_buzz(self):
        num = 5
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")

    def test_give_15_should_return_fizzbuzz(self):
        num = 15
        result = fizzbuzz(num)
        self.assertEqual(result, "FizzBuzz")

    def test_give_neg1_should_return_empty_str(self):
        num = -1
        result = fizzbuzz(num)
        self.assertEqual(result, "")

    def test_give_0_should_return_fizzbuzz(self):
        num = 0
        result = fizzbuzz(num)
        self.assertEqual(result, "FizzBuzz")

    def test_give_112019_should_return_empty_str(self):
        num = 112019
        result = fizzbuzz(num)
        self.assertEqual(result, "")

    def test_give_112018_should_return_empty_str(self):
        num = 112018
        result = fizzbuzz(num)
        self.assertEqual(result, "")

    def test_give_112025_should_return_buzz(self):
        num = 112025
        result = fizzbuzz(num)
        self.assertEqual(result, "Buzz")

    def test_give_112035_should_return_fizzbuzz(self):
        num = 112035
        result = fizzbuzz(num)
        self.assertEqual(result, "FizzBuzz")