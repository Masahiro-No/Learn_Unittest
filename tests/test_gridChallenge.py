from coe_number.gridChallenge import gridChallenge

import unittest

class TestGridChallenge(unittest.TestCase):
    def test_give_abc_bdf_ceg_should_return_YES(self):
        grid = ["abc", "bdf", "ceg"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_cba_daf_geh_should_return_YES(self):
        grid = ["cba", "daf", "geh"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_abc_ade_afg_should_return_YES(self):
        grid = ["abc", "ade", "afg"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_zxy_should_return_YES(self):
        grid = ["zxy"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_a_b_c_should_return_YES(self):
        grid = ["a", "b", "c"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_b_a_c_should_return_NO(self):
        grid = ["b", "a", "c"]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")
    
    def test_give_aaa_aaa_aaa_should_return_YES(self):
        grid = ["aaa", "aaa", "aaa"]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_large_case_should_return_YES(self):
        grid = [
            "ebacd",
            "fghij",
            "olmkn",
            "trpqs",
            "xywuv"
        ]
        result = gridChallenge(grid)
        self.assertEqual(result, "YES")
    
    def test_give_large_case_fail_should_return_NO(self):
        grid = [
            "zyxwvutsrq",
            "ponmlkjihg",
            "edcbazyxwv",
            "utsrqponml",
            "kjihgfedcb",
            "azyxwvutsr",
            "qponmlkjih",
            "gfedcbazyx",
            "wvutsrqpon",
            "mlkjihgfed"
        ]
        result = gridChallenge(grid)
        self.assertEqual(result, "NO")
