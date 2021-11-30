import unittest
import pytest

# https://www.interviewcake.com/question/python/nth-fibonacci?section=dynamic-programming-recursion&course=fc1
# Iteration version

# Write a function fib() that takes an integer n and returns the nth Fibonacci number.
#
# Let's say our Fibonacci series is 0-indexed and starts with 0. So:
#
# fib(0)  # => 0
# fib(1)  # => 1
# fib(2)  # => 1
# fib(3)  # => 2
# fib(4)  # => 3
# ...
#
# Gotchas
#
# Our solution runs in n time.
#
# There's a clever, more mathy solution that runs in O(lg(n)) time, but we'll leave that one as a bonus.
#
# If you wrote a recursive function, think carefully about what it does. It might do repeat work,
# like computing fib(2) multiple times!
#
# We can do this in O(1) space. If you wrote a recursive function,
# there might be a hidden space cost in the call stack!
#
# Complexity
#
# O(n) time and O(1) space


def fib(n):
    # Calculate the nth Fibonacci number with iteration
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
