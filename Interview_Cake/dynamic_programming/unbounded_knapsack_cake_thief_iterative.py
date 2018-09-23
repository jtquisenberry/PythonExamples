import unittest


# https://www.interviewcake.com/question/python/cake-thief?course=fc1&section=dynamic-programming-recursion
# There are unlimited cakes. Each cake is a tuple of (weight, value)
# There is a knapsack of finite capacity. Find the greatest aggregate value of cakes
# that fit in the knapsack.

# Evaluate for each capacity up to total capacity, for each cake type.
# The maximum value at a capacity given a cake is the value of the cake + the maximum
# value at the the current capacity minus the weight of the cake.

# Time: O(n * k) n is number of types of cake and k is the capacity of the knapsack
# Space O(k)


def max_duffel_bag_value(cake_tuples, weight_capacity):
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    # The + 1 is required to ensure there is an index for the full capacity.
    max_values_at_capacities = [0] * (weight_capacity + 1)

    # Look at each possible capacity
    # The + 1 is required to evaluate the total capacity
    for current_capacity in xrange(weight_capacity + 1):

        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        # For each cake
        for cake_weight, cake_value in cake_tuples:

            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # Determine whether the current cake will fit in the current capacity.
            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:
                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities

                max_value_using_cake = (
                        cake_value
                        + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value

    return max_values_at_capacities[weight_capacity]


# Tests

class Test(unittest.TestCase):

    def test_one_cake(self):
        actual = max_duffel_bag_value([(2, 1)], 9)
        expected = 4
        self.assertEqual(actual, expected)

    def test_two_cakes(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 9)
        expected = 9
        self.assertEqual(actual, expected)

    def test_only_take_less_valuable_cake(self):
        actual = max_duffel_bag_value([(4, 4), (5, 5)], 12)
        expected = 12
        self.assertEqual(actual, expected)

    def test_lots_of_cakes(self):
        actual = max_duffel_bag_value([(2, 3), (3, 6), (5, 1), (6, 1), (7, 1), (8, 1)], 7)
        expected = 12
        self.assertEqual(actual, expected)

    def test_value_to_weight_ratio_is_not_optimal(self):
        actual = max_duffel_bag_value([(51, 52), (50, 50)], 100)
        expected = 100
        self.assertEqual(actual, expected)

    def test_zero_capacity(self):
        actual = max_duffel_bag_value([(1, 2)], 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_cake_with_zero_value_and_weight(self):
        actual = max_duffel_bag_value([(0, 0), (2, 1)], 7)
        expected = 3
        self.assertEqual(actual, expected)

    def test_cake_with_non_zero_value_and_zero_weight(self):
        actual = max_duffel_bag_value([(0, 5)], 5)
        expected = float('inf')
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)