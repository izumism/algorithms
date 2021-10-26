import random
import string
import unittest

from burrows_wheeler import (
    parse2run_length,
    run_length_encoding,
    burrows_wheeler_transform,
    burrows_wheeler_decoding_bad,
    burrows_wheeler_decoding,
    burrows_wheeler_encoding,
    decorate_index,
    get_top_index,
    get_buttom_index,
    bwt_matching,
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
        self.assertEqual(actual, expected, 'run_length_encoding')

    def test_run_length_encoding2(self):
        input = 'GGGGGGGGGGCCCCCCCCCCCAAAAAAATTTTTTTTTTTTTTTCCCCC'
        actual = run_length_encoding(input)
        expected = '10G11C7A15T5C'
        self.assertEqual(actual, expected, 'run_length_encoding')

    def test_run_length_encode_decode(self):
        input = random_alphabetic_text(10)
        result = parse2run_length(input).as_decoding()
        self.assertEqual(
            result, input,
            'run_length encoding/decoding property based testing')

    def test_burrows_wheeler_encoding1(self):
        input = 'panamabananas'
        actual = burrows_wheeler_encoding(input)
        expected = 'smnpbnnaaaaa$a'
        self.assertEqual(actual, expected, 'burrows_wheeler_encoding1')

    def test_burrows_wheeler_decoding1(self):
        input = 'smnpbnnaaaaa$a'
        actual = burrows_wheeler_decoding(input)
        expected = 'panamabananas$'
        self.assertEqual(actual, expected, 'burrows_wheeler_decoding')

    def test_burrows_wheeler_encoding2(self):
        input = 'AGACATA'
        actual = burrows_wheeler_encoding(input)
        expected = 'ATG$CAAA'
        self.assertEqual(actual, expected, 'burrows_wheeler_encoding2')

    def test_burrows_wheeler_decoding2(self):
        input = 'AGGGAA$'
        actual = burrows_wheeler_decoding(input)
        expected = 'GAGAGA$'
        self.assertEqual(actual, expected, 'burrows_wheeler_decoding')

    def test_bwt_matching(self):
        input = 'panamabananas'
        bw_code = burrows_wheeler_encoding(input)
        self.assertEqual(bw_code, 'smnpbnnaaaaa$a', 'matcher input')
        match_num = bwt_matching(bw_code, 'ana')
        expected = 3
        self.assertEqual(match_num, expected, 'test_bwt_matching')

    def test_bwt_matching_using_func(self):
        input = 'panamabananas'
        bw_code = burrows_wheeler_transform(input).as_encoding()
        self.assertEqual(bw_code, 'smnpbnnaaaaa$a', 'bwt_encode')
        indexed_bw = decorate_index(bw_code)
        buttom_index = len(indexed_bw) - 1
        top_index = get_top_index(indexed_bw, 0, buttom_index, 'a')
        self.assertEqual(top_index, 7, 'top_index')
        buttom_index = get_buttom_index(indexed_bw, 0, buttom_index, 'a')
        self.assertEqual(buttom_index, 13, 'buttom_index')
        buttom_index2 = get_buttom_index(indexed_bw, 1, 6, 'n')
        self.assertEqual(buttom_index2, 6, 'buttom_index2')

    def test_burrows_wheeler_decoding_bad(self):
        input = 'annb$aa'
        actual = burrows_wheeler_decoding_bad(input)
        expected = 'banana'
        self.assertEqual(actual, expected, 'burrows_wheeler_decoding_bad')

if __name__ == "__main__":
    unittest.main()
