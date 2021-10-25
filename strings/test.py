import random
import string
import unittest

from burrows_wheeler import (
    run_length_encoding,
    burrows_wheeler_transform,
    burrows_wheeler_decoding_bad,
    burrows_wheeler_decoding,
)


def random_alphabetic_text(n):
    return ''.join(random.choices(string.ascii_letters, k=n)).upper()


class TestSort(unittest.TestCase):
    """test case for various implementation of sort algorithm
    """

    def test_run_length_encoding1(self):
        input = 'GGGGGGGGGGCCCCCCCCCCCAAAAAAATTTTTTTTTTTTTTTCCCCCG'
        actual = run_length_encoding(input)
        expected = '10G11C7A15T5C1G'
        self.assertEqual(actual.as_encoding(), expected, 'run_length_encoding')

    def test_run_length_encoding2(self):
        input = 'GGGGGGGGGGCCCCCCCCCCCAAAAAAATTTTTTTTTTTTTTTCCCCC'
        actual = run_length_encoding(input)
        expected = '10G11C7A15T5C'
        self.assertEqual(actual.as_encoding(), expected, 'run_length_encoding')

    def test_run_length_encode_decode(self):
        input = random_alphabetic_text(10)
        result = run_length_encoding(input).as_decoding()
        self.assertEqual(
            result, input,
            'run_length encoding/decoding property based testing')

    def test_burrows_wheeler_transform1(self):
        input = 'panamabananas'
        actual = burrows_wheeler_transform(input)
        expected = 'smnpbnnaaaaa$a'
        self.assertEqual(
            actual.as_encoding(), expected,
            'burrows_wheeler_transform')

    def test_burrows_wheeler_transform2(self):
        input = 'AGACATA'
        actual = burrows_wheeler_transform(input)
        expected = 'ATG$CAAA'
        self.assertEqual(
            actual.as_encoding(), expected,
            'burrows_wheeler_transform')

    def test_burrows_wheeler_decoding_bad(self):
        input = 'annb$aa'
        actual = burrows_wheeler_decoding_bad(input)
        expected = 'banana'
        self.assertEqual(actual, expected, 'burrows_wheeler_decoding_bad')

    def test_burrows_wheeler_decoding(self):
        input = 'smnpbnnaaaaa$a'
        actual = burrows_wheeler_decoding(input)
        expected = 'panamabananas$'
        self.assertEqual(actual, expected, 'burrows_wheeler_decoding')


if __name__ == "__main__":
    unittest.main()
