import unittest
import pytest

# https://www.interviewcake.com/question/python3/nth-fibonacci?course=fc1&section=dynamic-programming-recursion
# Recursion


def fibonacci(n):

    if n < 0:
        raise ValueError("n must be a positive integer")

    if n < 2:
        # print(n)
        return n
    else:
        # print(n-1, n-2, fibonacci(n-1), fibonacci(n-2), fibonacci(n-1) + fibonacci(n-2))
        return fibonacci(n - 1) + fibonacci(n - 2)


x = 10
print(fibonacci(x))
-- 55


# Tests
class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fibonacci(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fibonacci(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fibonacci(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fibonacci(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fibonacci(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fibonacci(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fibonacci(-1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
