# compress string from aabcccccaa -> a2b1c5a2


import unittest


def string_compression(string):

    res = []
    i = 0
    count = 0

    while i < len(string):

        if i == 0:
            res.append(string[i])
            count += 1
        elif i != 0 and string[i] == string[i - 1]:
            count += 1

        elif i != 0 and string[i] != string[i - 1]:
            res.append(str(count))
            res.append(string[i])
            count = 1

        i += 1
    res.append(str(count))
    return "".join(res)


class Test(unittest.TestCase):
    test_cases = [("aabcccccaa", "a2b1c5a2"), ("aabccaa", "a2b1c2a2")]

    def test_string_compression(self):
        for (string1, expected) in self.test_cases:
            result = string_compression(string1)
            self.assertEqual(
                result, expected, msg=f"Expected {expected} from {string1}"
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
