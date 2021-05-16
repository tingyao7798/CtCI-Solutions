# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.


import unittest


def is_palindrome_perm(string):
    # check if odd characters besides whitespace
    odds = 0

    alpha_counts = {}

    for char in string.lower().replace(" ", ""):
        if not alpha_counts.get(char):
            alpha_counts[char] = 1
        else:
            alpha_counts[char] += 1

        if alpha_counts[char] % 2:
            odds += 1
        else:
            odds -= 1

    return True if odds <= 1 else False


class Test(unittest.TestCase):
    true_cases = [
        ("tact coa"),
        ("hello olleh"),
        "Able was I ere I saw Elba",
        "no x in nixon",
    ]
    false_cases = [("very wrong case"), ("obv wrong case")]

    def test_unique(self):
        for test_case in self.true_cases:
            result = is_palindrome_perm(test_case)
            self.assertTrue(result, msg=f"Expected True from {test_case}")
        for test_case in self.false_cases:
            result = is_palindrome_perm(test_case)
            self.assertFalse(result, msg=f"Expected False from {test_case}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
