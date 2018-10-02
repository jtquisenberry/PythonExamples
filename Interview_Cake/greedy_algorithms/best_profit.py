# https://www.interviewcake.com/question/python/stock-price?course=fc1&section=greedy
# Greedy algorithm
# Performed in one pass
# Time = O(n)
# Space = O(n) (because using a slice)
# Space = O(1) if change from slice to index.


# For a greedy problem, the idea is to keep track of the best solution
# so far and the variables needed to calculate a better solution if one arises.
# Setup often involves setting initial values to the first elements in a list.
# In this case, setting best profit to 0 would fail to handle the case where only
# a loss is possible. That is why I use the first two elements in stock_prices.

# Greedy often performs a comparison before resetting the best precursors so far.

def get_max_profit(stock_prices):
    if len(stock_prices) < 1:
        raise ValueError('Two prices are required')

    # Calculate the max profit

    minimum_price_so_far = stock_prices[0]
    best_profit_so_far = stock_prices[1] - stock_prices[0]

    # Could save space by using indexing over stock_prices,
    # rather than a slice.
    for price in stock_prices[1:]:

        # Do this first because the current price must not be considered
        # a purchase price to determine the current best profit.
        profit = price - minimum_price_so_far

        # Could also use max(best_profit, current_profit)
        if profit > best_profit_so_far:
            best_profit_so_far = profit

        # Could also use min(lowest_cost_so_far, price)
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

if __name__ == '__main__':
    unittest.main(verbosity=2)