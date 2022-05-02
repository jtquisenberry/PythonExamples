import unittest


# https://www.interviewcake.com/question/python/recursive-string-permutations?section=dynamic-programming-recursion&course=fc1
# Get all permutations of a string.
# Iterative version


def get_permutations(string):
    # Generate all permutations of the input string

    if len(string) < 1:
        return set([string])

    #permutations_temp = {''}
    permutations = {''}

    for char in string[:]:


        a = 1

        for permutation in permutations:

            b = 1

            for i in range(len(permutations) + 1):
                start = permutation[:i]
                end = permutation[i:]
                out = start + char + end
                permutations.add(out)

            permutations = permutations

    return permutations


# Tests
'''
class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
'''
print(get_permutations('abc'))