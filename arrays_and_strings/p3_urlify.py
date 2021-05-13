# Replace all spaces in a string with %20
import unittest


def urlify_algo(string, length):

    new_index = len(string)

    for i in reversed(range(length)):
        if string[i] == " ":
            string[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            string[new_index - 1] = string[i]
            new_index -= 1

    return string


def urlify_python(string, length):
    return list("".join(string).replace(" ", "%20"))


class Test(unittest.TestCase):
    test_cases = [
        (
            list("much ado about nothing      "),
            22,
            list("much%20ado%20about%20nothing"),
        ),
        (list("Mr John Smith    "), 13, list("Mr%20John%20Smith")),
    ]

    def test_unique_algo(self):
        for [test_case, length, expected] in self.test_cases:
            result = urlify_algo(test_case, length)
            self.assertEqual(result, expected)

    def test_unique_python(self):
        for [test_case, length, expected] in self.test_cases:
            result = urlify_python(test_case, length)
            self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
