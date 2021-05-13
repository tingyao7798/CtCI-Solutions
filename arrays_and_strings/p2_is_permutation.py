# Given two strings, write a method to decide if
# one is a permutation of the other
import unittest


def is_permutation(string_1, string_2):
    # use XOR operator to find pairs
    res = 0
    for char in string_1 + string_2:
        res ^= ord(char)

    return True if res == 0 else False


class Test(unittest.TestCase):
    true_cases = [
        ("abcdef", "bacdef"),
        ("3563476", "7334566"),
        ("wef34f", "wffe34"),
    ]
    false_cases = [
        ("abcd", "d2cba"),
        ("2354", "1234"),
        ("dcw4f", "dcw5f"),
    ]

    def test_unique(self):
        for test_case in self.true_cases:
            result = is_permutation(*test_case)
            self.assertTrue(result, msg=f"Expected True from {test_case}")
        for test_case in self.false_cases:
            result = is_permutation(*test_case)
            self.assertFalse(result, msg=f"Expected False from {test_case}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
