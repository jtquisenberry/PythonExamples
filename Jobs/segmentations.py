import unittest


def return_segmentations(string, subsequences):

    # Edge cases
    if string == None or string == '':
        raise ValueError('string should be populated')

    if len(list(subsequences)) == 0:
        raise IndexError('subsequences should be populated')

    # Convert dictionary to list to impose a consistent order
    subsequences = list(subsequences)

    # A list of possible segmentations
    complete_results = []

    # Use of a stack to store possibly segmentable string.
    string_segments = list()
    string_segments.append([string, []])

    # Continue processing as long as there is a segmentable string.
    while len(string_segments) > 0:
        remainder_of_string, found_segments = string_segments.pop()

        if remainder_of_string == '':
            complete_results.append(found_segments)
        else:

            for sequence in subsequences:
                if remainder_of_string.find(sequence) == 0:
                    remainder = remainder_of_string[len(sequence):]
                    string_segments.append([remainder, found_segments + [sequence]])

    complete_results.sort()
    return complete_results


class Test(unittest.TestCase):

    def test_partially_segmentable(self):
        expected = []
        actual= return_segmentations('intointoA', {'int', 'in', 'to', 'into'})
        self.assertEqual(expected, actual)

    def test_not_at_all_segmentable(self):
        expected = []
        actual = return_segmentations('abc', {'int', 'in', 'to', 'into'})
        self.assertEqual(expected, actual)

    def test_segmenation_with_bad_initial_match(self):
        expected = [['in', 'to', 'in', 'to'], ['in', 'to', 'into'], ['into', 'in', 'to'], ['into', 'into']]
        actual = return_segmentations('intointo', {'int', 'in', 'to', 'into'})
        self.assertEqual(expected, actual)

    def test_segmentation_with_spaces(self):
        expected = []
        actual = return_segmentations('in to', {'int', 'in', 'to', 'into'})
        self.assertEqual(expected, actual)

    def test_longer_word(self):
        expected = [['in', 'in', 'to', 'to', 'in'], ['in', 'into', 'to', 'in']]
        actual = return_segmentations('inintotoin', {'int', 'in', 'to', 'into'})
        self.assertEqual(expected, actual)

    def test_empty_word(self):
        #expected = [['in', 'into', 'to', 'in'], ['in', 'in', 'to', 'to', 'in']]
        with self.assertRaises(Exception):
            return_segmentations(None, {'int', 'in', 'to', 'into'})

    def test_empty_dictionary(self):
        with self.assertRaises(Exception):
            return_segmentations('', {})

if __name__ == '__main__':
    unittest.main()
    print(return_segmentations('inintotoin', {'int', 'in', 'to', 'into'}))
