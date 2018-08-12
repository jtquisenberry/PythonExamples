import unittest

class Test(unittest.TestCase):

    def test_integers(self):
        expected = 0
        actual = 1
        self.assertEqual(expected, actual, msg='xxx')
        #self.assertTrue(1 == 1, 'not true')

#if __name__ == '__main__':
unittest.main()

