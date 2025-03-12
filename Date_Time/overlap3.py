def find_overlapping_intervals(intervals):
    """
    Finds all overlapping intervals in a list of time intervals.

    Args:
        intervals: A list of tuples, where each tuple represents an interval
                   in the format (start_time, end_time).

    Returns:
        A list of tuples, where each tuple represents a pair of overlapping
        intervals.
    """
    overlapping_pairs = []
    n = len(intervals)
    for i in range(n):
        for j in range(i + 1, n):
            if intervals_overlap(intervals[i], intervals[j]):
                overlapping_pairs.append((intervals[i], intervals[j]))
    return overlapping_pairs

def intervals_overlap(interval1, interval2):
    """
    Checks if two time intervals overlap.

    Args:
        interval1: A tuple representing the first interval (start_time, end_time).
        interval2: A tuple representing the second interval (start_time, end_time).

    Returns:
        True if the intervals overlap, False otherwise.
    """
    return interval1[0] < interval2[1] and interval2[0] < interval1[1]

# Example Usage
intervals = [(1, 5), (2, 4), (3, 3.5), (7, 10), (8, 12), (13, 16), (15, 18)]
overlapping_intervals = find_overlapping_intervals(intervals)
print("Overlapping Intervals:", overlapping_intervals)
# Expected Output: Overlapping Intervals: [((1, 5), (2, 4)), ((7, 10), (8, 12)), ((13, 16), (15, 18))]

intervals2 = [(10, 20), (5, 15), (25, 30)]
overlapping_intervals2 = find_overlapping_intervals(intervals2)
print("Overlapping Intervals:", overlapping_intervals2)
# Expected Output: Overlapping Intervals: [((10, 20), (5, 15))]

intervals3 = [(1, 2), (3, 4), (5, 6)]
overlapping_intervals3 = find_overlapping_intervals(intervals3)
print("Overlapping Intervals:", overlapping_intervals3)
# Expected Output: Overlapping Intervals: []