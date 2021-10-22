import unittest
from insertion_sort import insertion_sort
from selection_sort import selection_sort


class TestSort(unittest.TestCase):
    """test case for various implementation of sort algorithm
    """

    def setUp(self):
        self.input = [31, 41, 59, 26, 41, 58]
        self.expected = [26, 31, 41, 41, 58, 59]

    def test_insersion(self):
        actual = insertion_sort(self.input)
        self.assertListEqual(self.expected, actual, "insersion sort")
    
    def test_selection(self):
        actual = selection_sort(self.input)
        self.assertListEqual(self.expected, actual, "selection sort")


if __name__ == "__main__":
    unittest.main()
