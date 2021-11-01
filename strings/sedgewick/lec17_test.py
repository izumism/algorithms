import unittest

from lcp import lcp
from key_indexed_counting import key_indexed_counting
from lsd_radix_sort import lsd_radix_sort


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


if __name__ == "__main__":
    unittest.main()
