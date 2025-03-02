from coe_number.staircase import staircase

import unittest

class TestStaircase(unittest.TestCase):
    def test_give_1_should_return_1(self):
        value = 1
        result = staircase(value, "#")
        self.assertEqual(result, "#")

    def test_give_2_should_return_2(self):
        value = 2
        result = staircase(value, "#")
        self.assertEqual(result, " #\n##")

    def test_give_3_should_return_3(self):
        value = 3
        result = staircase(value, "#")
        self.assertEqual(result, "  #\n ##\n###")

    def test_give_31_should_return_invalid(self):
        value = 31
        result = staircase(value, "#")
        self.assertEqual(result, "Invalid input!")

    def test_give_0_should_return_invalid(self):
        value = 0
        result = staircase(value, "#")
        self.assertEqual(result, "Invalid input!")

    def test_give_minus_1_should_return_invalid(self):
        value = -1
        result = staircase(value, "#")
        self.assertEqual(result, "Invalid input!")

    def test_give_30_should_return_30(self):
        value = 30
        result = staircase(value, "#")
        self.assertTrue(result.startswith(" " * 29 + "#"))
        self.assertTrue(result.endswith("#" * 30))

    def test_give_custom_character_return_custom_char(self):
        value = 3
        result = staircase(value, "@")
        expected_output = "  @\n @@\n@@@"
        self.assertEqual(result, expected_output)

    def test_spaces_as_character(self):
        value = 3
        result = staircase(value, " ")
        expected_output = "   \n   \n   "
        self.assertEqual(result, expected_output)