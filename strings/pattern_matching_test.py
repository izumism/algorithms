import unittest

from pattern_matching import (
    brute_force,
    border,
    longest_common_prefix,
    length_to_skip,
    prefix_function_bad,
    prefix_function,
    match_by_prefix_function,
)


class TestPatternMatching(unittest.TestCase):
    """test case for various implementation of pattern matching algorithm
    """

    def test_brute_force(self):
        text = 'abracadabra'
        pattern = 'abra'
        actual = brute_force(text, pattern)
        expected = [0, 7]
        self.assertListEqual(actual, expected, 'brute force')

    def test_border(self):
        parameters = [
            ('arba', 'a'), ('abcdab', 'ab'), ('ababab', 'abab'),
        ]
        for input, expected in parameters:
            actual = border(input)
            self.assertEqual(actual, expected, 'border of string')

    def test_border2(self):
        text = 'GGGACATACAGGG'[3:]
        pattern = 'ACATACACACA'
        actual = border(longest_common_prefix(text, pattern))
        lcp = longest_common_prefix(text, pattern)
        self.assertEqual(lcp, 'ACATACA', 'lcp')
        expected = 'ACA'
        self.assertEqual(actual, expected, 'longest common prefix\'s border')

    def test_length_to_skip(self):
        target = 'abcdabcxx'
        pattern = 'abcdabcef'
        actual = length_to_skip(target, pattern)
        expected = 4
        self.assertEqual(actual, expected, 'length to be able to skipped')

    def test_prefix_function_bad(self):
        parameters = [
            ('abababcaab', [0, 0, 1, 2, 3, 4, 0, 1, 1, 2]),
            ('ababcababac', [0, 0, 1, 2, 0, 1, 2, 3, 4, 3, 0])
        ]
        for pattern, expected in parameters:
            actual = prefix_function_bad(pattern)
            self.assertListEqual(actual, expected, 'prefix function')
    
    def test_prefix_function(self):
        parameters = [
            ('abababcaab', [0, 0, 1, 2, 3, 4, 0, 1, 1, 2]),
            ('ababcababac', [0, 0, 1, 2, 0, 1, 2, 3, 4, 3, 0]),
        ]
        for pattern, expected in parameters:
            actual = prefix_function(pattern)
            self.assertListEqual(actual, expected, 'prefix function')

    def test_match_by_prefix_function(self):
        pattern = 'abra'
        text = 'abracadabra'
        actual = match_by_prefix_function(text, pattern)
        expected = [0, 7]
        self.assertListEqual(actual, expected, 'prefix function matching')


if __name__ == "__main__":
    unittest.main()
