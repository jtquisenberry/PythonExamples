import unittest

#my name is john
#name = 3
#wjohn = -1


def find_index(long_string, short_string):
    if len(short_string) > len(long_string):
        raise ValueError('error message')

    if len(short_string) == 0:
        raise ValueError('small_string must contain at least one character.')

    for i in range(len(long_string) - len(short_string)):
        substring = long_string[i:i+len(short_string)]
        if substring == short_string:
            return i

    return -1


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        long = 'my name is john'
        short = 'name'
        expected = 3
        actual = find_index(long, short)
        self.assertEqual(expected, actual)

    def test_2(self):
        long = 'my name is john'
        short = 'wjohn'
        expected = -1
        actual = find_index(long, short)
        self.assertEqual(expected, actual)
