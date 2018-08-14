import unittest


class Cat():

    def __init__(self, name, hair_color):

        self._hair_color = hair_color

    # Use of a getter to return hair_color
    @property
    def hair_color(self):
        return self._hair_color

    # Use of a setter to throw AttributeError with a custom message.
    @hair_color.setter
    def hair_color(self, value):
        #raise AttributeError("Property hair_color is read-only.")
        self._hair_color = value


class Test(unittest.TestCase):

    def setUp(self):
        self.cat = Cat('orange', 'Morris')
        self.cat._hair_color = 'black'

    def test_set_hair_color_field(self):
        expected = 'black'
        actual = self.cat._hair_color
        self.assertEqual(expected, actual, 'error at test_set_hair_color')

    def test_set_hair_color_property(self):
        expected = 'white'
        self.cat.hair_color = 'white'
        actual = self.cat.hair_color
        self.assertEqual(expected,actual,'error at test_set_hair_color_property')








if __name__ == '__main__':
    unittest.main()