import unittest
import pytest

# https://www.interviewcake.com/question/python/nth-fibonacci?section=dynamic-programming-recursion&course=fc1

# Includes recursion and memoization.
# The memo should be a dictionary where the key is the
# being passed to the first argument of fib and the value
# is the result of the computation.


def fib(n):
    # Calculate the nth Fibonacci number with recursion
    pass


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


if __name__ == '__main__':
    unittest.main(verbosity=2)
