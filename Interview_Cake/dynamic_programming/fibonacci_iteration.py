import unittest


# https://www.interviewcake.com/question/python/nth-fibonacci?section=dynamic-programming-recursion&course=fc1

# Iteration version


def fib(n):
    # Calculate the nth Fibonacci number with iteration

    # Edge Case
    if n < 0:
        raise ValueError('n must be a positive integer')

    # Special Cases
    if n <= 1:
        return n

    previous_2 = 0
    previous_1 = 1
    total = 1

    for i in range(2, n + 1):
        total = previous_2 + previous_1
        previous_2 = previous_1
        previous_1 = total

    return total

    # An alternate way to do the iteration
    '''
    counter = 2
    while counter <= n:
        counter += 1
    '''


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