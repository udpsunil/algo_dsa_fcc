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

if __name__ == '__main__':
    unittest.main()
