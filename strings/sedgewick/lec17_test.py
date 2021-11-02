import unittest

from lcp import lcp
from key_indexed_counting import key_indexed_counting
from lsd_radix_sort import (
    lsd_radix_sort, counting_sort, counting_sort_alphabets
)


class Leccture17(unittest.TestCase):
    def test_lcp(self):
        input = ('prefetch', 'prefix')
        actual = lcp(input[0], input[1])
        expected = 4
        self.assertEqual(actual, expected, 'lcp')

    def test_key_indexed_counting(self):
        input = 'dacffbdbfbea'
        actual = ''.join(key_indexed_counting(input))
        expected = 'aabbbcddefff'
        self.assertEqual(actual, expected, 'key indexed counting')

    def test_lsd_radix_sort(self):
        input = [
            'dab', 'cab', 'fad', 'bad', 'dad', 'ebb', 'ace', 'add',
            'fed', 'bed', 'fee', 'bee'
        ]
        actual = lsd_radix_sort(input, 3)
        expected = [
            'ace', 'add', 'bad', 'bed', 'bee', 'cab', 'dab', 'dad',
            'ebb', 'fad', 'fed', 'fee'
        ]
        self.assertListEqual(actual, expected, 'lsd radix sort')

    def test_counting_sort(self):
        input = [2, 5, 3, 0, 2, 3, 0, 3]
        k = 6
        actual = counting_sort(input, k)
        expected = [0, 0, 2, 2, 3, 3, 3, 5]
        self.assertEqual(actual, expected, 'counting sort')

    def test_alphabets_counting_sort(self):
        input = 'ababacddaccba'
        actual = counting_sort_alphabets(input)
        expected = 'aaaaabbbcccdd'
        self.assertEqual(actual, expected, 'alphabets counting sort')


if __name__ == "__main__":
    unittest.main()
