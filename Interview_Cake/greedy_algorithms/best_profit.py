# https://www.interviewcake.com/question/python/stock-price?course=fc1&section=greedy
# Greedy algorithm
# Performed in one pass
# Time = O(n)
# Space = O(n) (because using a slice)
# Space = O(1) if change from slice to index.


def get_max_profit(stock_prices):
    if len(stock_prices) < 1:
        raise ValueError('Two prices are required')

    # Calculate the max profit

    minimum_price_so_far = stock_prices[0]
    best_profit_so_far = stock_prices[1] - stock_prices[0]

    for price in stock_prices[1:]:

        profit = price - minimum_price_so_far
        if profit > best_profit_so_far:
            best_profit_so_far = profit

        if price < minimum_price_so_far:
            minimum_price_so_far = price

    return best_profit_so_far


# Tests

import unittest


class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)