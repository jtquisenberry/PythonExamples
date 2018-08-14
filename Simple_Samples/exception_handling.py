import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def test_equal(self):
        expected = self.a
        actual = 1
        self.assertEqual(expected, actual,'aaa')

    def test_true(self):
        expected = self.b
        actual = 2
        self.assertTrue(expected == actual, 'bbb')

    def test_false(self):
        expected = self.c
        actual = 0
        self.assertFalse(expected == actual, 'ccc')

    def test_exception(self):
        with self.assertRaises(Exception) as context:
            x = 0
            1 / x


if __name__ == '__main__':
    unittest.main()