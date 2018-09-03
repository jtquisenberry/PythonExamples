import unittest

# https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation
# Sort ranges of tuples
# sort is n*log(n)

def merge_ranges(meetings):

    if len(meetings) < 1:
        return meetings

    # Sort by start time n*log(n)
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    # Use this alternative for less space use
    # meetings.sort()

    for current_start, current_end in sorted_meetings[1:]:
        merged_start, merged_end = merged_meetings[-1]

        if current_start <= merged_end:
            # Overlapping meeting
            merged_meetings[-1] = (merged_start, max(merged_end, current_end))

        else:
            # Non-overlapping meeting
            merged_meetings.append((current_start, current_end))

    return merged_meetings


# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(1, 4), (2, 5), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
