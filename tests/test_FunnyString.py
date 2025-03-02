from coe_number.FunnyString import funnyString

import unittest

class TestFunnyString(unittest.TestCase):
    def test_give_acxz_is_funny(self):
        string = "acxz"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_zxc_is_not_funny(self):
        string = "zxc"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Not Funny")

    def test_give_lmnop_is_funny(self):
        string = "lmnop"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_123456789_is_funny(self):
        string = "123456789"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_247_is_not_funny(self):
        string = "247"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Not Funny")

    def test_give_dot_colon_slash_is_not_funny(self):
        string = ".:/"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Not Funny")
    
    def test_give_empty_string_is_funny(self):
        string = ""
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_thai_letter_is_funny(self):
        string = "กขฃ"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_thai_number_is_funny(self):
        string = "๑๒๓๔๕๖๗๘๙"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_thai_letter_is_not_funny(self):
        string = "กขคง"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Not Funny")

    def test_give_thai_number_is_not_funny(self):
        string = "๑๒๓๔๕๖๗๘๙๐๑"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Not Funny")

    def test_give_x_is_funny(self):
        string = "x"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_xx_is_funny(self):
        string = "xxx"
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")

    def test_give_3space_is_funny(self):
        string = "    "
        is_funny = funnyString(string)
        self.assertEqual(is_funny, "Funny")