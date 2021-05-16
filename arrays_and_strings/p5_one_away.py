# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards.


import unittest


def is_one_insert_remove_away(string1, string2):
    step = 0
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):

        if not string1[i] == string2[j]:
            step += 1
            i += 1

            if step > 1:
                return False
        else:
            i += 1
            j += 1

    return True


def is_one_replace_away(string1, string2):

    replace_needed = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            replace_needed += 1
        if replace_needed > 1:
            return False
    return True


def is_one_away(string1, string2):

    if len(string1) == len(string2):
        return is_one_replace_away(string1, string2)
    elif len(string1) - len(string2) == 1:
        return is_one_insert_remove_away(string1, string2)
    elif len(string1) - len(string2) == -1:
        return is_one_insert_remove_away(string2, string1)
    else:
        return False


class Test(unittest.TestCase):
    test_cases = [
        ("pale", "ple", True),
        ("pales", "pale", True),
        ("pale", "bale", True),
        ("paleabc", "pleabc", True),
        ("pale", "ble", False),
        ("a", "b", True),
        ("", "d", True),
        ("d", "de", True),
        ("pale", "pale", True),
        ("pale", "ple", True),
        ("ple", "pale", True),
        ("pale", "bale", True),
        ("pale", "bake", False),
        ("pale", "pse", False),
        ("ples", "pales", True),
        ("pale", "pas", False),
        ("pas", "pale", False),
        ("pale", "pkle", True),
        ("pkle", "pable", False),
        ("pal", "palks", False),
        ("palks", "pal", False),
    ]

    def test_unique(self):
        for (string1, string2, expected) in self.test_cases:
            result = is_one_away(string1, string2)
            self.assertEqual(
                result, expected, msg=f"Expected {expected} from {string1},{string2}"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
