# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
import unittest


def is_unique_char(string):
    checker = 0

    for char in string:
        # convert to ascii value
        val = ord(char)

        # check if val has already been seen
        # at the corresponding bit in checker
        if checker & (1 << val):
            return False

        # by bitwise shifting by val of check, we are setting a seen flag
        checker |= 1 << val

    return True


class Test(unittest.TestCase):
    true_cases = ["abcd", "defg", ""]
    false_cases = ["aabc", "1123ab", "abcdefg1234566"]

    def test_unique(self):
        for test_case in self.true_cases:
            result = is_unique_char(test_case)
            self.assertTrue(result, msg=f"Expected True from {test_case}")
        for test_case in self.false_cases:
            result = is_unique_char(test_case)
            self.assertFalse(result, msg=f"Expected False from {test_case}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
