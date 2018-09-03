import unittest


# https://www.interviewcake.com/question/python/reverse-string-in-place?section=array-and-string-manipulation&course=fc1
# space = O(1)
# time = O(n)

# Use a while loop to converge on the center of the list.

def reverse(list_of_chars):
    # Reverse the input list of chars in place

    if len(list_of_chars) < 1:
        return

    start_index = 0
    end_index = len(list_of_chars) - 1

    # <= would also work, but the middle character (if there is an odd number of characters)
    # is already in its final place.
    while start_index < end_index:
        list_of_chars[start_index], list_of_chars[end_index] = \
            list_of_chars[end_index], list_of_chars[start_index]
        start_index += 1
        end_index -= 1

    return


# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        list_of_chars = []
        reverse(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ['A']
        reverse(list_of_chars)
        expected = ['A']
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ['A', 'B', 'C', 'D', 'E']
        reverse(list_of_chars)
        expected = ['E', 'D', 'C', 'B', 'A']
        self.assertEqual(list_of_chars, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)