import unittest

# https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation
# Sort ranges of tuples
# Time: O(n * lg(n)) because of the sorting step.
# Space: O(n) -- 1n for sorted_meetings, 1n for merged_meetings.

# First, we sort our input list of meetings by start time so any meetings that might
# need to be merged are now next to each other.
# Then we walk through our sorted meetings from left to right. At each step, either:
# We can merge the current meeting with the previous one, so we do.
# We can't merge the current meeting with the previous one, so we know the previous meeting can't be merged with any
# future meetings and we throw the current meeting into merged_meetings.


def merge_ranges(meetings):

    if len(meetings) < 1:
        return meetings

    # Sort by start time n*log(n)
    sorted_meetings = sorted(meetings)

    # Initialize merged_meetings with the earliest meeting
    # The for loop requires comparison with the latest meeting in the list,
    # so there needs to be a latest meeting in the list.
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
