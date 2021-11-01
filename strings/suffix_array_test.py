import unittest

from suffix_array import (
    suffixes_lexicographic_order,
    suffix_array,
    get_cyclic_order_index,
    construct_suffix_array,
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

    def test_cyclic_order_index(self):
        string = 'ababaa$'
        expected = [6, 0, 2, 4, 5, 1, 3]
        actual = get_cyclic_order_index(string, 1)
        self.assertListEqual(actual, expected, 'cyclic_order, 1')
        expected = [6, 5, 4, 0, 2, 1, 3]
        actual = get_cyclic_order_index(string, 2)
        self.assertListEqual(actual, expected, 'cyclic_order, 2')
        expected = [6, 5, 4, 2, 0, 3, 1]
        actual = get_cyclic_order_index(string, 4)
        self.assertListEqual(actual, expected, 'cyclic_order, 4')
        expected = [6, 5, 4, 2, 0, 3, 1]
        actual = get_cyclic_order_index(string, 8)
        self.assertListEqual(actual, expected, 'cyclic_order, 4')
    
    def test_construct_suffix_array(self):
        string = 'ababaa$'
        actual = construct_suffix_array(string)
        expected = [6, 5, 4, 2, 0, 3, 1]
        self.assertListEqual(actual, expected, 'suffix array')


if __name__ == "__main__":
    unittest.main()
