import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.a = 1
        self.b = 2
        self.c = 3
        #print('setUp')

    def test_equal(self):
        expected = self.a
        actual = 1
        self.assertEqual(expected, actual,'test_equal failed.')

    def test_true(self):
        expected = self.b
        actual = 2
        self.assertTrue(expected == actual, 'test_true failed.')

    def test_false(self):
        expected = self.c
        actual = 0
        self.assertFalse(expected == actual, 'test_false failed.')

    def test_exception(self):
        with self.assertRaises(Exception):
            x = 0
            1 / x

    def tearDown(self):
        #print('teardown')
        pass

if __name__ == '__main__':
    unittest.main()