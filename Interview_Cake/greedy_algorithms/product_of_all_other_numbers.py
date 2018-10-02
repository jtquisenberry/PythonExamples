import unittest


# https://www.interviewcake.com/question/python/product-of-other-numbers?section=greedy&course=fc1
# Space O(n) for the output list.
# Time O(n) for iterating over the list twice.

# To find the products of all the integers except the integer at each index, we'll go through
# our list greedily twice. First we get the products of all the integers before each index, and
# then we go backwards to get the products of all the integers after each index.
# When we multiply all the products before and after each index, we get our answer - the products
# of all the integers except the integer at each index!


def get_products_of_all_ints_except_at_index(int_list):
    # Make a list with the products

    if len(int_list) < 2:
        raise ValueError('At least two values are required')

    # Specifying a list of [1] is better than [None] because the body
    # of each for loops can be identical.
    # Otherwise, the first for loop must contain output_list[i] = product_so_far
    output_list = [1] * len(int_list)

    product_so_far = 1
    for i in range(len(int_list)):
        output_list[i] *= product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1
    for i in range(len(int_list) - 1, -1, -1):
        output_list[i] *= product_so_far
        product_so_far *= int_list[i]

    return output_list


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


if __name__ == '__main__':
    unittest.main(verbosity=2)