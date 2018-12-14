import unittest
from problem1 import sum_equals_num


class MyTestCase(unittest.TestCase):
    def test_sum_equals_num_with_few_nums(self):
        nums = [10, 15, 3, 7]
        k = 17
        self.assertTrue(sum_equals_num(nums, k))

    def test_sum_equals_num_with_negative_num(self):
        nums = [10, 15, 3, 7]
        k = -1
        self.assertFalse(sum_equals_num(nums, k))


if __name__ == '__main__':
    unittest.main()
