from coe_number.alternate import alternate

import unittest


class TestAlternate(unittest.TestCase):

    def test_give_beabeefeab_should_return_5(self):
        string = "beabeefeab"
        result = alternate(string)
        self.assertEqual(result, 5)

    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_should_return_8(self):
        string = "asdcbsdcagfsdbgdfanfghbsfdab"
        result = alternate(string)
        self.assertEqual(result, 8)

    def test_give_ab_should_return_2(self):
        string = "ab"
        result = alternate(string)
        self.assertEqual(result, 2)

    def test_give_abc_should_return_2(self):
        string = "abc"
        result = alternate(string)
        self.assertEqual(result, 2)

    def test_give_abcabc_should_return_4(self):
        string = "abcabc"
        result = alternate(string)
        self.assertEqual(result, 4)

    def test_give_empty_string_should_return_0(self):
        string = ""
        result = alternate(string)
        self.assertEqual(result, 0)

    def test_give_single_character_a_should_return_0(self):
        string = "a"
        result = alternate(string)
        self.assertEqual(result, 0)

    def test_give_aabbcc_should_return_0(self):
        string = "aabbcc"
        result = alternate(string)
        self.assertEqual(result, 0)

    def test_give_space_only_should_return_0(self):
        string = "   "
        result = alternate(string)
        self.assertEqual(result, 0)

    def test_give_special_characters_should_return_6(self):
        string = ".,.,.,"
        result = alternate(string)
        self.assertEqual(result, 6)

    def test_give_unicode_thai_characters_should_return_7(self):
        string = "กขกขกขกขก"
        result = alternate(string)
        self.assertEqual(result, 9)

    def test_give_unicode_thai_characters_should_return_0(self):
        string = "กกขขคค"
        result = alternate(string)
        self.assertEqual(result, 0)