import unittest


# https://www.interviewcake.com/question/python/temperature-tracker?course=fc1&section=general-programming

# Temperatures rang from 0-110 and are integers.

# Space O(1), the list used to store temperatures for the mode.
# Time O(1)


class TempTracker(object):

    # Implement methods to track the max, min, mean, and mode

    def __init__(self):
        # Mode
        self.occurrences = [0] * 111
        self.max_occurrences = 0
        self.mode = None

        # Mean
        self.number_of_readings = 0
        self.total_sum = 0.0
        self.mean = None

        # Max, Min
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature):
        # Mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.max_occurrences = self.occurrences[temperature]
            self.mode = temperature

        # Mean
        self.number_of_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.number_of_readings

        # Max
        self.max_temp = max(self.max_temp, temperature)
        self.min_temp = min(self.min_temp, temperature)

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode


# Tests

class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TempTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='mean ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max ' + msg)
        self.assertEqual(tracker.get_min(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='mean ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

if __name__ == '__main__':
    unittest.main(verbosity=2)