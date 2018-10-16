import unittest


def is_isomorphic(str1, str2):

    if len(str1) != len(str2):
         return False

    character_map = dict()
    seen_values = set()

    for i in range(len(str1)):

        if str1[i] in character_map:
            if str2[i] != character_map[str1[i]]:
                return False
        else:

            character_map[str1[i]] = str2[i]
            if str2[i] in seen_values:
                return False

        seen_values.add(str2[i])

    return True


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        str1 = 'egg'
        str2 = 'app'

        result = is_isomorphic(str1, str2)
        self.assertTrue(result)

    def test_2(self):
        str1 = 'cow'
        str2 = 'app'

        result = is_isomorphic(str1, str2)
        self.assertFalse(result)

    def test_3(self):
        str1 = 'egs'
        str2 = 'add'

        result = is_isomorphic(str1, str2)
        self.assertFalse(result)

    def test_4(self):
        str1 = 'paper'
        str2 = 'title'

        result = is_isomorphic(str1, str2)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()