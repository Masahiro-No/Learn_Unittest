from coe_number.caesarCipher import caesarCipher

import unittest

class TestCaesarCipher(unittest.TestCase):
    def test_give_middle_Outz_and_2_should_return_okffng_Qwvb(self):
        string = "middle-Outz"
        key = 2
        result = caesarCipher(string, key)
        self.assertEqual(result, "okffng-Qwvb")

    def test_give_Hello_World_and_4_should_return_Lipps_Asvph(self):
        string = "Hello_World!"
        key = 4
        result = caesarCipher(string, key)
        self.assertEqual(result, "Lipps_Asvph!")
    
    def test_give_A_and_1_should_return_B(self):
        string = "A"
        key = 1
        result = caesarCipher(string, key)
        self.assertEqual(result, "B")

    def test_give_Z_and_1_should_return_A(self):
        string = "Z"
        key = 1
        result = caesarCipher(string, key)
        self.assertEqual(result, "A")

    def test_give_a_and_1_should_return_b(self):
        string = "a"
        key = 1
        result = caesarCipher(string, key)
        self.assertEqual(result, "b")

    def test_give_z_and_1_should_return_a(self):
        string = "z"
        key = 1
        result = caesarCipher(string, key)
        self.assertEqual(result, "a")

    def test_give_AaZz_and_1_should_return_BbAa(self):
        string = "AaZz"
        key = 1
        result = caesarCipher(string, key)
        self.assertEqual(result, "BbAa")

    def test_give_A_and_neg1_should_return_Z(self):
        string = "A"
        key = -1
        result = caesarCipher(string, key)
        self.assertEqual(result, "Z")

    def test_give_a_and_neg1_should_return_z(self):
        string = "a"
        key = -1
        result = caesarCipher(string, key)
        self.assertEqual(result, "z")

    def test_give_Z_and_neg1_should_return_Y(self):
        string = "Z"
        key = -1
        result = caesarCipher(string, key)
        self.assertEqual(result, "Y")

    def test_give_AaZz_and_4_should_return_EeDd(self):
        string = "AaZz"
        key = 4
        result = caesarCipher(string, key)

    def test_give_space_space_space_and_5_should_return_space_space_space(self):
        string = "   "
        key = 5
        result = caesarCipher(string, key)
        self.assertEqual(result, "   ")

    def test_give_1234567890_and_6_should_return_1234567890(self):
        string = "1234567890"
        key = 6
        result = caesarCipher(string, key)
        self.assertEqual(result, "1234567890")

    def test_give_empty_string_and_7_should_return_empty_string(self):
        string = ""
        key = 7
        result = caesarCipher(string, key)
        self.assertEqual(result, "")

    def test_give_a_and_0_should_return_a(self):
        string = "a"
        key = 0
        result = caesarCipher(string, key)
        self.assertEqual(result, "a")

    def test_give_A_and_0_should_return_A(self):
        string = "A"
        key = 0
        result = caesarCipher(string, key)
        self.assertEqual(result, "A")

    def test_give_comma_c_comma_vsdlss_slash_xkf_and_3_should_return_comma_f_comma_yvguv_slash_ani(self):
        string = ",c,c,vsdlss/xkf"
        key = 3
        result = caesarCipher(string, key)
        self.assertEqual(result, ",f,f,yvgovv/ani")