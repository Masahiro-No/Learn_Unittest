from coe_number.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_2_is_prime(self):
        prime_list = [2]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_0_1_neg1_is_not_prime(self):
        prime_list = [0,1,-1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_1_is_not_prime(self):
        prime_list = [1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_4_6_8_10_is_not_prime(self):
        prime_list = [4, 6, 8, 10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_3_11_17_is_not_prime(self):
        prime_list = [3, 11, 17]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)