import unittest

from suffix_array import (
    suffixes_lexicographic_order,
    suffix_array,
)


class TestSuffixArray(unittest.TestCase):
    """test case for various implementation of suffix array algorithm
    """

    def test_suffixes(self):
        input = 'ababaa'
        actual = suffixes_lexicographic_order(input)
        expected = ['a', 'aa', 'abaa', 'ababaa', 'baa', 'babaa']
        self.assertListEqual(actual, expected, 'suffixes lex order')

    def test_suffix_array(self):
        string = 'ababaa$'
        actual = suffix_array(string)
        expected = [6, 5, 4, 2, 0, 3, 1]
        self.assertListEqual(actual, expected, 'suffix array')


if __name__ == "__main__":
    unittest.main()
