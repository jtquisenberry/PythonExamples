import unittest


# https://www.interviewcake.com/question/python/nth-fibonacci?section=dynamic-programming-recursion&course=fc1

# Includes recursion and memoization.
# The memo should be a dictionary where the key is the
# being passed to the first argument of fib and the value
# is the result of the computation.


def fib(n, memo={0: 0}):
    # Calculate the nth Fibonacci number with recursion

    # Edge Case
    if n < 0:
        raise ValueError('n must be positive.')

    # Base case (encompasses 0 and 1)
    if n <= 1:
        return n

    # Return the result from the memo dictionary if available.
    if n in memo:
        return memo[n]

    # Do an operation on nodes that are on the same level.
    # By nodes, imagine that n has nodes
    #           n
    #        /     \
    #      n-1     n-2
    # Here it is "+"
    return fib(n - 1) + fib(n - 2)


# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)