from coe_number.alternatingCharacters import alternatingCharacters

import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_give_AAAA_should_return_3(self):
        string = "AAAA"
        result = alternatingCharacters(string)
        self.assertEqual(result, 3)

    def test_give_BBBBB_should_return_4(self):
        string = "BBBBB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 4)

    def test_give_ABABABAB_should_return_0(self):
        string = "ABABABAB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 0)

    def test_give_AAABBB_should_return_4(self):
        string = "AAABBB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 4)

    def test_give_AAABBBAABB_should_return_6(self):
        string = "AAABBBAABB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 6)
    
    def test_give_AABBAABB_should_return_4(self):
        string = "AABBAABB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 4)

    def test_give_ABABABAA_should_return_1(self):
        string = "ABABABAA"
        result = alternatingCharacters(string)
        self.assertEqual(result, 1)
    
    def test_give_XYZXXQWE_should_return_4(self):
        string = "XYZXXQWE"
        result = alternatingCharacters(string)
        self.assertEqual(result, 1)

    def test_give_A_should_return_0(self):
        string = "A"
        result = alternatingCharacters(string)
        self.assertEqual(result, 0)
    
    def test_give_empty_string_should_return_0(self):
        string = ""
        result = alternatingCharacters(string)
        self.assertEqual(result, 0)
    
    def test_give_AB_should_return_0(self):
        string = "AB"
        result = alternatingCharacters(string)
        self.assertEqual(result, 0)

    def test_give_AA_should_return_1(self):
        string = "AA"
        result = alternatingCharacters(string)
        self.assertEqual(result, 1)

    def test_give_กกก_should_return_2(self):
        string = "กกก"
        result = alternatingCharacters(string)
        self.assertEqual(result, 2)

    def test_give_dotandcolon_should_return_0(self):
        string = ".,.,"
        result = alternatingCharacters(string)
        self.assertEqual(result, 0)

    def test_give_6space_should_return_6(self):
        string = "       "
        result = alternatingCharacters(string)
        self.assertEqual(result, 6)