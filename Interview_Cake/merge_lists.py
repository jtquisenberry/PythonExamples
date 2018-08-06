import unittest
#https://www.interviewcake.com/question/python/merging-ranges?course=fc1&section=array-and-string-manipulation

def merge_ranges(meetings):
    if len(meetings) < 1:
        return meetings

    # Sort meetings
    sorted_meetings = sorted(meetings)

    meetings_range = []
    meetings_range.append(sorted_meetings[0])

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_meeting_start, last_meeting_end = meetings_range[-1]
        if current_meeting_start <= last_meeting_end:
            # extend the range
            meetings_range[-1] = (last_meeting_start, max(current_meeting_end, last_meeting_end))

        else:
            meetings_range.append((current_meeting_start, current_meeting_end))

    return meetings_range


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


unittest.main(verbosity=2)