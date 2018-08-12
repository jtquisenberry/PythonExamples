import unittest
#https://www.interviewcake.com/question/python/nth-fibonacci?course=fc1&section=dynamic-programming-recursion

def fib(n, memo={0: 0}):
    if n < 0:
        raise ValueError('n must be positive.')

    if n <= 1:
        return n

    if n in memo:
        return memo[n]
    else:
        result = fib(n - 1) + fib(n - 2)
        memo[n] = result
        return result


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