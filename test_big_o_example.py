import unittest
from big_o_example import BigOExamples

class TestBigOExamples(unittest.TestCase):
    def setUp(self):
        self.examples = BigOExamples()

    def test_get_first_element(self):
        self.assertEqual(self.examples.get_first_element([1, 2, 3]), 1)
        self.assertEqual(self.examples.get_first_element(['a', 'b', 'c']), 'a')
        with self.assertRaises(IndexError):
            self.examples.get_first_element([])

    def test_binary_search(self):
        self.assertEqual(self.examples.binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(self.examples.binary_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(self.examples.binary_search([], 1), -1)
        self.assertEqual(self.examples.binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(self.examples.binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_linear_search(self):
        self.assertEqual(self.examples.linear_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(self.examples.linear_search([1, 2, 3, 4, 5], 6), -1)
        self.assertEqual(self.examples.linear_search([], 1), -1)
        self.assertEqual(self.examples.linear_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(self.examples.linear_search([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(self.examples.linear_search([1], 2), -1)
        self.assertEqual(self.examples.linear_search([1], 1), 0)

    def test_merge_sort(self):
        arr = [12, 11, 13, 5, 6, 7]
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [5, 6, 7, 11, 12, 13])

        arr = []
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [])

        arr = [1]
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1])

        arr = [5, 4, 3, 2, 1]
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [1, 2, 3, 4, 5]
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [5, 2, 4, 1, 3, 2]
        self.examples.merge_sort(arr, 0, len(arr)-1)
        self.assertEqual(arr, [1, 2, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()
